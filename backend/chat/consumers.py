import json
import urllib.parse
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.utils import timezone
from .models import Chat, Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_id = self.scope['url_route']['kwargs']['chat_id']
        self.room_group_name = f'chat_{self.chat_id}'
        
        # Verify permissions: must be staff OR session must have this chat_id
        is_staff = self.scope['user'].is_staff
        session_chat_id = self.scope['session'].get('chat_id')
        
        query_string = self.scope.get('query_string', b'').decode('utf-8')
        query_params = dict(urllib.parse.parse_qsl(query_string))
        source = query_params.get('source', 'widget')

        if not (is_staff and source == 'admin') and str(session_chat_id) != str(self.chat_id):
            await self.close()
            return
            
        # Verify chat exists
        chat_exists = await self.check_chat_exists(self.chat_id)
        if not chat_exists:
            await self.close()
            return

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        # Customer connects: notify admins they are online or whatever. 
        # (Requirements don't explicitly ask for online status, but we must broadcast new messages to "admins" group).

        await self.accept()

    async def disconnect(self, close_code):
        if hasattr(self, 'room_group_name'):
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )

    async def receive(self, text_data):
        if not text_data:
            return
            
        try:
            data = json.loads(text_data)
        except json.JSONDecodeError:
            return

        action = data.get('action', 'message')
        
        if action == 'start':
            name = data.get('name', '').strip()
            if not name:
                return
            words = name.split()
            if len(words) < 2 or len(name) < 2 or len(name) > 60:
                return
            import html
            name = html.escape(name)
            
            chat = await database_sync_to_async(Chat.objects.get)(id=self.chat_id)
            if chat.customer_name == "Qonaq":
                chat.customer_name = name
                await database_sync_to_async(chat.save)()
                
                first_name = words[0]
                first_char = first_name[0]
                rest = first_name[1:].lower()
                
                if first_char == 'i': first_char = 'İ'
                elif first_char == 'ı': first_char = 'I'
                elif first_char == 'ə': first_char = 'Ə'
                elif first_char == 'ö': first_char = 'Ö'
                elif first_char == 'ü': first_char = 'Ü'
                elif first_char == 'ş': first_char = 'Ş'
                elif first_char == 'ç': first_char = 'Ç'
                elif first_char == 'ğ': first_char = 'Ğ'
                else: first_char = first_char.upper()
                
                rest = rest.replace('İ', 'i').replace('I', 'ı')
                formatted_first_name = first_char + rest
                
                greeting_text = f"Salam {formatted_first_name}, xoş gəldiniz! Sizə necə kömək edə bilərik?"
                msg_obj, _ = await self.save_message(self.chat_id, greeting_text, 'operator')
                
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'chat_message',
                        'message': msg_obj.text,
                        'sender_type': msg_obj.sender_type,
                        'created_at': msg_obj.created_at.isoformat(),
                        'message_id': msg_obj.id,
                        'chat_id': self.chat_id
                    }
                )
                
                await self.channel_layer.group_send(
                    'admins',
                    {
                        'type': 'admin_notification',
                        'message': f"Yeni müştəri qoşuldu: {name}",
                        'chat_id': self.chat_id,
                        'customer_name': name
                    }
                )

        elif action == 'message':
            message = data.get('message', '').strip()
            
            if not message:
                return
                
            if len(message) > 2000:
                message = message[:2000]

            is_staff = self.scope['user'].is_staff
            query_string = self.scope.get('query_string', b'').decode('utf-8')
            query_params = dict(urllib.parse.parse_qsl(query_string))
            source = query_params.get('source', 'widget')
            
            sender_type = 'operator' if (is_staff and source == 'admin') else 'customer'
            
            if sender_type == 'customer':
                chat = await database_sync_to_async(Chat.objects.get)(id=self.chat_id)
                if chat.customer_name == "Qonaq":
                    return
            
            # Save message
            msg_obj, bot_reply_text = await self.save_message(self.chat_id, message, sender_type)
            
            payload = {
                'type': 'chat_message',
                'message': msg_obj.text,
                'sender_type': msg_obj.sender_type,
                'created_at': msg_obj.created_at.isoformat(),
                'message_id': msg_obj.id,
                'chat_id': self.chat_id
            }

            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                payload
            )

            # If customer sends message, notify admins
            if sender_type == 'customer':
                chat_name = await self.get_chat_name(self.chat_id)
                await self.channel_layer.group_send(
                    'admins',
                    {
                        'type': 'admin_notification',
                        'message': msg_obj.text,
                        'chat_id': self.chat_id,
                        'customer_name': chat_name
                    }
                )
                
            # If bot reply was generated, send it after a short delay
            if bot_reply_text:
                import asyncio
                await asyncio.sleep(1.5)
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'chat_message',
                        'message': bot_reply_text,
                        'sender_type': 'bot',
                        'created_at': timezone.now().isoformat(),
                        'message_id': -1, # bot messages might need real ID, but we save it in save_message
                        'chat_id': self.chat_id
                    }
                )

        elif action == 'read' and self.scope['user'].is_staff:
            await self.mark_messages_read(self.chat_id)
            await self.channel_layer.group_send(
                'admins',
                {
                    'type': 'admin_read_update',
                    'chat_id': self.chat_id
                }
            )

        elif action == 'delete_message':
            message_id = data.get('message_id')
            
            is_staff = self.scope['user'].is_staff
            query_string = self.scope.get('query_string', b'').decode('utf-8')
            query_params = dict(urllib.parse.parse_qsl(query_string))
            source = query_params.get('source', 'widget')
            sender_type = 'operator' if (is_staff and source == 'admin') else 'customer'
            
            if message_id:
                success = await self.delete_message_from_db(message_id, sender_type)
                if success:
                    await self.channel_layer.group_send(
                        self.room_group_name,
                        {
                            'type': 'chat_message_delete',
                            'message_id': message_id,
                            'chat_id': self.chat_id
                        }
                    )

        elif action == 'edit_message':
            message_id = data.get('message_id')
            new_text = data.get('message', '').strip()
            
            is_staff = self.scope['user'].is_staff
            query_string = self.scope.get('query_string', b'').decode('utf-8')
            query_params = dict(urllib.parse.parse_qsl(query_string))
            source = query_params.get('source', 'widget')
            sender_type = 'operator' if (is_staff and source == 'admin') else 'customer'
            
            if message_id and new_text:
                success = await self.edit_message_in_db(message_id, new_text, sender_type)
                if success:
                    await self.channel_layer.group_send(
                        self.room_group_name,
                        {
                            'type': 'chat_message_edit',
                            'message_id': message_id,
                            'message': new_text,
                            'chat_id': self.chat_id
                        }
                    )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'action': 'message',
            'message': event['message'],
            'sender_type': event['sender_type'],
            'created_at': event['created_at'],
            'chat_id': event['chat_id'],
            'message_id': event.get('message_id')
        }))

    async def chat_message_delete(self, event):
        await self.send(text_data=json.dumps({
            'action': 'delete_message',
            'message_id': event['message_id'],
            'chat_id': event['chat_id']
        }))

    async def chat_message_edit(self, event):
        await self.send(text_data=json.dumps({
            'action': 'edit_message',
            'message_id': event['message_id'],
            'message': event['message'],
            'chat_id': event['chat_id']
        }))
        
    @database_sync_to_async
    def check_chat_exists(self, chat_id):
        return Chat.objects.filter(id=chat_id).exists()

    @database_sync_to_async
    def get_chat_name(self, chat_id):
        chat = Chat.objects.filter(id=chat_id).first()
        return chat.customer_name if chat else "Qonaq"

    @database_sync_to_async
    def save_message(self, chat_id, text, sender_type):
        chat = Chat.objects.get(id=chat_id)
        msg = Message.objects.create(
            chat=chat,
            text=text,
            sender_type=sender_type,
            is_read=True if sender_type != 'customer' else False
        )
        
        bot_reply = None
        # Bot logic: reply exactly once per conversation
        if sender_type == 'customer':
            customer_msg_count = Message.objects.filter(chat=chat, sender_type='customer').count()
            if customer_msg_count == 1:
                bot_reply = "Sualınızı operatorlarımıza yönləndirdik, tezliklə cavab veriləcək. Əlavə sualınız varsa, yaza bilərsiniz."
                Message.objects.create(
                    chat=chat,
                    text=bot_reply,
                    sender_type='bot',
                    is_read=True
                )
        
        return msg, bot_reply

    @database_sync_to_async
    def mark_messages_read(self, chat_id):
        Message.objects.filter(chat_id=chat_id, sender_type='customer', is_read=False).update(is_read=True)

    @database_sync_to_async
    def delete_message_from_db(self, message_id, sender_type):
        try:
            msg = Message.objects.get(id=message_id, chat_id=self.chat_id)
            if msg.sender_type != sender_type and sender_type != 'operator':
                return False
            msg.delete()
            return True
        except Message.DoesNotExist:
            return False

    @database_sync_to_async
    def edit_message_in_db(self, message_id, new_text, sender_type):
        try:
            msg = Message.objects.get(id=message_id, chat_id=self.chat_id)
            if msg.sender_type != sender_type and sender_type != 'operator':
                return False
            msg.text = new_text
            msg.save()
            return True
        except Message.DoesNotExist:
            return False


class AdminNotifyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        if not self.scope['user'].is_staff:
            await self.close()
            return

        self.group_name = 'admins'
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        if hasattr(self, 'group_name'):
            await self.channel_layer.group_discard(
                self.group_name,
                self.channel_name
            )

    async def admin_notification(self, event):
        await self.send(text_data=json.dumps({
            'action': 'notify',
            'message': event['message'],
            'chat_id': event['chat_id'],
            'customer_name': event['customer_name']
        }))
        
    async def admin_read_update(self, event):
        await self.send(text_data=json.dumps({
            'action': 'read_update',
            'chat_id': event['chat_id']
        }))

import os
import django
import asyncio

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "websuper.settings")
django.setup()

from channels.testing import WebsocketCommunicator
from django.contrib.auth import get_user_model
from django.contrib.sessions.backends.db import SessionStore
from websuper.asgi import application
from chat.models import Chat, Message
from channels.db import database_sync_to_async

User = get_user_model()

async def test_admin_notify():
    # 1. Create a staff user
    admin_user, _ = await database_sync_to_async(User.objects.get_or_create)(username="admin_test")
    admin_user.is_staff = True
    await database_sync_to_async(admin_user.save)()
    
    # 2. Connect AdminNotifyConsumer
    print("Connecting AdminNotifyConsumer...")
    admin_comm = WebsocketCommunicator(application, "/ws/admin-notify/")
    admin_comm.scope['user'] = admin_user
    admin_session = SessionStore()
    await database_sync_to_async(admin_session.save)()
    admin_comm.scope['session'] = admin_session
    
    connected, _ = await admin_comm.connect()
    print(f"Admin connected: {connected}")
    
    # 3. Create a chat
    chat = await Chat.objects.acreate(customer_name="Test Customer")
    
    # 4. Connect ChatConsumer (as a customer)
    print("Connecting ChatConsumer as customer...")
    customer_comm = WebsocketCommunicator(application, f"/ws/chat/{chat.id}/")
    customer_session = SessionStore()
    customer_session['chat_id'] = str(chat.id)
    await database_sync_to_async(customer_session.save)()
    customer_comm.scope['session'] = customer_session
    from django.contrib.auth.models import AnonymousUser
    customer_comm.scope['user'] = AnonymousUser()
    
    connected_cust, _ = await customer_comm.connect()
    print(f"Customer connected: {connected_cust}")
    
    # 5. Customer sends a message
    print("Customer sending message...")
    await customer_comm.send_json_to({
        "action": "message",
        "message": "Hello from customer!"
    })
    
    # 6. Customer receives echo
    try:
        echo = await customer_comm.receive_json_from()
        print(f"Customer received echo: {echo}")
    except Exception as e:
        print(f"Customer echo error: {e}")
        
    # 7. Admin receives notification
    print("Waiting for admin notification...")
    try:
        notify = await admin_comm.receive_json_from(timeout=3)
        print(f"Admin received: {notify}")
    except Exception as e:
        print(f"Admin receive error: {e}")
        
    await customer_comm.disconnect()
    await admin_comm.disconnect()

if __name__ == "__main__":
    asyncio.run(test_admin_notify())

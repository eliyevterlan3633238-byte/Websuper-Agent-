import os
import django
import asyncio
from channels.testing import WebsocketCommunicator

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "websuper.settings")
django.setup()

from websuper.asgi import application
from chat.models import Chat, Message

async def test_chat():
    print("Creating chat...")
    chat = await Chat.objects.acreate(customer_name="Test User")
    
    print(f"Connecting to /ws/chat/{chat.id}/...")
    communicator = WebsocketCommunicator(application, f"/ws/chat/{chat.id}/")
    # Provide a mock session to bypass the permission check
    communicator.scope['session'] = {'chat_id': str(chat.id)}
    
    connected, subprotocol = await communicator.connect()
    print(f"Connected: {connected}")
    if not connected:
        return
        
    print("Sending message...")
    await communicator.send_json_to({
        "action": "message",
        "message": "Hello from test!"
    })
    
    response = await communicator.receive_json_from()
    print(f"Received back: {response}")
    
    await communicator.disconnect()
    
    messages = [m async for m in Message.objects.filter(chat=chat)]
    for msg in messages:
        print(f"DB Message: {msg.sender_type} - {msg.text}")

if __name__ == "__main__":
    asyncio.run(test_chat())

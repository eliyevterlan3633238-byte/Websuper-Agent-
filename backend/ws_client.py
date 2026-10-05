import asyncio
import websockets
import json
import urllib.request

async def test():
    # 1. Fetch homepage to get a chat_id
    req = urllib.request.Request("http://127.0.0.1:8000/")
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        cookies = response.headers.get('Set-Cookie')
        
    # Extract chat_id from HTML
    import re
    match = re.search(r'<script id="chat-id" type="application/json">"([^"]+)"</script>', html)
    if not match:
        print("Could not find chat-id in HTML")
        return
    chat_id = match.group(1)
    print(f"Got chat_id: {chat_id}")
    
    # 2. Connect to websocket
    headers = {}
    if cookies:
        # Extract sessionid if any
        headers['Cookie'] = cookies.split(';')[0]
    headers['Origin'] = "http://127.0.0.1:8000"
        
        
    uri = f"ws://127.0.0.1:8000/ws/chat/{chat_id}/"
    print(f"Connecting to {uri}")
    try:
        async with websockets.connect(uri, additional_headers=headers) as websocket:
            print("Connected!")
            msg = {"action": "message", "message": "Test from websockets client"}
            await websocket.send(json.dumps(msg))
            print("Sent message.")
            
            res = await websocket.recv()
            print(f"Received: {res}")
            
            # Receive bot reply if any
            try:
                res2 = await asyncio.wait_for(websocket.recv(), timeout=2.0)
                print(f"Received 2: {res2}")
            except asyncio.TimeoutError:
                print("No bot reply within 2 seconds")
    except Exception as e:
        print(f"Failed: {e}")

if __name__ == "__main__":
    asyncio.run(test())

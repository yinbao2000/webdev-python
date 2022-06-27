import asyncio
 
import websockets
import json
import logging
import sys
 

root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)


# create handler for each connection
 
async def handler(websocket, path):

    while True: 
        data = await websocket.recv()
        response = {"Speed": "22", "Error": "5"}
        reply = json.dumps(response)
        await websocket.send(reply)
 
 
start_server = websockets.serve(handler, "localhost", 8081)
 
 
 
asyncio.get_event_loop().run_until_complete(start_server)
 
asyncio.get_event_loop().run_forever()


import asyncio
 
import websockets
import json
import logging
import sys

# create websocket handler for each connection websocket
 
async def websocket_handler(websocket, path):

    # handler is always waiting for client messages

    while True: 
        
        # Read websocket message from client (JSON format)

        data = await websocket.recv()
        logging.info("Received: %s", data)

        # Process client message

        # Send response to client (hardcoded JSON response for now)

        response = {"Speed": "22", "Error": "5"}
        reply = json.dumps(response)
        await websocket.send(reply)
        logging.info("Sent message to websocket client: %s", reply)
 
def main():

    # set up logger to pump logs to console

    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)      # set this to DEBUG will spill a lot more websocket debug messages
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)

    # configure websocket to listen on a port
    start_server = websockets.serve(websocket_handler, "localhost", 8081)
    
    # start server
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    main()


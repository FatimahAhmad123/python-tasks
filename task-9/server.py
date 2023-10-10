#!/usr/bin/python3
import asyncio
import websockets
import datetime
import logging

# Configure the logging
logging.basicConfig(filename="server.log", level=logging.INFO)  # configuring the logging system.

async def server_handler(websocket):  # coroutine
    async for message in websocket:
        # Append a timestamp to the received message
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        response = f"Received '{message}' at {timestamp}"
        
        # Send the modified message back to the client
        await websocket.send(response)

        # Log the received message
        logging.info(f"Received message: {message}")

start_server = websockets.serve(server_handler, "localhost", 8888)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
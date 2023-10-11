#!/usr/bin/python3
import asyncio
import websockets
import datetime
import logging
import json

# Configure the logging
logging.basicConfig(filename="server.log", level=logging.INFO)  # configuring the logging system.

async def server_handler(websocket):  # async coroutine
    async for message in websocket:
        # Append a timestamp to the received message
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") # converts datetime object into string formate
        message_json = json.loads(message)
        message_json['time_stamp']=timestamp
        # response = f"Received '{message}'"
        response_msg=json.dumps(message_json)
        await websocket.send(response_msg)

        # Log the received message
        logging.info(f"Received message: {message}")

start_server = websockets.serve(server_handler, "localhost", 8888)  # websockets API used to generate a communication session between the user's browser and a server

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
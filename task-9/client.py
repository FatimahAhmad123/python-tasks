#!/usr/bin/python3
import asyncio
import websockets
import json
import datetime
import logging

# Configure the logging
logging.basicConfig(filename="client.log", level=logging.INFO)

async def client():
    uri = "ws://localhost:8888"
    async with websockets.connect(uri) as websocket:
        with open("client_messages.json", "r") as json_file:
            messages = json.load(json_file)

        for message_obj in messages:
            method = message_obj["method"]
            message = json.dumps({"jsonrpc": "2.0", "method": method})

            # Log the message before sending
            logging.info(f"Sending message: {message}")

            await websocket.send(message)
            response = await websocket.recv()

            # Log the received response
            logging.info(f"Received response: {response}")

            print(f"Server response: {response}")

asyncio.get_event_loop().run_until_complete(client())
#!/usr/bin/python3
import asyncio
import websockets
import json
import logging
import datetime

# Configure the logging
logging.basicConfig(filename="client.log", level=logging.INFO)

async def client():   # client coroutine
    uri = "ws://localhost:8888"
    async with websockets.connect(uri) as websocket:
        with open("client_messages.json", "r") as json_file:
            messages = json.load(json_file)

        for message_obj in messages:
            message = json.dumps(message_obj)  # for creating json formatted string

            # Log the message before sending
            logging.info(f"Sending message: {message}")
            start_time = datetime.datetime.now()
            
            await websocket.send(message)
            response = await websocket.recv()
            # response_time= json.loads(response)
            # print(response_time["time_stamp"])
            end_time = datetime.datetime.now()
            elapsed_time = end_time - start_time

            # Log the received response
            logging.info(f"Received response: {response}")
            logging.info(f"Time taken: {elapsed_time.total_seconds()} seconds")


            print(f"Server response: {response}")
            print(f"Time taken: {elapsed_time.total_seconds()} seconds")

asyncio.get_event_loop().run_until_complete(client())
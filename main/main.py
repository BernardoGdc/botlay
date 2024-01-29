from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from setup import *


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

async def send_message(message: Message, user_message: str):

    if not user_message:
        print('Message was empty because intents were not enabled probably')
        return
    
    if is_private := user_message[0] == '?':  # (:=) walrus operator will assign the value of the expression on the right to variable to the left.
        user_message = user_message[1:]
    try: 
        response = get_response(user_message)
        await message.author.send(response) if is_private else  await message.channel.send(response)
    except Exception as e:
        print(e)


@client.event
async def on_ready():
    print(f'{client.user} is now running!')

@client.event
async def on_message(message: Message):

    #bot don't respond to itself
    if message.author == client.user:
        return 
    
    username = str(message.author)
    user_message = message.content
    channel = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


def main():
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()
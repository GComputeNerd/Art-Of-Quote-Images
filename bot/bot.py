import discord
from dotenv import load_dotenv
import os
import subprocess

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!sun-tzu "):
        os.system(f'python sun-tzu.py {message.content[9:]}')
        await message.channel.send(file=discord.File('img.png'))

client.run(TOKEN)

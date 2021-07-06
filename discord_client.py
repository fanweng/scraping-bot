#!/usr/bin/env python3

import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
WEBHOOK_URL = os.getenv('DISCORD_MYBOT_GENERAL_WEBHOOK_URL')

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    
    print(
        f'{client.user} is connected to the following Discord guild:\n'
        f'{guild.name} (id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "ping":
        response = "pong"
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException

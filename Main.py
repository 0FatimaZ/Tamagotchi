import discord
import asyncio
import Maintenance 
from 

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

PATH = "./Icons/"

@client.event
async def menu(client, message):
    if 
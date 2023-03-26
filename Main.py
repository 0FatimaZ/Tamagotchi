import discord
import asyncio
import Maintenance 
from Maintenance import Health

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

PATH = "./Icons/"

@client.event
async def menu(message):
    await message.channel.send(file=discord.File(PATH + "Cleancat.png"))
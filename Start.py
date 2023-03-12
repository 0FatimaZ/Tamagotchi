import discord
import asyncio
import Maintenance 

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def menu(message):
    contents = message.content

    if Maintenance.state["stats"].happy == 0:
        await message.channel.send(file=discord.File("CatHappy.png"))
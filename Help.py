import discord
import Maintenance
import asyncio

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def help(client, message):
    contents = message.content
    reply = "Here's a guide for the game:"
    await message.channel.send(reply)
    
    if contents.startswith(">help"):
            reply = Maintenance.helpMes
            for n in reply:
                await message.channel.send(n)
                await asyncio.sleep(3)
               

import discord
import asyncio
import Maintenance 
import pickle

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def start(client, message):
    contents = message.content

    with open('state.p', 'rb') as fp:
        Maintenance.state = pickle.load(fp)
        Maintenance.fridge = pickle.load(fp)
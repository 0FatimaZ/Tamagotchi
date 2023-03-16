import discord
import asyncio
import Maintenance 
import pickle
import random

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def save_pet():
    pass


@client.event
async def start(client, message):
    contents = message.content
    user = message.author.id

    if user in Maintenance.users:
        
        with open('StateDict.p', 'rb') as fp:
            state = pickle.load(fp)
            fridge = pickle.load(fp)
            Maintenance.users[user] = (fridge, state)
    else:
        Maintenance.users[user] = Maintenance.new_stats()

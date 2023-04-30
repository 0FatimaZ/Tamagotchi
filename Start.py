import discord
import Maintenance 
import pickle

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def start(message):
    user = str(message.author.id)
    
    if user in Maintenance.users:
        with open('StateDict.p', 'wb') as fp:
            pickle.load(Maintenance.users, fp, protocol=pickle.HIGHEST_PROTOCOL)
        await message.channel.send("Welcome!")
    else:
        Maintenance.users.update({user: Maintenance.new_stats()})
        print(Maintenance.users)
        await message.channel.send("Welcome to the game!")
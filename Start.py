import discord
import Maintenance 
import pickle

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def start(message):
    contents = message.content
    user = str(message.author.id)

    if contents.startswith(">start"):
        if user in Maintenance.users:
            await message.channel.send("Welcome!")
        else:
            Maintenance.users.update({user: Maintenance.new_stats()})
            print(Maintenance.users)
            await message.channel.send("Welcome to the game!")
    


    
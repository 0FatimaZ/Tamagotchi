import discord
from discord.ext import commands
import asyncio
import Maintenance 
from Maintenance import Health

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

PATH = "./Icons/"

@client.event
async def menu(message):
    user = str(message.author.id)
    (fridge, state) = Maintenance.users[user]

    hungry_pics = discord.File(PATH + "HungerFull.png")
    if state["stats"].hungry <= 0:
        hungry_pics = discord.File(PATH + "HungerLow.png")
    elif state["stats"].hungry == 1:
        hungry_pics = discord.File(PATH + "HungerMiddle.png")
    
    clean_pics = discord.File(PATH + "HealthFull_1.png")
    if state["stats"].clean <= 0:
        clean_pics = discord.File(PATH + "HealthLow.png")
    elif state["stats"].clean == 1:
        clean_pics = discord.File(PATH + "HealthMiddle.png")
    
    happy_pics = discord.File(PATH + "MoodFull.png")
    if state["stats"].happy <= 0:
        happy_pics = discord.File(PATH + "MoodLow.png")
    elif state["stats"].happy == 1:
        happy_pics = discord.File(PATH + "MoodMiddle.png")

    
    cat = None
    happy_pic = discord.File(PATH + "CatHappy.png")
    happy_dirty_pic = discord.File(PATH + "DirtyHappyCat.png")
    sad_pic = discord.File(PATH + "SadCleanCat.jpeg") 
    sad_dirty_pic = discord.File(PATH + "SadDirtyCat.png")
    if state["stats"].happy >= 2 and state["stats"].clean >= 2:
        cat = happy_pic
    elif state["stats"].happy >= 2 and state["stats"].clean <= 1:
        cat = happy_dirty_pic
    elif state["stats"].happy <= 1 and state["stats"].clean >= 2:
        cat = sad_pic
    elif state["stats"].happy <= 1 and state["stats"].clean <= 1:
        cat = sad_dirty_pic
    
    await message.channel.send(files=[hungry_pics])
    await message.channel.send(files=[clean_pics])
    await message.channel.send(files=[happy_pics])
    await message.channel.send(files=[cat])
    await message.channel.send(file=discord.File(PATH + "FastMenu.png"))
    await message.channel.send("Type '>wallet' to see how many buckaloues you have >w<")
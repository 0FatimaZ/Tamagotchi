import discord
from discord.ext import commands
import asyncio
import Maintenance 
from Maintenance import Health

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
#bot = commands.Bot(command_prefix='!')

PATH = "./Icons/"

#pet = Health(hungry=0, clean=0, happy=0)

@client.event
async def menu(message):
    user = str(message.author.id)
    (fridge, state) = Maintenance.users[user]

    hungry_pics = discord.File(PATH + "HungerFull.png")
    if state["stats"].hungry == 0:
        hungry_pics = discord.File(PATH + "HungerLow.png")
    elif state["stats"].hungry == 1:
        hungry_pics = discord.File(PATH + "HungerMiddle.png")
    
    clean_pics = discord.File(PATH + "HealthFull_1.png")
    if state["stats"].clean == 0:
        clean_pics = discord.File(PATH + "HealthLow.png")
    elif state["stats"].clean == 1:
        clean_pics = discord.File(PATH + "HealthMiddle.png")
    
    happy_pics = discord.File(PATH + "MoodFull.png")
    if state["stats"].happy == 0:
        happy_pics = discord.File(PATH + "MoodLow.png")
    elif state["stats"].happy == 1:
        happy_pics = discord.File(PATH + "MoodMiddle.png")
    
    await message.channel.send(files=[hungry_pics])
    await message.channel.send(files=[clean_pics])
    await message.channel.send(files=[happy_pics])

    """ if pet.hungry == 0:
        await message.channel.send(file=discord.File(PATH + "HungerLow.png"))
    elif pet.hungry == 1:
        await message.channel.send(file=discord.File(PATH + "HungerMiddle.png"))
    elif pet.hungry == 2:
        await message.channel.send(file=discord.File(PATH + "HungerFull.png"))
    elif pet.clean == 0:
        await message.channel.send(file=discord.File(PATH + "HealthLow.png"))
    elif pet.clean == 1:
        await message.channel.send(file=discord.File(PATH + "HealthMiddle.png"))
    elif pet.clean == 2:
        await message.channel.send(file=discord.File(PATH + "HealthFull_1.png"))
    elif pet.happy == 0:
        await message.channel.send(file=discord.File(PATH + "MoodLow.png"))
    elif pet.happy == 1:
        await message.channel.send(file=discord.File(PATH + "MoodMiddle.png"))
    elif pet.happy == 2:
        await message.channel.send(file=discord.File(PATH + "MoodFull.png")) """

""" @client.command()
async def menu(ctx):
    pet = Health(hungry=0, clean=0, happy=0)
    if pet.hungry == 0:
        await ctx.send(file=discord.File(PATH + "HungerLow.png"))
    elif pet.hungry == 1:
        await ctx.send(file=discord.File(PATH + "HungerMiddle.png"))
    elif pet.hungry == 2:
        await ctx.send(file=discord.File(PATH + "HungerFull.png"))
    elif pet.clean == 0:
        await ctx.send(file=discord.File(PATH + "HealthLow.png"))
    elif pet.clean == 1:
        await ctx.send(file=discord.File(PATH + "HealthMiddle.png"))
    elif pet.clean == 2:
        await ctx.send(file=discord.File(PATH + "HealthFull_1.png"))
    elif pet.happy == 0:
        await ctx.send(file=discord.File(PATH + "MoodLow.png"))
    elif pet.happy == 1:
        await ctx.send(file=discord.File(PATH + "MoodMiddle.png"))
    elif pet.happy == 2:
        await ctx.send(file=discord.File(PATH + "MoodFull.png")) """
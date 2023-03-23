import discord
import Maintenance
import Icons

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

PATH = "./Icons/"

@client.event
async def wallet(message):

    if Maintenance.state["buckaloues"] == 0:
        reply = ("You currently have 0 buckaloues...")
        await message.channel.send(reply)
        await message.channel.send(file=discord.File(PATH + "EmptyWallet.png"))
    elif Maintenance.state["buckaloues"] < 5: 
        reply = ("You currently have " +  str(Maintenance.state["buckaloues"])  + " buckaloues..that's not much.")
        await message.channel.send(reply)
        await message.channel.send(file=discord.File(PATH + "HalfWallet.png"))
    elif Maintenance.state["buckaloues"] > 5:
        reply = ("You currently have " +  str(Maintenance.state["buckaloues"])  + " buckaloues!")
        await message.channel.send(reply)
        await message.channel.send(file=discord.File(PATH + "FullWallet.png"))
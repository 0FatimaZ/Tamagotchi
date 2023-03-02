import discord
import asyncio
import Maintenance 

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def feed(client, message):
    contents = message.content

    await message.channel.send(file=discord.File("fridge_placeholder.jpg"))
    await message.channel.send("Things in your fridge: ")
    for (name, number) in Maintenance.fridge.items():
        reply = str(name) + ": " + str(number)
        await message.channel.send(reply)
    
    reply = "What would you like to feed your pet?"
    feed_message = await message.channel.send(reply) 
    #for name in Maintenance.fridge:
        #feed_message.add_reaction(name)
    await feed_message.react(":pizza:")


        


import discord
import asyncio
import Maintenance



intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

PATH = "./Icons/"

@client.event
async def shower(client, message):
    contents = message.content
    reply = "Would you like to give Cato a shower?" + "if yes react with" + ': ' + ':shower:'
    shower_message = await message.channel.send(reply)
    await shower_message.add_reaction('🚿')  
    def check(reaction, user):
        return user == message.author and str(reaction.emoji) in ['🚿']
    try:
        reaction, user = await client.wait_for('reaction_add', timeout=10.0, check=check)
        
    except asyncio.TimeoutError:
        try:
            await shower_message.delete()
        except discord.errors.NotFound:
            pass
    
    else:
        if str(reaction.emoji) == '🚿':
            if Maintenance.state["stats"].clean == 3:
                await message.channel.send("Your pet is already clean")
            elif Maintenance.state["stats"].clean < 3:
                reply = "Let's clean your pet" + '⏳'
                await message.channel.send(reply)
                await message.channel.send(file=discord.File(PATH + "Cleancat.png"))
                await asyncio.sleep(5) 
                reply = "Your pet is now clean" + '⌛' + "you recieved 1 buckaloue! :3"
                await message.channel.send(reply)
                Maintenance.state.update({"buckaloues": Maintenance.state["buckaloues"] + 1}) 
                Maintenance.state["stats"].clean = 3
                print(Maintenance.state["stats"].clean)
                print(Maintenance.state["buckaloues"])
                



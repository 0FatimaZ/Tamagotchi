import discord
import asyncio
import Maintenance

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

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
            if Maintenance.state["health"].cleanliness < 3:
                reply = "Let's clean Cato."
                await message.channel.send(reply)
                await message.channel.send(file=discord.File("CleanCat_1.png"))
                await asyncio.sleep(5) 
                reply = "Cato is now clean, you recieved 1 buckaloue! :3"
                await message.channel.send(reply)
                Maintenance.pet.update({"buckaloues": Maintenance.pet["buckaloues"] + 1}) 
                Maintenance.Health.cleanliness +=1

# Hvordan ved spilleren hvor mange buckaloues de har? En speerat commando eller messages der bliver sendt efter hver aktivitet?
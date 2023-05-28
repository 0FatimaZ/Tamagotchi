import discord
import asyncio
import Maintenance
import Main



intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

PATH = "./Icons/"

@client.event
async def shower(client, message):

    user = str(message.author.id)
    (fridge, state) = Maintenance.users[user]

    
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
            await shower_message.delete()

            # Unable to shower because pet has full stats
            if state["stats"].clean >= 2:
                await message.channel.send("Your pet is already clean")
        
           #Showering pet 
            elif state["stats"].clean < 2:
                reply = "Let's clean your pet" + '⏳'
                await message.channel.send(reply)
                await message.channel.send(file=discord.File(PATH + "Cleancat.png"))
                await asyncio.sleep(3) 
                reply = "Your pet is now clean" + '⌛' + "you recieved 1 buckaloue! :3"
                await message.channel.send(reply)
            #Updating corresponding variables
                state["buckaloues"] += 1
                print(state["buckaloues"])
                state["stats"].clean += 2
                state["stats"].happy -= 1
                if state["stats"].happy < 0:
                    state["stats"].happy = 0
                print(str(state["stats"].clean))
            
            #showering pet 
            elif state["stats"].clean == 0:
                reply = "Your pet could really use a shower..." + '⏳'
                await message.channel.send(reply)
                await message.channel.send(file=discord.File(PATH + "Cleancat.png"))
                await asyncio.sleep(3) 
                reply = "Your pet is now clean" + '⌛' + "you recieved 1 buckaloue! :3"
                await message.channel.send(reply)
                state["buckaloues"] += 1
                state["stats"].clean += 2
            
            await Main.menu(message)
                

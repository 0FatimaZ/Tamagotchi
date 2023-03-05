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
    if Maintenance.fridge["empty"] == True:
        await message.channel.send("Your fridge is empty :(")
        await message.channel.send("Go to the *>shop* to by more food.")
    else:
        await message.channel.send("Things in your fridge: ")
        for (name, Food) in Maintenance.fridge.items():
            if Food > 0:
                reply = str(name) + ": " + str(Food)
                await message.channel.send(reply)
        

        reply = f"What would you like to feed your pet?"
        feed_message = await message.channel.send(reply)
        for (name, Food) in Maintenance.fridge.items():
            if Food > 0:
                await feed_message.add_reaction(name)
        
        def check(reaction, user):
            return user == message.author and str(reaction.emoji) in list(Maintenance.fridge.keys())
        
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=10.0, check=check)
        

        except asyncio.TimeoutError:
            try:
                await feed_message.delete()
            except discord.errors.NotFound:
                pass
            reaction = None
        
        
        if reaction is not None:

            if str(reaction.emoji) in list(Maintenance.fridge.keys()):
                Maintenance.fridge.update({str(reaction.emoji): Maintenance.fridge[str(reaction.emoji)] - 1}) 
                if all(Food == 0 for Food in Maintenance.fridge.values()):
                    Maintenance.fridge.update({"empty": True})
               #? else:
               #?     if Maintenance.pet.Health.hunger["stats"] < 3:
               #?         Maintenance.pet.update({"stats": Maintenance.pet.Health.hunger["stats"] + 1}) 
                Maintenance.pet.update({"buckaloues": Maintenance.pet["buckaloues"] + 1}) 
                await message.channel.send("You fed your pet!! and you got 1 buckaloue :3")


            

        


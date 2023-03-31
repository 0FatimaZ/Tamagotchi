import discord
import asyncio
import Maintenance 
import Main

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

PATH = "./Icons/"

@client.event
async def shop(client, message):

    user = str(message.author.id)
    (fridge, state) = Maintenance.users[user]
    
    
    if state["buckaloues"] <= 0:
        await message.channel.send("Your are too poor to buy anything 3:")
    else:
        reply = "You have " + str(state["buckaloues"]) + " buckaloues."
        await message.channel.send(reply)

        await message.channel.send("What would you like to buy?")
        shop_message = await message.channel.send(file=discord.File(PATH + "shop.PNG"))
        await shop_message.add_reaction("🍕")
        await shop_message.add_reaction("🍓")
        await shop_message.add_reaction("🍩")
        await shop_message.add_reaction("🍙")
    
        def check(reaction, user):
            return user and str(reaction.emoji) in list(fridge.keys())
        
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=10.0, check=check)
        

        except asyncio.TimeoutError:
            try:
                await shop_message.delete()
            except discord.errors.NotFound:
                pass
            reaction = None
        
        
        if reaction is not None:
            price = fridge[str(reaction.emoji)].price
            if str(reaction.emoji) in list(fridge.keys()) and state["buckaloues"] >= price:
                state["buckaloues"] -= fridge[str(reaction.emoji)].price 
                fridge[str(reaction.emoji)].number += 1
                await message.channel.send("You bought a " + str(reaction.emoji) + "!")
            else:
                await message.channel.send("You don't have enough buckaloues to buy this item :'(")
        await Main.menu(message)
        
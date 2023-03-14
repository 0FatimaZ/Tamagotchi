import discord
import asyncio
import Maintenance 

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

PATH = "./Icons/"

@client.event
async def shop(client, message):
    contents = message.content

    if Maintenance.state["buckaloues"] <= 0:
        await message.channel.send("Your are too poor to buy anything 3:")
    else:
        reply = "You have " + str(Maintenance.state["buckaloues"]) + " buckaloues."
        await message.channel.send(reply)

        await message.channel.send("What would you like to buy?")
        shop_message = await message.channel.send(file=discord.File(PATH + "shop.PNG"))
        await shop_message.add_reaction("🍕")
        await shop_message.add_reaction("🍓")
        await shop_message.add_reaction("🍩")
        await shop_message.add_reaction("🍙")
    
        def check(reaction, user):
            return user == message.author and str(reaction.emoji) in list(Maintenance.fridge.keys())
        
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=10.0, check=check)
        

        except asyncio.TimeoutError:
            try:
                await shop_message.delete()
            except discord.errors.NotFound:
                pass
            reaction = None
        
        
        if reaction is not None:
            price = Maintenance.fridge[str(reaction.emoji)].price
            if str(reaction.emoji) in list(Maintenance.fridge.keys()) and Maintenance.state["buckaloues"] >= price:
                Maintenance.state.update({"buckaloues": Maintenance.state["buckaloues"] - Maintenance.fridge[str(reaction.emoji)].price})
                new_number = Maintenance.fridge[str(reaction.emoji)].number + 1
                print(new_number)
                Maintenance.fridge.update({str(reaction.emoji): Maintenance.Food(new_number, Maintenance.fridge[str(reaction.emoji)].price)})
                await message.channel.send("You bought a " + str(reaction.emoji) + "!")
            else:
                await message.channel.send("You don't have enough buckaloues to buy this item :'(")
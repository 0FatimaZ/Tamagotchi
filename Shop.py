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

        await message.channel.send("Select your items and then simply wait for the confimation message. Then you can confirm by typing '>buy'.")
    
        # Collect reactions
        def check(reaction, user):
            return user == message.author and str(reaction.emoji) in list(fridge.keys())

        selected_items = []
        while True:
            try:
                reaction, user = await client.wait_for('reaction_add', timeout=10.0, check=check)
            except asyncio.TimeoutError:
                break

            selected_items.append(str(reaction.emoji))
            await reaction.remove(user)

        # Check if any items were selected
        if len(selected_items) == 0:
            await message.channel.send("You didn't select anything! :0")
            return
        
        # Confirm purchase
        purchase_message = await message.channel.send("Purchase " + ", ".join(selected_items) + "? Type '>buy' to confirm :3")
        try:
            confirm = await client.wait_for('message', timeout=10.0, check=lambda m: m.author == message.author and m.content == '>buy')
        except asyncio.TimeoutError:
            await message.channel.send("You didn't confirm! :0 Purchase cancelled.")
            return
 
        # Purchase items
        total_price = 0
        for item in selected_items:
            price = fridge[item].price
            if state["buckaloues"] >= price:
                state["buckaloues"] -= price
                fridge[item].number += 1
                total_price += price
            else:
                await message.channel.send("You don't have enough buckaloues to buy " + item + " :'(")
        
        # Send confirmation message
        if total_price > 0:
            await message.channel.send("You bought " + ", ".join(selected_items) + " for " + str(total_price) + " buckaloues!")
        await Main.menu(message)
        
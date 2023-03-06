import discord
import asyncio
import Maintenance 

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def shop(client, message):
    contents = message.content

    reply = "you have " + str(Maintenance.state[])
    await message.channel.send(reply)
    await message.channel.send(file=discord.File("shop_placeholder.jpg"))


    """
        await message.channel.send("Things in your fridge: ")
        for (name, food) in Maintenance.fridge.items():
            if food.number > 0:
                reply = str(name) + ": " + str(food.number)
                await message.channel.send(reply)
        

        reply = f"What would you like to feed your pet?"
        feed_message = await message.channel.send(reply)
        for (name, food) in Maintenance.fridge.items():
            if food.number > 0:
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
                if Maintenance.state["stats"].hungry == 3:
                    await message.channel.send("Your pet is full ❤️")
                else:
                    new_number = Maintenance.fridge[str(reaction.emoji)].number - 1
                    Maintenance.fridge.update({str(reaction.emoji): Maintenance.Food(new_number, Maintenance.fridge[str(reaction.emoji)].price)})
                    new_hungry = Maintenance.state["stats"].hungry + 1
                    Maintenance.state.update({"stats": Maintenance.Health(new_hungry, Maintenance.state["stats"].clean,  Maintenance.state["stats"].happy)})    
                    await message.channel.send("You fed your pet!!")
            """
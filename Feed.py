import discord
import asyncio
import Maintenance 

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

PATH = "./Icons/"

Feed = {"feeding": 0}

def fridge_empty(message):
    user = str(message.author.id)
    (fridge, state) = Maintenance.users[user]
    total = 0
    for food in fridge.values():
        total += food.number
    return total == 0

@client.event
async def feed(client, message):
    user = str(message.author.id)
    (fridge, state) = Maintenance.users[user]

    while Feed["feeding"] == 0:
        Feed.update({"feeding": 1})

        if fridge_empty(message) == True:
            await message.channel.send(file=discord.File(PATH + "fridge_empty.PNG"))
            await message.channel.send("Your fridge is empty :(")
            await message.channel.send("Go to the *>shop* to by more food.")
        elif fridge_empty(message) == False:
            await message.channel.send(file=discord.File(PATH + "fridge_full.PNG"))
            await message.channel.send("Things in your fridge: ")
            for (name, food) in fridge.items():
                if food.number > 0:
                    reply = str(name) + ": " + str(food.number)
                    await message.channel.send(reply)
            

            reply = "What would you like to feed your pet?"
            feed_message = await message.channel.send(reply)
            for (name, food) in fridge.items():
                if food.number > 0:
                    await feed_message.add_reaction(name)
            
            def check(reaction, user):
                return user == message.author and str(reaction.emoji) in list(fridge.keys())
            
            try:
                reaction, user = await client.wait_for('reaction_add', timeout=10.0, check=check)
            

            except asyncio.TimeoutError:
                try:
                    await feed_message.delete()
                except discord.errors.NotFound:
                    pass
                reaction = None
            
            
            
            if reaction is not None and Feed["feeding"] == 1:
                if str(reaction.emoji) in list(fridge.keys()):
                    if state["stats"].hungry == 3:
                        await message.channel.send("Your pet is full ❤️")
                    else:
                        fridge[str(reaction.emoji)].number - 1
                        state["stats"].hungry + 1   
                        await message.channel.send("You fed your pet!!")
                Feed.update({"feeding": 1})


                
   




            

        


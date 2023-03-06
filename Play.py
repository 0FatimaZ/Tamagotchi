import discord
import asyncio
import random

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

cup = ["🪣", "🪣", "🪣", "🪣", "🐭"]

Game = {"cup_game": 0}

@client.event
async def play(client, message):
    contents = message.content
    reply = f"What game would you like to play? (You can currently only play one game)"
    game_message = await message.channel.send(reply)
    await game_message.add_reaction('🪣')

    def check(reaction, user):
        return user == message.author and str(reaction.emoji) in ['🪣']
    try:
        reaction, user = await client.wait_for('reaction_add', timeout = 10.0, check = check)
        
    except asyncio.TimeoutError:
        try:
            await game_message.delete()
        except discord.errors.NotFound:
            pass
        reaction = None
    
    else:
        if reaction is not None:
            if str(reaction.emoji) == '🪣' and  Game["cup_game"] == 0:
                reply = "Let's play the cup game."
                await message.channel.send(reply)
                random.shuffle(cup)
                msg1 = await message.channel.send("🪣🪣🪣🪣🪣")
                await asyncio.sleep(3)
                await msg1.delete()
                msg2 = await message.channel.send("".join(cup))
                await asyncio.sleep(3)
                await msg2.delete()
                msg1 = await message.channel.send("🪣🪣🪣🪣🪣")
                Game.update({"cup_game": 1})
                print(Game["cup_game"])

""" @client.event
async def play(client, message):
    contents = message.content
    reply = f"Where is the mouse?"
    game_message = await message.channel.send(reply)

    if Game["cup_game"] == 1:
        if contents.startswith("!1"):
            if cup[0] =="🐭":
                await message.channel.send("You found the mouse!")
        elif contents.startswith("!2"):
            if cup[1] == "🐭":
                await message.channel.send("You found the mouse!")
        elif contents.startswith("!3"):
            if cup[2] == "🐭":
                await message.channel.send("You found the mouse!")
        elif contents.startswith("!4"):
            if cup[3] == "🐭":
                await message.channel.send("You found the mouse!")
        elif contents.startswith("!5"):
            if cup[4] == "🐭":
                await message.channel.send("You found the mouse!")
        else:
            await message.channel.send("Where is the mouse?!") """

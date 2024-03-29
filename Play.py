import discord
import asyncio
import random
import Maintenance
import Main


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
            await game_message.delete()
            if str(reaction.emoji) == '🪣' and  Game["cup_game"] == 0:
                reply = "Let's play the cup game."
                await message.channel.send(reply)
                reply = "For choosing the cup, write its order number"
                await message.channel.send(reply)
                random.shuffle(cup)
                msg1 = await message.channel.send("🪣🪣🪣🪣🪣")
                await asyncio.sleep(3)
                await msg1.delete()
                msg2 = await message.channel.send("".join(cup))
                await asyncio.sleep(0.5)
                await msg2.delete()
                msg1 = await message.channel.send("🪣🪣🪣🪣🪣")
                Game.update({"cup_game": 1})
                reply = f"Where is the mouse?"
                game_message = await message.channel.send(reply)


@client.event
async def play_2(message):
    contents = message.content
    user = str(message.author.id)
    (fridge, state) = Maintenance.users[user]
    state["stats"].hungry -= 1
    if state["stats"].hungry < 0:
         state["stats"].hungry = 0

    if cup[0] =="🐭":
        if contents.startswith("1"):
            await message.channel.send("You found the mouse!")
            state["stats"].happy += 1
            state["buckaloues"] += 1
            await message.channel.send("You received 1 buckaloue!")
            print(state["stats"].happy)
        elif contents.startswith("2" or "3" or "4" or "5"):
                await message.channel.send("Uuuuuh. Better luck next time!")
        else:
            await message.channel.send("What? What does that even mean?")
        Game.update({"cup_game": 0})

    elif cup[1] == "🐭":
        if contents.startswith("2"):
            await message.channel.send("You found the mouse!")
            state["stats"].happy += 1
            state["buckaloues"] += 1
            await message.channel.send("You received 1 buckaloue!")
            print(state["stats"].happy)
        elif contents.startswith("1" or "3" or "4" or "5"):
                await message.channel.send("Uuuuuh. Better luck next time!")
        else:
            await message.channel.send("What? What does that even mean?")
        Game.update({"cup_game": 0})

    elif cup[2] == "🐭":
        if contents.startswith("3"):
            await message.channel.send("You found the mouse!")
            state["stats"].happy += 1
            state["buckaloues"] += 1
            await message.channel.send("You received 1 buckaloue!")
            print(state["stats"].happy)
        elif contents.startswith("2" or "1" or "4" or "5"):
                await message.channel.send("Uuuuuh. Better luck next time!")
        else:
            await message.channel.send("What? What does that even mean?")
        Game.update({"cup_game": 0})

    elif cup[3] == "🐭":
        if contents.startswith("4"):
            await message.channel.send("You found the mouse!")
            state["stats"].happy += 1
            state["buckaloues"] += 1
            await message.channel.send("You received 1 buckaloue!")
            print(state["stats"].happy)
        elif contents.startswith("2" or "3" or "1" or "5"):
                await message.channel.send("Uuuuuh. Better luck next time!")
        else:
            await message.channel.send("What? What does that even mean?")
        Game.update({"cup_game": 0})

    elif cup[4] == "🐭":
        if contents.startswith("5"):
            await message.channel.send("You found the mouse!")
            state["stats"].happy += 1
            state["buckaloues"] += 1
            await message.channel.send("You received 1 buckaloue!")
            print(state["stats"].happy)
        elif contents.startswith("2" or "3" or "4" or "1"):
                await message.channel.send("Uuuuuh. Better luck next time!")
        else:
            await message.channel.send("What? What does that even mean?")
        Game.update({"cup_game": 0})
    
    await Main.menu(message)

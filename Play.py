import discord
import asyncio
import random

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

cup = [":bucket:", ":bucket:", ":bucket:", ":bucket:", ":mouse:"]

Game = {"cup_game": 0}

@client.event
async def gank_lane(client, message):
    contents = message.content
    reply = "What game would you like to play? (You can currently only play one game)"
    game_message = await message.channel.send(reply)
    await game_message.add_reaction(':bucket:')

    def check(reaction, user):
        return user == message.author and str(reaction.emoji) in [':bucket:']
    try:
        reaction, user = await client.wait_for('reaction_add', timeout = 10.0, check = check)
        
    except asyncio.TimeoutError:
        try:
            await game_message.delete()
        except discord.errors.NotFound:
            pass
    
    else:
        if str(reaction.emoji) == ':bucket:'and  Game["cup_game"] == 0:
            reply = "Let's play the cup game."
            await message.channel.send(reply)
            Game.update({"cup_game": 1})

            if Game["cup_game"] == 1:
                random.shuffle(cup)
                msg1 = await message.channel.send(":bucket::bucket::bucket::bucket::bucket:")
                await asyncio.sleep(3)
                await msg1.delete()
                msg2 = await message.channel.send("".join(cup))
                await asyncio.sleep(3)
                await msg2.delete()
                msg1 = await message.channel.send(":bucket::bucket::bucket::bucket::bucket:")
                await message.channel.send("Where is the mouse?")
                Game.update({"cup_game": 2})
            
            elif Game["cup_game"] == 2:
                if contents.startswith("1"):
                    if cup[0]==":mouse:":
                        await message.channel.send("You found the mouse!")
                        Game.update({"cup_game": 0})
                elif contents.startswith("2"):
                    if cup[1]==":mouse:":
                        await message.channel.send("You found the mouse!")
                        Game.update({"cup_game": 0})
                elif contents.startswith("3"):
                    if cup[2]==":mouse:":
                        await message.channel.send("You found the mouse!")
                        Game.update({"cup_game": 0})
                elif contents.startswith("4"):
                    if cup[3]==":mouse:":
                        await message.channel.send("You found the mouse!")
                        Game.update({"cup_game": 0})
                elif contents.startswith("5"):
                    if cup[4]==":mouse:":
                        await message.channel.send("You found the mouse!")
                        Game.update({"cup_game": 0})

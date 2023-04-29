import discord
import asyncio
import Maintenance
import Play
from Play import Game
import Feed
import Shower
import Wallet
import Quit
import Start
import Shop
import Main


intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.members = True

client = discord.Client(intents=intents)
TOK_FILE = "token.txt"

def get_token():
  tokfile = open(TOK_FILE, 'r')
  token = tokfile.read()
  tokfile.close()
  return token

@client.event
async def on_ready():
    print("Connected!")

@client.event
async def on_member_join():
    global player
    player = Maintenance.Stats()


#mainloop
@client.event
async def on_message(message):
    global run_game
    contents = message.content.lower()

    user = str(message.author.id)

    if not (message.author.bot):
      if contents.startswith(">start"):
        await Start.start(message)
        await Main.menu(message)
      (fridge, state) = Maintenance.users[user] 

      if state["stage"] == 0: 
        state["stage"] = 1
        state.update({"stage": 1})
            
      elif state["stage"] == 1:

        if contents.startswith(">help"):
          reply = Maintenance.helpMes
          for n in reply:
              await message.channel.send(n)
              await asyncio.sleep(2)

        elif contents.startswith(">wallet"):
            await Wallet.wallet(message)

        elif contents.startswith(">feed"):
            await Feed.feed(client, message)
            print(str(state["stats"].hungry))

        elif contents.startswith(">shower"):
            await Shower.shower(client, message)

        elif contents.startswith(">play") and Game["cup_game"] == 0:
            await Play.play(client, message)
            
        elif Game["cup_game"] == 1:
            await Play.play_2(message)
        
        elif contents.startswith(">shop"):
            await Shop.shop(client, message)

        elif contents.startswith(">menu"):
            await Main.menu(message)

        elif contents.startswith(">quit"): 
            state["stage"] = 0
            print(str(state["stage"]))
            await Quit.quit(message)
            pass
            
        else:
            pass
    

token = get_token()
client.run(token)
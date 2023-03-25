import discord
import asyncio
import Maintenance
import Play
import Feed
import Shower
import Wallet
import Quit
import Start
import Shop
#import pickle


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
    contents = message.content

    user = str(message.author.id)

    if not (message.author.bot):
      await Start.start(message)
      #await message.channel.send (Start.start(message))
      (fridge, state) = Maintenance.users[user]

      if state["stage"] == 0:
        await message.channel.send("Welcome!")
        # await Main.main(client, message)
        state["stage"] = 1
        state.update({"stage": 1})

      elif state["stage"] >= 1:
        if contents.startswith(">help"):
          reply = Maintenance.helpMes
          for n in reply:
              await message.channel.send(n)
              await asyncio.sleep(2)

        elif contents.startswith(">wallet"):
            await Wallet.wallet(message)

        elif contents.startswith(">quit"):
            await Quit.quit(message)
            
      elif state["stage"] == 1:
        if contents.startswith(">feed"):
            await Feed.feed(client, message)

        elif contents.startswith(">shower"):
            await Shower.shower(client, message)

        elif contents.startswith(">play"):
            await Play.play(client, message)
        
        elif contents.startswith(">shop"):
            await Shop.shop(client, message)

        elif contents.startswith(">quit"):
            state["stage"] == 1
            await Quit.quit(client, message) 
            
      

token = get_token()
client.run(token)
    # user = message.author.id

    # if not (message.author.bot):
        
    #     if user in Maintenance.users:

    #       if contents.startswith(">start"):
    #         if user in Maintenance.users:
        
    #             with open('StateDict.p', 'rb') as fp:
    #                 state = pickle.load(fp)
    #                 fridge = pickle.load(fp)
    #                 Maintenance.users[user] = (fridge, state)
    #         else:
    #             Maintenance.users[user] = Maintenance.new_stats() 
            
    #         (userfridge, userstate) = Maintenance.users[user]
    #         await message.channel.send("Welcome!")
            

    #       if userstate["stage"] == 2:
          
    #         if contents.startswith(">feed"):
    #           await Feed.feed(client, message)

    #         elif contents.startswith(">shower"):
    #           await Shower.shower(client, message)

    #         elif contents.startswith(">play"):
    #           await Play.play(client, message)

    #         elif contents.startswith(">help"):
    #             reply = Maintenance.helpMes
    #             for n in reply:
    #                 await message.channel.send(n)
    #                 await asyncio.sleep(2)

    #         elif contents.startswith(">wallet"):
    #           await Wallet.wallet(client, message)

    #         elif contents.startswith(">shop"):
    #           await Shop.shop(client, message)

            
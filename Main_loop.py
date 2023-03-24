import discord
import asyncio
import Maintenance
import Start
import Play
import Feed
import Shower
import Wallet
import Shop
import Quit
#import Main

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
    user = message.author.id

    if not (message.author.bot):
      await Start.start(message)
      (fridge, state) = Maintenance.users[user]

      if state["stage"] == 0:
        await message.channel.send("Welcome!")
        # await Main.main(client, message)
        state["stage"] = 1

      if state["stage"] >= 1:
        if contents.startswith(">help"):
          reply = Maintenance.helpMes
          for n in reply:
              await message.channel.send(n)
              await asyncio.sleep(2)

        elif contents.startswith(">wallet"):
            await Wallet.wallet(message)

        elif contents.startswith(">quit"):
            await Quit.quit(message)
            
      if state["stage"] == 1:
        if contents.startswith(">feed"):
            await Feed.feed(client, message)

        elif contents.startswith(">shower"):
            await Shower.shower(client, message)

        elif contents.startswith(">play"):
            await Play.play(client, message)
        
        elif contents.startswith(">shop"):
            await Shop.shop(client, message)


        #    if stage == 3:
        #     await Main.main(client, message)

                
                
           

token = get_token()
client.run(token)
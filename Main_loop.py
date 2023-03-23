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
    (userstate) = Maintenance.users[user]

    if not (message.author.bot):
        
        if userstate["stage"] == 1:

          if contents.startswith(">Start"):
            Maintenance.state.update({"stage": 2})
            await message.channel.send("Welcome!")
            await Start.start(client, message) #mangler at sende stats, cato, og menu, ift health 
          
          if userstate["stage"] == 2:

            if contents.startswith(">feed"):
              await Feed.feed(client, message)

            elif contents.startswith(">shower"):
              await Shower.shower(client, message)

            elif contents.startswith(">play"):
              await Play.play(client, message)

            elif contents.startswith(">help"):
                reply = Maintenance.helpMes
                for n in reply:
                    await message.channel.send(n)
                    await asyncio.sleep(2)

            elif contents.startswith(">wallet"):
              await Wallet.wallet(client, message)

            elif contents.startswith(">shop"):
              await Shop.shop(client, message)

            elif contents.startswith(">quit"):
              userstate["stage"] == 1
              await Quit.quit(client, message) 
            
      
        

      
      

token = get_token()
client.run(token)
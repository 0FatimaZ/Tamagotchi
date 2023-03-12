import discord
import asyncio
import Maintenance
import Play
import Feed
import Shower


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
async def on_member_join(member):
    global player
    player = Maintenance.Stats()


#mainloop
@client.event
async def on_message(message):
    global run_game
    contents = message.content
    user = message.author.id
    
    if not (message.author.bot):

      
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
                await asyncio.sleep(3)
      elif contents.startswith(">wallet"):
         reply = ("You've got" + Maintenance.state["buckaloues"] + "buckaloues!")
         await message.channel.send(reply)

      
      



token = get_token()
client.run(token)
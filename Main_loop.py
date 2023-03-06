import discord
import asyncio
import Maintenance
import Play
import Feed
import Shower
import Help

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

      
      if contents.startswith("f"):
         await Feed.feed(client, message)
      elif contents.startswith(">shower"):
         await Shower.shower(client, message)
      elif contents.startswith("p"):
        await Play.play(client, message)
      elif contents.startswith(">help"):
         await Help.help(client, message)

      
      



token = get_token()
client.run(token)
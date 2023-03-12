import discord
import asyncio
import Maintenance
import Play
import Feed
import Shower
import Help
from Play import Game

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.members = True

client = discord.Client(intents=intents)
TOK_FILE = "token_Am.txt"

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
    player = Maintenance.Health()


#mainloop
@client.event
async def on_message(message):
    global run_game
    contents = message.content
    user = message.author.id
    
    if not (message.author.bot):
        
        if contents.startswith("feed"):
            await Feed.feed(client, message)
        
        elif contents.startswith("shower"):
            await Shower.shower(client, message)
        
        elif contents.startswith("g") and Game["cup_game"] == 0:
            await Play.play(client, message)
        
        elif Game["cup_game"] == 1:
            await Play.play_2(message)
        
        elif contents.startswith(">Help"):
            await Help.help(client, message)
      
      



token = get_token()
client.run(token)
import discord
import asyncio
import Maintenance
import Play

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
      return x



token = get_token()
client.run(token)
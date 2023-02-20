import discord
import datetime
from datetime import datetime, timedelta

DEBUG = True

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

TOK_FILE = "token.txt"

user_pet_food = {}
pet_owners = {}
pets = []

time_to_die = timedelta(hours=24)
if DEBUG:
    time_to_die = timedelta(minutes=1)

def add_user_pet(user, pet):
    time = datetime.now()
    if user in pet_owners:
        pet_owners[user].append(pet)
    else:
        pet_owners[user] = [pet]
    user_pet_food[user] = time

def get_token():
  tokfile = open(TOK_FILE, 'r')
  token = tokfile.read()
  tokfile.close()
  return token

@client.event
async def on_ready():
    print("Connected!")


@client.event
async def on_message(message):
    contents = message.content
    user = message.author.id

# Check pet shop
    if contents == "!shop":
        reply = "Are you looking for a pet? here are the animals waiting for a home!\n"
        reply += "Cat :cat2:\n"
        reply += "Dog :dog2:\n"
        reply += "Pigeon :bird:"
        await message.channel.send(reply)

# Købe Pet
    if contents == "!buy dog":
        await message.channel.send("Out of stock")
    elif contents == "!buy cat":
        await message.channel.send("Out of stock")

    elif contents == "!buy pigeon":
        await message.channel.send("Pigeon! i choose youuu!", file=discord.File('pigeon.jpg'))
        add_user_pet(user, "pigeon")
        await message.channel.send("remember to feed your pets every 24 hours")


# Game handling
    elif contents == "!kill pigeon":
        if user in pet_owners and "pigeon" in pet_owners[user]:
            if datetime.now() - timedelta(minutes=1) < user_pet_food[user]:
                await message.channel.send("Shot by a knife", file=discord.File('pigeon-dead.png'))
                pet_owners[user].remove("pigeon")
            else:
                await message.channel.send("your pet already died from hunger.")
                pet_owners[user] = []
        else:
            await message.channel.send("luckily you dont have a pigeon you monster")

# Game handling
    elif contents == "!play w pigeon":
        if user in pet_owners and "pigeon" in pet_owners[user]:
            if datetime.now() - timedelta(minutes=1) < user_pet_food[user]:
                await message.channel.send("KAKAAAAH!", file=discord.File('pigeon-play.jpg'))
            else:
                await message.channel.send("your pet died from hunger.")
                pet_owners[user] = []
        else:
            await message.channel.send("you dont have a pigeon to play with u lonely shit")

# Handling som skal udføres indenfor deadline.
    elif contents == "!feed pigeon":
        if user in pet_owners and "pigeon" in pet_owners[user]:
            if datetime.now() - timedelta(minutes=1) < user_pet_food[user]:
                await message.channel.send("Yum yum, dis some good shit!", file=discord.File('pigeon-eat.png'))
                add_user_pet(user, "pigeon")
            else:
                await message.channel.send("your pet died from hunger.") 
                pet_owners[user] = []
        else:
            await message.channel.send("you cant afford feeding a pigeon, let alone buy one")

token = get_token()
client.run(token)
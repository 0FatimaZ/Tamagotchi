import discord
import Maintenance
import pickle

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def save(client, message):
    contents = message.content

    with open('StateDict.p', 'wb') as fp:
        pickle.dump(Maintenance.users, fp, protocol=pickle.HIGHEST_PROTOCOL)
        return
        
import discord
import Maintenance
import pickle

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def quit(client, message):
    contents = message.content

    with open('state.p', 'wb') as fp:
        pickle.dump(Maintenance.state, fp, protocol=pickle.HIGHEST_PROTOCOL)
        pickle.dump(Maintenance.fridge, fp, protocol=pickle.HIGHEST_PROTOCOL)
        reply = "You've left your pet. Remeber to come back!"
        await message.channel.send(reply)
        return
        
import os
import discord
import random
from keep_alive import keep_alive
import league as lol
import misc as msc

client = discord.Client()

#readfile plans
p = open("plans.txt","r")
plans = p.read()

#readfile Readme
f = open("README.txt", "r")
readme = f.read()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):

    msg = message.content

    if message.author == client.user:
        return

#encourage
    if any(word in msg for word in lol.achievement):
        await message.channel.send(random.choice(lol.encourage))

#quote generator command
    if msg.startswith('$quote'):
        quote = msc.get_quote()
        await message.channel.send(quote)

#random commands
    if any(word in msg for word in msc.meow):
        await message.channel.send(random.choice(msc.meow))

    if msg.startswith("$commands"):
        await message.channel.send(readme)

    if msg.startswith("$plans"):
        await message.channel.send(plans)

keep_alive()
client.run(os.getenv('token'))
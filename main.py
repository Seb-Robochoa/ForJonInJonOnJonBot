import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('FOR JON \n IN JON \n ON JON \n' + '{0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('!fj'):
    await message.channel.send('FOR JON \nIN JON \nON JON \n')

client.run(os.getenv('TOKEN') )
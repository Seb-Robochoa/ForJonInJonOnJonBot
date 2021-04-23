import discord
import os
from keep_alive import keep_alive


client = discord.Client()

@client.event
async def on_ready():
  print('FOR JON \n IN JON \n ON JON \n' + '{0.user}'.format(client))

myid = '<@501886733353222164>'
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('!fj'):
    await message.channel.send('FOR JON \nIN JON \nON JON \nhttps://giphy.com/gifs/2uPi4A3mGSIyTZ8IVN')
  if message.content.startswith('!fj2'):
    await message.channel.send('FOR JON \nIN JON \nON JON \nhttps://giphy.com/gifs/mWTlyGwfNNgcIj9I2q')
  if message.content.startswith('!bruh'):
    await message.channel.send('<:bruh2:745666231570268180>')
  



    
keep_alive()
client.run(os.getenv('TOKEN') )
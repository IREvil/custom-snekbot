import discord
from discord.ext import commands
import asyncio
import re
import random
import requests
import json

bot = commands.Bot(command_prefix=['snek ', 'snekbot '], description='this is snekbot.')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name="snek.py"))

@bot.command()
async def hss(*, stuff_for_snek_to_say):
    """says stuff"""
    await bot.say(stuff_for_snek_to_say)

@bot.command()
async def pls():
    """try it"""
    await bot.say(':snake:')

@bot.command()
async def whomade():
    """who made snek?"""
    await bot.say('splitpixl made snekbot')

@bot.command()
async def info():
    """info about snekbot"""
    await bot.say('snekbot was coded in python with the library discord.py. hss.')

@bot.command()
async def invite():
    """snekbot invite link"""
    await bot.say('to add snekbot to your server click this: https://snek.splitpixl.xyz/')

@bot.command()
async def intensifies():
    """[SNEK INTENSIFIES]"""
    await bot.say('https://snek.splitpixl.xyz/intense.gif')

@bot.command()
async def hello():
    """hi"""
    await bot.say('hello yes this is snek.')

@bot.command()
async def noboop():
    """noboop snek"""
    await bot.say('https://snek.splitpixl.xyz/noboop.jpg')

@bot.command()
async def play(*, game_to_play):
    """snek likes playing game"""
    await bot.change_presence(game=discord.Game(name=game_to_play))

@bot.command()
async def sourcecode():
    """snek's source code"""
    await bot.say('https://github.com/SplitPixl/snekbot')

@bot.command()
async def snek():
    """sneksneksnek"""
    sneks = ['snek', 'hss', 'ssssnek', 'slither', 'snek sneek']
    await bot.say(random.choice(sneks))
    
client = discord.Client()
user = 'CLEVERBOT.IO API USER'
key = 'CLEVERBOT.IO API KEY'

@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | '+str(len(client.servers))+' servers')
    await client.change_presence(game=discord.Game(name='chat with me!'))

@client.event
async def on_message(message):
    if not message.author.bot and (message.server == None or client.user in message.mentions):
        await client.send_typing(message.channel)
        txt = message.content.replace(message.server.me.mention,'') if message.server else message.content
        r = json.loads(requests.post('https://cleverbot.io/1.0/ask', json={'user':user, 'key':key, 'nick':'frost', 'text':txt}).text)
        if r['status'] == 'success':
            await client.send_message(message.channel, r['response'] )

print('Starting...')
requests.post('https://cleverbot.io/1.0/create', json={'user':user, 'key':key, 'nick':'frost'})
client.run('DISCORD BOT TOKEN')


bot.run(open('./token','r').read().replace('\n', ''))

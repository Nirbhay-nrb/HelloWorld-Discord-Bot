import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get('TOKEN')
prefix = '>'

client = commands.Bot(command_prefix=prefix, activity = discord.Activity(type=discord.ActivityType.playing , name='with worlds'))

cogs = ['cogs.hello','cogs.react','cogs.reply','cogs.change_nickname']

for cog in cogs:
    client.load_extension(cog)

@client.event
async def on_ready():
    print('Bot switched on : {}'.format(client.user.name))
    print('Bot id : {}'.format(client.user.id))

client.run(token)
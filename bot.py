import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

# getting data from .env file
token = os.environ.get('TOKEN')
prefix = os.environ.get('PREFIX')

# initialising the bot
client = commands.Bot(command_prefix=prefix,help_command=None, activity = discord.Activity(type=discord.ActivityType.playing , name='with worlds'))

# list of all cogs
cogs = ['cogs.hello','cogs.react','cogs.reply','cogs.change_nickname','cogs.help','cogs.create']

# loading the cogs
for cog in cogs:
    client.load_extension(cog)

# what to do when the bot switches on
@client.event
async def on_ready():
    print('Bot switched on : {}'.format(client.user.name))
    print('Bot id : {}'.format(client.user.id))

client.run(token)
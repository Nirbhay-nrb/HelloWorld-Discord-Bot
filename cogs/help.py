import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

class Help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def help(self,ctx):
        prefix = os.environ.get('PREFIX')
        commands = {f'``{prefix}hello``' : 'Greets you',
                f'```{prefix}react```' : 'Add reactions to your message',
                f'```{prefix}reply```' : 'Replies to your message',
                f'```{prefix}nick```' : 'Changes the nickname of the user',
                f'```{prefix}help```' : 'Displays this message',
                }
        embed = discord.Embed(title='List of commands: ',description='These are the commands to use with this bot', color=0xFFF44F)
        count = 1
        for command in commands:
            embed.add_field(name=str(count)+'. '+command, value=commands[command],inline=False)
            count += 1
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Help(client))

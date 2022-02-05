import discord
from discord.ext import commands

class Nick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def nick(self,ctx,nick=None):
        try:
            if nick is None:
                await ctx.send('Please enter a nickname')
            else:
                await ctx.message.author.edit(nick=nick)
                await ctx.send('Changed NickName')
        except Exception as e:
            print(str(e))
            if str(e).split()[0] == '403':
                await ctx.send('Sorry i don\'t have the permissions')
            if str(e).split()[0] == '400':
                await ctx.send('Nickname can not be longer than 32 letters')

def setup(client):
    client.add_cog(Nick(client))

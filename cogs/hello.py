from discord.ext import commands

class Hello(commands.Cog):
    def __init__ (self , bot):
        self.bot = bot

    @commands.command()
    async def hello(self,ctx):
        await ctx.send('Hello {}'.format(ctx.message.author.mention))

def setup(client):
    client.add_cog(Hello(client))
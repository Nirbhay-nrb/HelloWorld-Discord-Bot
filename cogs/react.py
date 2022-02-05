from discord.ext import commands

class React(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
    
    @commands.command()
    async def react(self,ctx):
        await ctx.message.add_reaction('🇭')
        await ctx.message.add_reaction('🇮')
        await ctx.message.add_reaction('🤍')

def setup(client):
    client.add_cog(React(client))
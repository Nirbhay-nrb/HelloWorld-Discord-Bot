import discord
from discord.ext import commands
import asyncio

class Create(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def create(self, ctx):
        # menu of options in embed format
        embed = discord.Embed(title='Choose one from the following:', description='Input the corresponding number', color=0xFFF44F)
        embed.add_field(name='1. **Category**',value='Create a category',inline=False)
        embed.add_field(name='2. **Text Channel**',value='Create a text channel inside any category',inline=False)
        embed.add_field(name='3. **Voice Channel**',value='Create a voice channel inside any category',inline=False)
        await ctx.send(embed=embed)

        # getting a response from the user
        def check(reply_user):
            return reply_user.author == ctx.author and reply_user.channel == ctx.channel
        
        # timeout error
        try:
            msg = await self.bot.wait_for('message' , check=check , timeout=10) # a timeout for 10 seconds
        except asyncio.TimeoutError:
            await ctx.send('Sorry, you didn\'t reply in time!')
            return
        
        # Proceeding further according to user response
        await ctx.send('Your response {}'.format(msg.content))

def setup(client):
    client.add_cog(Create(client))
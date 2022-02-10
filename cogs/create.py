import discord
from discord.ext import commands
import asyncio

class Create(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def create(self, ctx):
        # list of categories on the server
        cats = ctx.message.guild.categories
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
        # creating a category
        if msg.content == '1':
            await ctx.send('Please pick a name!!')
            try:
                reply = await self.bot.wait_for('message', check=check, timeout=15)
                await ctx.guild.create_category(reply.content)
                await ctx.send('Category created!!')
            except asyncio.TimeoutError:
                await ctx.send('Sorry, you didn\'t reply in time!')
        # creating a text channel
        elif msg.content == '2':
            embed = discord.Embed(title='Choose one of the following categories:', description='Input the corresponding number', color=0xFFF44F)
            i = 1
            for cat in cats:
                embed.add_field(name=f'{i}. **{cat.name}**',value=f'{cat.id}',inline=False)
                i = i+1
            await ctx.send(embed = embed)
            try:
                replyCat = await self.bot.wait_for('message', check=check, timeout=10)
                if int(replyCat.content)-1 >= len(cats):
                    await ctx.send('Invalid input')
                    return
                await ctx.send('Please pick a name!!')
                try:
                    replyName = await self.bot.wait_for('message', check=check, timeout=15)
                    await ctx.guild.create_text_channel(f'{replyName.content}', category=cats[int(replyCat.content)-1])
                    await ctx.send('Text channel created!!')
                except asyncio.TimeoutError:
                    await ctx.send('Sorry, you didn\'t reply in time!')
            except asyncio.TimeoutError:
                await ctx.send('Sorry, you didn\'t reply in time!')
        # creating a voice channel
        elif msg.content == '3':
            embed = discord.Embed(title='Choose one of the following categories:', description='Input the corresponding number', color=0xFFF44F)
            i = 1
            for cat in cats:
                embed.add_field(name=f'{i}. **{cat.name}**',value=f'{cat.id}',inline=False)
                i = i+1
            await ctx.send(embed = embed)
            try:
                replyCat = await self.bot.wait_for('message', check=check, timeout=10)
                if int(replyCat.content)-1 >= len(cats):
                    await ctx.send('Invalid input')
                    return
                await ctx.send('Please pick a name!!')
                try:
                    replyName = await self.bot.wait_for('message', check=check, timeout=15)
                    await ctx.guild.create_voice_channel(f'{replyName.content}', category=cats[int(replyCat.content)-1])
                    await ctx.send('Voice channel created!!')
                except asyncio.TimeoutError:
                    await ctx.send('Sorry, you didn\'t reply in time!')
            except asyncio.TimeoutError:
                await ctx.send('Sorry, you didn\'t reply in time!')
        # no option 
        else:
            await ctx.send('Invalid input')

def setup(client):
    client.add_cog(Create(client))
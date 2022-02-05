from discord.ext import commands

class Reply(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
    
    @commands.command()
    async def reply(self,ctx):
        await ctx.message.reply('Replied to your message {}'.format(ctx.message.author.nick))

def setup(client):
    client.add_cog(Reply(client))
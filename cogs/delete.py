from discord.ext import commands

class Delete(commands.Cog):
    def __int__ (self , bot):
        self.bot = bot
    
    # listens to every message
    @commands.Cog.listener()
    async def on_message(self, message):
        curseWords = ['@everyone','@here']
        msg = message.content.lower()
        for word in curseWords:
            if word in msg:
                await message.delete()
                break

def setup(client):
    client.add_cog(Delete(client))
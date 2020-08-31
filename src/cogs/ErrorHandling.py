import discord

from discord.ext import commands

def setup(bot):
    bot.add_cog(ErrorHandling(bot))

class ErrorHandling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener('on_command_error')
    async def cmdError(self, ctx, exception):
            await ctx.message.channel.send(f"**ERROR**: Command doesn't exist or invalid parameters entered, please see `+help` for a list of valid commands")
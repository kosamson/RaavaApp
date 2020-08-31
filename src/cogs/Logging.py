import discord
import pytz

from discord.ext import commands
from datetime import datetime
from pytz import timezone
from pathlib import Path

def setup(bot):
    bot.add_cog(Logging(bot))

class Logging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener('on_message')
    async def everyoneLog(self, message):
        # Check if message mentions everyone
        if message.mention_everyone or '@here' in message.content:
            await self.logEveryoneMention(message)
    

    async def logEveryoneMention(self, message):
        # Get current date and time (datetime object) in PST timezone
        date = datetime.now(tz=timezone('US/Pacific'))

        # Truncate microsecond and timezone information
        date = date.replace(microsecond=0, tzinfo=None)

        # Create new server log folder if doesn't exist
        Path(f'../serverlogs/{message.guild.id}').mkdir(parents=True, exist_ok=True)

        # Store log message into respective server's @everyone log (evLog) file
        with open(f'../serverlogs/{message.guild.id}/everyoneLog.txt', 'a+') as everyoneLog:
            everyoneLog.write(f'{message.author} mentioned everyone on: {date} PST (UTC-7)\n')

    @commands.Cog.listener('on_member_remove')
    async def memberRemoveLog(self, member):
        # Get current date and time (datetime object) in PST timezone
        date = datetime.now(tz=timezone('US/Pacific'))

        # Truncate microsecond and timezone information
        date = date.replace(microsecond=0, tzinfo=None)

        # Create new server log folder if doesn't exist
        Path(f'../serverlogs/{member.guild.id}').mkdir(parents=True, exist_ok=True)
        
        with open(f'../serverlogs/{member.guild.id}/leaveLog.txt', 'a+') as leaveLog:
            leaveLog.write(f'{member.name}#{member.discriminator} removed from guild on {date} PST (UTC-7)')

    @commands.Cog.listener('on_message_delete')
    async def msgDeleteLog(self, message):
        # Get current date and time (datetime object) in PST timezone
        date = datetime.now(tz=timezone('US/Pacific'))

        # Truncate microsecond and timezone information
        date = date.replace(microsecond=0, tzinfo=None)

        # Retrieve and truncate message timestamp
        msgTimeStamp = message.created_at
        msgTimeStamp = msgTimeStamp.replace(microsecond=0, tzinfo=None)

        with open(f'../serverlogs/{message.guild.id}/msgDeleteLog.txt', 'a+') as msgDeleteLog:
            msgDeleteLog.write(f'Author: {message.author}, Message Sent: {msgTimeStamp} PST (UTC-7), Channel: {message.channel}, Deleted On: {date} PST (UTC-7)\n')

    @commands.Cog.listener('on_message_edit')
    async def msgEditLog(self, before, after):
        # Get current date and time (datetime object) in PST timezone
        date = datetime.now(tz=timezone('US/Pacific'))

        # Truncate microsecond and timezone information
        date = date.replace(microsecond=0, tzinfo=None)

        # Create new server log folder if doesn't exist
        Path(f'../serverlogs/{before.guild.id}').mkdir(parents=True, exist_ok=True)

        # Store log message into respective server's message edit log (msgEditLog) file
        with open(f'../serverlogs/{before.guild.id}/msgEditLog.txt', 'a+') as msgEditLog:
            msgEditLog.write(f'{before.author}\'s original message: "{before.content}" to "{after.content}" in {before.channel} was edited on: {date} PST (UTC-7)\n')
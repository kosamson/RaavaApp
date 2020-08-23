import discord
import pytz
import inspect
import random

from datetime import datetime
from pytz import timezone
from discord.ext import commands
from pathlib import Path

class RaavaApp(commands.Bot):
    def __init__(self):
        # Command Prefix for Raava is '+'; 
        # Ex: "+help" -- Runs the "help" command from Raava
        super().__init__(command_prefix='+', help_command=None)

        self.COMMAND_PREFIX = '+'

        # Add all commands to Bot
        members = inspect.getmembers(self)
        for name, member in members:
            if isinstance(member, commands.Command):
                if member.parent is None:
                    self.add_command(member)

    async def on_ready(self):  
        # Startup Checks
        print(f'{self.user} is now connected.')
        print('Connected to Guilds:')
        for guild in self.guilds:
            print(f'\tGuild Name: {guild.name}, Guild ID: {guild.id}')

        # Set Bot Status
        await self.change_presence(activity=discord.Streaming(name="+help", url='https://www.twitch.tv/RaavaApp'))

    async def on_message(self, message):
        if message.author == self.user:
            return

        # @everyone log check
        if message.mention_everyone or '@here' in message.content:
            await self.logEveryoneMention(message)

        # Check for cring inside message (if not a command)
        if not self.COMMAND_PREFIX in message.content:
            await self.on_cring(message)
        
        # Process message for command input
        await self.process_commands(message)

    async def on_member_remove(self, member):
        # Get current date and time (datetime object) in PST timezone
        date = datetime.now(tz=timezone('US/Pacific'))

        # Truncate microsecond and timezone information
        date = date.replace(microsecond=0, tzinfo=None)

        # Create new server log folder if doesn't exist
        Path(f'../serverlogs/{member.guild.id}').mkdir(parents=True, exist_ok=True)
        
        with open(f'../serverlogs/{member.guild.id}/leaveLog.txt', 'a+') as leaveLog:
            leaveLog.write(f'{member.name}#{member.discriminator} removed from guild on {date} PST (UTC-7)')

    async def on_command_error(self, ctx, exception):
        await ctx.message.channel.send(f"**ERROR**: Command doesn't exist or invalid parameters entered, please see `+help` for a list of valid commands")

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

            
    async def on_cring(self, message):
        if 'cring' in message.content.lower():
            await message.channel.send('CRING')


    """ BOT COMMANDS """

    @commands.command()
    async def cring(ctx):
        await ctx.message.channel.send('CRING')

    @commands.command()
    async def cringreact(ctx):
        # Get message prior to latest message (message before message that called command)
        prevMessage = (await ctx.message.channel.history(limit=3).flatten())[1]
        await ctx.message.delete()
        await prevMessage.add_reaction('🇨')
        await prevMessage.add_reaction('🇷')
        await prevMessage.add_reaction('🇮')
        await prevMessage.add_reaction('🇳')
        await prevMessage.add_reaction('🇬')

    @commands.command()
    async def shutdown(ctx):
        if ctx.message.author.guild_permissions.administrator:
                print(f'Bot shutting down by command from Guild: {ctx.message.guild.name} (Guild ID: {ctx.message.guild.id}) by user: {ctx.message.author}')
                await ctx.message.channel.send('Disconnecting client...')
                await ctx.bot.close()
            
        else:
            print(f'**ERROR**: Attempted shutdown of Bot from non-admin user: {ctx.message.author}')
            await ctx.message.channel.send('ERROR: Cannot shutdown Bot if not admin user')
    
    @commands.command()
    async def servericon(ctx):
        await ctx.message.channel.send(f'Retrieving {ctx.message.guild}\'s Server Icon:')
        await ctx.message.channel.send(ctx.message.guild.icon_url)

    @commands.command()
    async def help(ctx):
        commandList = []

        # Append all command names to commandList
        members = inspect.getmembers(ctx.bot)
        for name, member in members:
            if isinstance(member, commands.Command):
                if member.parent is None:
                    commandList.append('+' + str(member))

        # Send DM to command requester containing command info
        await ctx.message.author.send('**Raava Commands**:\n' + '\n'.join(commandList))

    @commands.command()
    async def getavatar(ctx, userid):
        targetUser = ctx.bot.get_user(int(userid))

        if (targetUser == None):
            await ctx.message.channel.send("**ERROR**: User ID does not match a user in this server, please try again. (Right-click the user and click 'Copy ID' to obtain their ID)")

        else:
            await ctx.message.channel.send(f'Retrieving `{targetUser.name}#{targetUser.discriminator}`\'s Icon:')
            await ctx.message.channel.send(targetUser.avatar_url)

    @commands.command()
    async def postcring(ctx):
        imgIdx = random.randint(1, 24)
        img = discord.File(f'../postcringimgs/{imgIdx}.jpg', filename=f'{imgIdx}.jpg')
        await ctx.message.channel.send(file=img)
        


import os
import discord
import pytz
import inspect

from datetime import datetime
from pytz import timezone
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
    
# Load personal token 
TOKEN = os.getenv('DISCORD_TOKEN')

class CringBotApp(commands.Bot):
    def __init__(self):
        # Command Prefix for CringBot is '+'; 
        # Ex: "+help" -- Runs the "help" command from CringBot
        super().__init__(command_prefix='+')

        # Add all commands to Bot
        members = inspect.getmembers(self)
        for name, member in members:
            if isinstance(member, commands.Command):
                if member.parent is None:
                    self.add_command(member)

    async def on_ready(self):  
        # Startup Checks
        print(f'{client.user} is now connected.')
        print('Connected to Guilds:')
        for guild in client.guilds:
            print(f'\tGuild Name: {guild.name}, Guild ID: {guild.id}')

    async def on_message(self, message):
        if message.author == self.user:
            return

        # @everyone log check
        if message.mention_everyone or '@here' in message.content:
            await self.logEveryoneMention(message)

        # Check for cring inside message
        else:
            await self.on_cring(message)
        
        # Process message for command input
        await self.process_commands(message)

    async def on_command_error(self, ctx, exception):
        await ctx.message.channel.send(f"**ERROR**: Invalid Command `{ctx.message.content}` entered, please see `+help` for a list of valid commands")

    async def logEveryoneMention(self, message):
        # Get current date and time (datetime object) in PST timezone
        date = datetime.now(tz=timezone('US/Pacific'))

        # Truncate microsecond and timezone information
        date = date.replace(microsecond=0, tzinfo=None)

        # Send log message to respective message's text channel
        await message.channel.send(f'**Mention Everyone Log:** `{message.author}` mentioned everyone on: `{date}` PST')
            
    async def on_cring(self, message):
        if 'cring' in message.content.lower():
            await message.channel.send('CRING')


    """ BOT COMMANDS """

    @commands.command()
    async def cring(ctx):
        # Get message prior to latest message (message before message that called command)
        prevMessage = (await ctx.message.channel.history(limit=3).flatten())[2]
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
                await client.close()
            
        else:
            print(f'ERROR: Attempted shutdown of Bot from non-admin user: {ctx.message.author}')
            await ctx.message.channel.send('ERROR: Cannot shutdown Bot if not admin user')
    
    @commands.command()
    async def servericon(ctx):
        await ctx.message.channel.send('Retrieving Server Icon:')
        await ctx.message.channel.send(ctx.message.guild.icon_url)


client = CringBotApp()
client.run(TOKEN)
import os
import discord
import pytz

from datetime import datetime
from pytz import timezone
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
    
# Load personal token 
TOKEN = os.getenv('DISCORD_TOKEN')

class CringBotApp(discord.Client):
    # Command Prefix for CringBot is '+'; 
    # Ex: "+help" -- Runs the "help" command from CringBot
    COMMAND_PREFIX = '+'

    async def on_ready(self):  
        # Startup Checks
        print(f'{client.user} is now connected.')
        print('Connected to Guilds:')
        for guild in client.guilds:
            print(f'\tGuild Name: {guild.name}, Guild ID: {guild.id}')

    async def on_message(self, message):
        if message.author == self.user:
            return

        # Check if message is a CringBot command
        if self.COMMAND_PREFIX in message.content and message.content[0] == self.COMMAND_PREFIX:
            await self.parseCommand(message)

        if message.mention_everyone:
            await self.logEveryoneMention(message)

        # Check for cring inside message
        else:
            await self.on_cring(message)

    async def logEveryoneMention(self, message):
        # Get current date and time (datetime object) in PST timezone
        date = datetime.now(tz=timezone('US/Pacific'))

        # Truncate microsecond and timezone information
        date = date.replace(microsecond=0, tzinfo=None)

        # Send log message to respective message's text channel
        await message.channel.send(f'**Mention Everyone Log:** `{message.author}` mentioned everyone on: `{date}` PST')

    async def parseCommand(self, message):
        commandName = (message.content.lower())[1:]
        if commandName == 'cring':
            # Get message prior to latest message (message before message that called command)
            prevMessage = (await message.channel.history(limit=2).flatten())[1]
            await message.delete()
            await prevMessage.add_reaction('🇨')
            await prevMessage.add_reaction('🇷')
            await prevMessage.add_reaction('🇮')
            await prevMessage.add_reaction('🇳')
            await prevMessage.add_reaction('🇬')

        elif commandName == 'shutdown':
            if message.author.guild_permissions.administrator:
                print(f'Bot shutting down by command from Guild: {message.guild.name} (Guild ID: {message.guild.id}) by user: {message.author}')
                await message.channel.send('Disconnecting client...')
                await self.close()
            
            else:
                print(f'ERROR: Attempted shutdown of Bot from non-admin user: {message.author}')
                await message.channel.send('ERROR: Cannot shutdown Bot if not admin user')

        elif commandName == 'servericon':
            await message.channel.send('Retrieving Server Icon:')
            await message.channel.send(message.guild.icon_url)

        else:
            print('ERROR: Invalid command entered')
            await message.channel.send('ERROR: Invalid command entered')
            
    async def on_cring(self, message):
        if 'cring' in message.content.lower():
            await message.channel.send('CRING')


client = CringBotApp()
client.run(TOKEN)
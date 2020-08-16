import os
import discord
import pytz

from datetime import datetime
from pytz import timezone
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
    
# Personal token and guild
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

class CringBotApp(discord.Client):
    # Command Prefix for CringBot is '+'; 
    # Ex: "+help" -- Runs the "help" command from CringBot
    COMMAND_PREFIX = '+'

    async def on_ready(self):
        for guild in client.guilds:
            if guild.name == GUILD:
                break
        
        # Startup Checks
        print(f'{client.user} is now connected.')
        print(f'Connected to Guild: {guild.name}, Guild ID: {guild.id}')

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
            print('Disconnecting client...')
            await message.channel.send('Disconnecting client...')
            await self.close()
        
        else:
            print('ERROR: Invalid command entered')
            await message.channel.send('ERROR: Invalid command entered')
            
    async def on_cring(self, message):
        if 'cring' in message.content.lower():
            await message.channel.send('CRING')


client = CringBotApp()
client.run(TOKEN)
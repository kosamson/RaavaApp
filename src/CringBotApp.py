import os
import discord
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

        if (self.COMMAND_PREFIX in message.content):
            await self.parseCommand(message)

        # Check for cring
        else:
            await self.on_cring(message)

    async def parseCommand(self, message):
        if (message.content.lower())[1:] == 'cring':
            await message.add_reaction('🇨')
            await message.add_reaction('🇷')
            await message.add_reaction('🇮')
            await message.add_reaction('🇳')
            await message.add_reaction('🇬')

    
    async def on_cring(self, message):
        if 'cring' in message.content.lower():
            await message.channel.send('CRING')


client = CringBotApp()
client.run(TOKEN)
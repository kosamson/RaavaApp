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

        if (message.content[0] == self.COMMAND_PREFIX):
            await self.parseCommand(message)

        # Check for cring
        else:
            await self.on_cring(message)

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

    @commands.command()
    async def cring(self, ctx):
        await message.add_reaction('🇨')
        await message.add_reaction('🇷')
        await message.add_reaction('🇮')
        await message.add_reaction('🇳')
        await message.add_reaction('🇬')


client = CringBotApp()
client.run(TOKEN)
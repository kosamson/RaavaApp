import discord
import os

from discord.ext import commands

class RaavaApp(commands.Bot):
    def __init__(self):
        # Command Prefix for Raava is '+'; 
        # Ex: "+help" -- Runs the "help" command from Raava
        super().__init__(command_prefix='+', help_command=None)

        # Load Cogs
        for fileName in os.listdir('cogs'):
            if (fileName.endswith('.py')):
                # Truncate '.py' from file name
                cog = fileName[:len(fileName) - 3]

                self.load_extension(f'cogs.{cog}')

    async def on_ready(self):  
        # Startup Checks
        print(f'{self.user} is now connected.')
        print('Connected to Guilds:')
        for guild in self.guilds:
            print(f'\tGuild Name: {guild.name}, Guild ID: {guild.id}')

        # Set Bot Status
        await self.change_presence(activity=discord.Streaming(name='+help', url='https://www.twitch.tv/RaavaApp'))

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        # Process message for command input
        await self.process_commands(message)
        


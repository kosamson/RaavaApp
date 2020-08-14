import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

# Command Prefix for CringBot is '+'; 
# Ex: "+help" -- Runs the "help" command from CringBot
COMMAND_PREFIX = commands.Bot(command_prefix = '+')

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    
    # Startup Checks
    print(f'{client.user} is now connected.')
    print(f'Connected to Guild: {guild.name}, Guild ID: {guild.id}')
    
    mainChannelID = int(input('Which text channel would you like this bot to be active? (Enter Channel ID): '))
    mainChannel = client.get_channel(mainChannelID)
    await mainChannel.send('TEST MESSAGE')
    print('Message successfully sent.')


# Run bot using token
client.run(TOKEN)




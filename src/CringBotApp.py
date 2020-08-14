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
    
    print(f'CRING!!! {client.user} IS HERE!!!')
    print(f'{guild.name}, id: {guild.id}')
    

# Run bot using token
client.run(TOKEN)




import os
import discord

from RaavaApp import RaavaApp
    
# Load personal token 
TOKEN = os.getenv('DISCORD_TOKEN')

# Initialize Discord client connection for CringBot
client = RaavaApp()

client.run(TOKEN)
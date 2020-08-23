import os
import discord

from dotenv import load_dotenv
from RaavaApp import RaavaApp

load_dotenv()
    
# Load personal token 
TOKEN = os.getenv('DISCORD_TOKEN')

# Initialize Discord client connection for CringBot
client = RaavaApp()

client.run(TOKEN)
import os
import discord

from dotenv import load_dotenv
from CringBotApp import CringBotApp

load_dotenv()
    
# Load personal token 
TOKEN = os.getenv('DISCORD_TOKEN')

# Initialize Discord client connection for CringBot
client = CringBotApp()
client.run(TOKEN)
import os
import CringBotApp
import discord

from dotenv import load_dotenv

load_dotenv()
    
# Load personal token 
TOKEN = os.getenv('DISCORD_TOKEN')

# Initialize Discord client connection for CringBot
client = CringBotApp.CringBotApp()
client.run(TOKEN)
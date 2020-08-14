import os
import discord
from discord.ext import commands

client = discord.Client()

# Command Prefix for CringBot is '+'; 
# Ex: "+help" -- Runs the "help" command from CringBot
COMMAND_PREFIX = commands.Bot(command_prefix = '+')

class CringBotClient(discord.Client):
    @client.event
    async def on_ready(self):
        print('CRING')

# Run bot using token
client.run("NzQzNjUxMzYyMzA2NTIzMTc2.XzXxTQ.grdv0_CyfinxNUmQEFLsljtM2I8")




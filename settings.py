import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# client = discord.Client(intents=intents )
bot =  commands.Bot(command_prefix=';', intents=intents)

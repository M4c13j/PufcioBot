import os
from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("DISCORD_TOKEN")

intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=';', intents=intents)


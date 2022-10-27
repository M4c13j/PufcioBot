import os
from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv
import logging

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename='dicord.log', encoding='utf-8', mode='w')
intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=';', intents=intents)


PUSZEK_NAMES = ["pufcio","pufć","puchol","pucholek","puszek","pusio"]

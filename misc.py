from settings import bot

def get_guild_names():
    return [guild.name for guild in bot.guilds]
from random import choice
from settings import *
from events import *
from comms import *


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)
    
bot.run(token)
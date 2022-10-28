from datetime import timedelta
from settings import PUSZEK_NAMES, bot
from random import choice
from random import randrange
import asyncio
@bot.event
async def on_ready():
    print(f"Logged in as a bot {bot.user}")
    # for guild in bot.guilds:
    #     for channel in guild.text_channels :
    #         if str(channel) == "general" :
    #             await channel.send('Bot Activated..')
    #             await channel.send(file=discord.File('giphy.png'))
    #     print('Active in {}\n Member Count : {}'.format(guild.name,guild.member_count))
    while True:
        delta_time = randrange(180,1080)
        print(f"Waiting {delta_time} seconds ...")
        await asyncio.sleep( delta_time )

        msg = await bot.get_channel(choice([
            786216614679937027,
            980156776882245632,
            806621316681170974,
            819333114941145088,
            842677852083978265,
            808736480951926854
        ])).send("<@649228867399319554> cześć")
        print(f"Sent to: {msg.channel}.")
        await asyncio.sleep(1)
        await msg.delete()
        print("DELETING MESSAGE")


@bot.event
async def on_message( message ):
    # print( message.content )
    # print( message.author )
    # print( message.channel )
    # print( message.id )
    # print( message.guild )
    if message.author == bot.user:
        return
    print(f"Message from  {message.author}: {message.content} | {message.author.id}" )

    # pluskwa na uytkownika pewnego...
    uidr= [649228867399319554, 344798686003593236]
    if message.author.id == uidr[0]:
        nickname = message.author
        if randrange(0,100) == 69:
            await message.channel.send( choice(['Jejo','Kako','Bajo\n\n\nJajo','Jajo','cześć',f"pozdram cieplutko {nickname}"]))
        if randrange(0,100)%10 == 5:
            await message.add_reaction("\N{EGG}")
    #pluskwa na mnie
    if message.author.id == uidr[1]:
        nickname = message.author
        if randrange(0,10) % 3 == 1:
            await message.add_reaction( bot.get_emoji(864435513464061953) )
    # :mac:864435513464061953
    if randrange(1,100) % 15 == 4:
        await message.channel.send('rel')
    if 'robert kubica' in message.content.lower():
        await message.channel.send('DRAJWER BŁYSKAWICA! 🏎️ 🏁 ')
    if any(el in message.content for el in PUSZEK_NAMES):
        await message.channel.send('słodziak')
    if 'nig' in message.content.lower():
        await message.channel.send('GER')
    if message.content.lower() == 'ping':
        await message.channel.send( choice(['pong','srong','gong','pytong']) )
    if 'debil' in message.content.lower() and any(el in message.content.lower() for el in PUSZEK_NAMES):
        # await message.author.timeout( timedelta(seconds=10), reason="Bo tak można." )
        await message.channel.send("Bana chcesz?")

    await bot.process_commands(message) # gowno, by komendy dzialaly 

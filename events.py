from settings import bot
from random import choice
@bot.event
async def on_ready():
    print(f"Logged in as a bot {bot.user}")

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
    if message.author.id == 649228867399319554:
        await message.channel.send( choice(['Jejo','Kako','Bajo\n\n\nJajo','Jajo','cześć','']))

    if 'robert kubica' in message.content.lower():
        await message.channel.send('DRAJWER BŁYSKAWICA!')
    if 'pufcio' in message.content.lower():
        await message.channel.send('słodziak')
    if 'nig' in message.content.lower():
        await message.channel.send('GER')
    if message.content == 'ping':
        await message.channel.send( choice(['pong','srong','gong','pytong']) )
    if 'debil' in message.content:
        await message.channel.send("Bana chcesz???")

    await bot.process_commands(message) # gowno, by komendy dzialaly 
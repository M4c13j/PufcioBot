from settings import bot
import discord
import os
from ytdlms import * 
import requests

@bot.command()
async def test(ctx, *args):
    ctx.message.delete()
    arguments = ', '.join(args)
    await ctx.send(f'{len(args)} arguments: {arguments}')

@bot.command(name='daj', help="Nakarm głodnego króliczka")
async def daj(ctx, type, amount ):
    await ctx.send(f"{ctx.author.nick} dał Pufciowi Króliczkowi {amount} {type}-ów!")


@bot.command(help = "Prints details of Server")
async def where_am_i(ctx):
    owner=str(ctx.guild.owner)
    guild_id = str(ctx.guild.id)
    memberCount = str(ctx.guild.member_count)
    desc=ctx.guild.description
    
    embed = discord.Embed(
        title=ctx.guild.name + " Server Information",
        description=desc,
        color=discord.Color.blue()
    )
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=guild_id, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)

    members=[]
    async for member in ctx.guild.fetch_members(limit=150) :
        await ctx.send('Name : {}\t Status : {}\n Joined at {}'.format(member.display_name,str(member.status),str(member.joined_at)))



@bot.command(help="dolacz do kanalu glosowego")
async def donogi(ctx):
    channel = ctx.message.author.voice.channel
    if ctx.voice_client:
        if ctx.voice_client.channel == channel:
            await ctx.send(f"Już jestem na kanale **{channel}**!")
            await ctx.message.delete()
            return
    if not ctx.message.author.voice:
        await ctx.send(f"Nie jesteś na kanale głosowym lol.")
        await ctx.message.delete()
        return

    if ctx.voice_client:
        await ctx.voice_client.move_to(channel)
    else:
        await channel.connect()
    await ctx.send(f"Kicam do ciebie **{ctx.message.author}** na kanał **{channel}**")
    await ctx.message.delete()

@bot.command(help="opusc kanal glowy i nie wracaj")
async def spadaj(ctx):
    vc = ctx.voice_client
    if vc:
        await vc.disconnect()
        await ctx.send(f"{ctx.message.author} sam **spadaj**.")
    else:
        await ctx.send(f"**{ctx.message.author}** ja nie jestem przy głosie teraz.")
    await ctx.message.delete()

@bot.command(help="graj muzyke z linku")
async def graj(ctx,url):
    # removing previously downloadded files
    for f in os.listdir(os.getcwd()):
        if f.endswith(".webm") or f.endswith(".part") or f.endswith(".mp3") or f.endswith(".m4a"):
            os.remove( os.path.join(os.getcwd(), f) )

    await donogi(ctx)
    try :
        author = ctx.message.author
        voice_channel = ctx.voice_client

        async with ctx.typing():
            # arg = url
            # with youtube_dl.YoutubeDL({'format': 'bestaudio', 'noplaylist':'True'}) as ydl:
            #     try: requests.get(arg)
            #     except: info = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
            #     else: info = ydl.extract_info(arg, download=False)
            # source = (info, info['formats'][0]['url'])
            # filename = url
            # FFMPEG_OPTS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            # voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=source, **FFMPEG_OPTS), after=lambda e: print('Everything done nice ziom', e))
            filename = await YTDLSource.from_url(url, loop=bot.loop)
            print(filename)
            voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=filename))
        filename.replace("_"," ")
        embed = discord.Embed(title="Teraz leci:", description=f"[**{filename}**]({url})\nOd **{ctx.author}**", color=discord.Color.green())
        await ctx.send(embed=embed)
        await ctx.message.delete()
    except:
        await ctx.send("Pojawił się **błąd**, ale nie wiem jaki :(")

@bot.command(help='pomijam piosenke')
async def pomin(ctx):
    vc = ctx.message.guild.voice_client
    if vc.is_playing():
        await vc.stop()
        await ctx.send("Granie zatrzymane.")
    else:
        await ctx.send("Nie zatrzymam nic, bo nic nie gram **NIG**.")
   

# https://medium.com/pythonland/build-a-discord-bot-in-python-that-plays-music-and-send-gifs-856385e605a1
# https://discordpy.readthedocs.io/en/stable/api.html?highlight=message#
# https://stackoverflow.com/questions/63647546/how-would-i-stream-audio-from-pytube-to-ffmpeg-and-discord-py-without-downloadin
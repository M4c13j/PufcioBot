from settings import bot
import discord
from ytdlms import *

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



@bot.command()
async def donogi(ctx):
    if not ctx.message.author.voice:
        await ctx.send(f"Nie jesteś na kanale głosowym lol.")
    else:
        channel = ctx.message.author.voice.channel
        await channel.connect()

@bot.command()
async def spadaj(ctx):
    vc = ctx.message.guild.voice_client
    if vc.is_connected():
        await vc.dissconnect()
        await ctx.send(f"{ctx.author.nick} sam spadaj.")
    else:
        await ctx.send(f"{ctx.author.nick} ja nie jestem przy głosie teraz.")

@bot.command()
async def play(ctx,url):
    try :
        server = ctx.message.guild
        voice_channel = server.voice_client

        async with ctx.typing():
            filename = await YTDLSource.from_url(url, loop=bot.loop)
            voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
        await ctx.send('**Now playing:** {}'.format(filename))
    except:
        await ctx.send("The bot is not connected to a voice channel.")
# https://medium.com/pythonland/build-a-discord-bot-in-python-that-plays-music-and-send-gifs-856385e605a1
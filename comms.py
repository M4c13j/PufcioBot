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



@bot.command(help="dolacz do kanalu glosowego")
async def donogi(ctx):
    if not ctx.message.author.voice:
        await ctx.send(f"Nie jesteś na kanale głosowym lol.")
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()
    await ctx.send(f"Kicam do ciebie **{ctx.message.author}** na kanał **{channel}**")

@bot.command(help="opusc kanal glowy i nie wracaj")
async def spadaj(ctx):
    vc = ctx.message.guild.voice_client
    if vc.is_connected():
        await vc.dissconnect()
        await ctx.send(f"{ctx.author.nick} sam spadaj.")
    else:
        await ctx.send(f"**{ctx.author.nick}** ja nie jestem przy głosie teraz.")

@bot.command(help="graj muzyke z linku")
async def graj(ctx,url):
    await donogi(ctx)
    try :
        server = ctx.message.guild
        voice_channel = server.voice_client

        async with ctx.typing():
            filename = await YTDLSource.from_url(url, loop=bot.loop)
            print(filename)
            voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=filename))
        filename.replace("_"," ")
        await ctx.send(f'**Now playing:** {filename}.\n From url:** {url}**')
        await ctx.message.delete()
    except:
        await ctx.send("Nie ma mnie na żadnym kanale **sneed**.")

@bot.command()
async def przestan(ctx):
    vc = ctx.message.guild.voice_client
    if vc.is_playing():
        await vc.stop()
        await ctx.send("**STOP** granie muzyki")
    else:
        await ctx.send("Jak mam przestać grać, jak **milczę**!")
        
@bot.command(help='pomijam piosenke')
async def pomin(ctx):
    vc = ctx.message.guild.voice_client
    if vc.is_playing():
        await vc.stop()
        await ctx.send("Granie zatrzymane.")
    else:
        await ctx.send("Nie zatrzymam nic, bo nic nie gram **NIG**.")
@bot.command()
async def skip(ctx):
    vc = ctx.message.guild.voice_client

# https://medium.com/pythonland/build-a-discord-bot-in-python-that-plays-music-and-send-gifs-856385e605a1
import logging

import pafy
#### logging [recommended]####
logging.basicConfig(level= logging.INFO)
########

import discord
from discord.ext import commands
import youtube_dl
import os
import random


client = commands.Bot(command_prefix='*')

@client.event
async def on_ready():
    print('Bot online')



@client.command(name= 'join', aliases= ['connect'])
async def join(ctx):
  #await ctx.invoke(join)
    vc = ctx.author.voice
    voice = ctx.voice_client
    if not vc:
        await ctx.send('You aren\'t connected to any voice channel.')
    else:
        if not voice:
                await vc.channel.connect()
                await ctx.send(f'Bot connected to {vc.channel.mention}')
        else:
                if voice.is_playing():
                    await ctx.send(f'Bot already connected to {voice.channel.mention} and playing music!!')
                elif voice.channel != vc.channel:
                    await voice.move_to(vc.channel)
                    await ctx.send(f'Bot moved to {vc.channel.mention}')
                else:
                    pass
    
@client.command(name= 'play', aliases= ['p','','sing'])
async def play(ctx, *, url= None):
    await ctx.invoke(join)
    if url:
        video =  pafy.new(url)
        audio =  video.audiostreams[0]
        if os.path.exists("song.mp3"):
          os.remove("song.mp3")

        audio.download("song.mp3")
        source = discord.FFmpegPCMAudio("song.mp3")
        await ctx.send(f'Now Playing: **{video.title}**')
        ctx.voice_client.play(source)



@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

#command 1
@client.command()
async def hi(ctx):
	await ctx.send(
	    "Hey! How are you? I am Alu. To know more about me type '*Alu' ")


#command 2
@client.command()
async def Alu(ctx):
	await ctx.send(
	    "Hi!! My name is Alu. Alu means Potato. But I am not a potato . I am a bot. Bappy is my creator. Mainly my work is to help you to mention anyone. If you want to mention anyone please write '*call' then mention him or her. I will send a massage to his or her DM with your name. you can also mention the channel where you are calling him or her. Also I will play music for you with so many features. Type ' *help' to know about all commands.  "
	)


#command 3
@client.command()
async def alu(ctx):
	await ctx.send("Hi!! My name is Alu. Alu means Potato. But I am not a potato . I am a bot. Bappy is my creator. Mainly my work is to help you to mention anyone. If you want to mention anyone please write '*call' then mention him or her. I will send a massage to his or her DM with your name. you can also mention the channel where you are calling him or her. Also I will play music for you with so many features. Type ' *help' to know about all commands. ")


#command 4
@client.command()
async def spin(ctx):
	await ctx.send(
	    random.choice(
	        ('Bill Gates will offered you to work at Microsoft ',
	         'Elon Musk will hack your computer ',
	         'Listen this song- https://youtu.be/jsXrqTXovIA',
	         'Go and watch 3 idiots movie',
	         'listen this and work hard- https://youtu.be/_4kHxtiuML0',
	         'Go and play Football ', 'Elon Musk will kill you ',
	         'listen this music and sleep-  https://youtu.be/UfcAVejslrU',
	         'You should play cricket now.')))



#command 5
@client.command()
async def me(ctx):
	await ctx.send(
	    random.choice(
	        ('you are lazy', 'you are brilliant', 'you are active',
	         'you are bad', 'you are little baby', 'you are crying now',
	         'you are in cox bazar now', 'you are a good boy')))
	
	
@client.command(name= 'bappy', aliases= ['Bappy'])
async def bappy(ctx):
	await ctx.send(
	    random.choice(
	        ('A lazy boy', 'Dont tell to me his name', 'A donkey who can not do anything',
	         'He is trying to delete me. Please help', 'He said to me that he will make another bot and delete me. Please help.', 'If you can, please ban him from this server. Please',
	         'Nowadays he is ignoring me. Why!!', 'He is not a good boy')))
	


#https://youtu.be/5K-J2KOmDTw
@client.command(name= 'sing', aliases= ['s'])
async def sing(ctx, *, url= https://youtu.be/5K-J2KOmDTw):
    await ctx.invoke(join)
    if url:
        video =  pafy.new(url)
        audio =  video.audiostreams[0]
        if os.path.exists("song.mp3"):
          os.remove("song.mp3")

        audio.download("song.mp3")
        source = discord.FFmpegPCMAudio("song.mp3")
        await ctx.send(f'Now Playing: **{video.title}**')
        ctx.voice_client.play(source)






@client.command()
async def call(ctx, user: discord.Member, channel: discord.TextChannel = None):
	if channel:
		await user.send(
		    f"{ctx.author.name} is calling you {user.mention} in {channel.mention} channel"
		)
	else:
		await user.send(
		    f"{ctx.author.name} is calling you {user.mention} in {ctx.channel.mention} channel"
		)

token = os.getenv("TOKEN")

client.run(token)
#client.run('ODYwNzM4Njc2ODQ1MDUxOTM0.YN_nXA.T__5V7i4PPt32kapqQI6m1h962k')

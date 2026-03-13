import discord; from discord.ext import commands;
from UserManagement import ModerationActions

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.guilds = True
intents.presences = True

client = commands.Bot(command_prefix='!', intents=intents);

@client.command(name='welcome_channel', description='Sets the welcome channel for the server')
async def welcome_channel(ctx):
    await ctx.send(f'Welcome channel set to {ctx.channel.mention}!')

@client.command(name='ban', description='Bans a user from the server')
async def ban(ctx):
    await ModerationActions.onBan(message=ctx.message)

@client.command(name='unban', description='Unbans a user from the server')
async def unban(ctx):
    await ModerationActions.onUnban(message=ctx.message)

@client.command(name='kick', description='Kicks a user from the server')
async def kick(ctx):
    await ModerationActions.onKick(message=ctx.message)

@client.command(name='mute', description='Mutes a user in the server')
async def mute(ctx):
    await ModerationActions.onMute(message=ctx.message)

@client.command(name='unmute', description='Unmutes a user in the server')
async def unmute(ctx):
    await ModerationActions.onUnmute(message=ctx.message)

@client.command(name='benice', description='Tells the user to be nice')
async def benice(ctx):
    if (ctx.message.author.guild_permissions.administrator): 
        await ctx.send(f'<@{ctx.message.mentions[0].id}>, please be nice!')#
    else:
        await ctx.send(f'<@{ctx.message.author.id}> shut up non')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Committing 50 different murders"))

@client.event
async def on_member_join(member):
    channel = client.get_channel(1482108486228774973)
    if channel:
        await channel.send(f'Welcome to the server, <@{member.id}>!')

client.run('YOUR_BOT_TOKEN_HERE')
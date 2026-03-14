import os

import discord; from discord.ext import commands;
from ServerManagement import RoleManager, WelcomeUsers
from UserManagement import ModerationActions;
from DataManager import Connection;
from MessageManagement import MessageDeletion;
from DataManager import PreferenceStore;

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.guilds = True
intents.presences = True

client = commands.Bot(command_prefix='!', intents=intents);

databaseConnection = Connection.DatabaseConnection();
databaseConnection.connect();



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
    if (ctx.message.mentions == []):
        await ctx.send(f'<@{ctx.message.author.id}>, be nice to yourself ig')
    elif (ctx.message.mentions[0].guild_permissions.administrator): 
        await ctx.send(f'<@{ctx.message.author.id}>, you cannot tell an administrator to be nice!')
    elif (ctx.message.author.guild_permissions.administrator):
        await ctx.send(f'<@{ctx.message.mentions[0].id}>, please be nice!')
    else:
        await ctx.send(f'<@{ctx.message.author.id}> shut up non')

@client.command(name='purge', description='Deletes a specified number of messages from the channel')
async def purge(ctx):
    await MessageDeletion.purge(message=ctx.message)

@client.command(name='addrole', description='Adds a specified role to a mentioned user')
async def addrole(ctx):
    await RoleManager.addRole(message=ctx.message)

@client.command(name='commandlist', description='Sends a list of all available commands')
async def commandlist(ctx):
    if (ctx.message.author.guild_permissions.administrator):    
        commandNames = [command.name for command in client.commands]
        commandDescriptions = [command.description for command in client.commands]
        commands = [f'- {name}: {description}\n' for name, description in zip(commandNames, commandDescriptions)]
        await ctx.send(f'Available commands:\n{"".join(commands)}')
    else:
        await ctx.send(f'<@{ctx.message.author.id}> You do not have permission to use this command!')

@client.command(name='setwelcomechannel', description='Sets a custom welcome channel for the server')
async def setwelcomechannel(ctx):
    await WelcomeUsers.setWelcomeChannel(ctx.message, databaseConnection)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Committing 50 different murders"))



@client.event
async def on_member_join(member):
    channel = client.get_channel(1482108486228774973)
    if channel:
        welcome_message = PreferenceStore.get_custom_welcome_message(member.guild.id, databaseConnection.connection)
        await channel.send(f'{welcome_message}, <@{member.id}>!')


client.run(os.getenv('BOT_TOKEN'))
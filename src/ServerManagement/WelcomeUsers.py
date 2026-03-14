import discord
from DataManager import PreferenceStore

async def setWelcomeChannel(message, databaseConnection):
    if message.author.guild_permissions.administrator:
        channel = message.channel
        PreferenceStore.set_welcome_channel(message.guild.id, channel.id, databaseConnection.connection)
        await message.channel.send(f'Welcome channel set to {channel.mention}!')
    else:
        await message.channel.send(f'<@{message.author.id}>, you do not have permission to set the welcome channel.')
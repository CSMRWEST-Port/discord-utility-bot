from DataManager.GuildPreferences import PreferenceStore
import ServerManagement.PermissionsManager as PermissionsManager
from DataManager import Connection

async def setWelcomeChannel(message, databaseConnection: Connection.DatabaseConnection):
    if PermissionsManager.guild_management_check(message):
        channel = int(message.content.split(" ")[1][2:-1]) if (len(message.content.split(" ")) > 1 and message.content.split(" ")[1].startswith('<#')) else message.channel.id
        PreferenceStore.set_welcome_channel(message.guild.id, channel, databaseConnection.connection)
        await message.channel.send(f'Welcome channel set to <#{channel}>!')
    else:
        await message.channel.send(f'<@{message.author.id}>, you do not have permission to set the welcome channel.')

async def setCustomWelcomeMessage(message, databaseConnection: Connection.DatabaseConnection):
    if PermissionsManager.guild_management_check(message):
        content = " ".join(message.content.split(" ")[1:])
        PreferenceStore.set_custom_welcome_message(message.guild.id, content, databaseConnection.connection)
        await message.channel.send(f'Custom welcome message set to "{content}"!')
    else:
        await message.channel.send(f'<@{message.author.id}>, you do not have permission to set the custom welcome message.')

async def setGoodbyeChannel(message, databaseConnection: Connection.DatabaseConnection):
    if PermissionsManager.guild_management_check(message):
        channel = int(message.content.split(" ")[1][2:-1]) if (len(message.content.split(" ")) > 1 and message.content.split(" ").startswith('<#')) else message.channel.id
        PreferenceStore.set_goodbye_channel(message.guild.id, channel, databaseConnection.connection)
        await message.channel.send(f'Goodbye channel set to {channel.mention}!')
    else:
        await message.channel.send(f'<@{message.author.id}>, you do not have permission to set the goodbye channel.')

async def setCustomGoodbyeMessage(message, databaseConnection: Connection.DatabaseConnection):
    if PermissionsManager.guild_management_check(message):
        content = " ".join(message.content.split(" ")[1:])
        PreferenceStore.set_custom_goodbye_message(message.guild.id, content, databaseConnection.connection)
        await message.channel.send(f'Custom goodbye message set to "{content}"!')
    else:
        await message.channel.send(f'<@{message.author.id}>, you do not have permission to set the custom goodbye message.')
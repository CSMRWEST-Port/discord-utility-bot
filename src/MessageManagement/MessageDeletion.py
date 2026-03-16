import discord, time;

from ServerManagement import PermissionChecks


async def purge(message: discord.Message):
    if (PermissionChecks.message_deletion_check(message)):
        try:
            amount = int(message.content.split(" ")[1])
        except (IndexError, ValueError):
            await message.channel.send(f'<@{message.author.id}>, you need to specify the number of messages to delete.')
            return
        await message.channel.purge(limit=amount + 1)
        await message.channel.send(f'{amount} messages have been deleted by {message.author}.', delete_after=5)
    else:
        await message.channel.send(f'<@{message.author.id}>, you do not have permission to delete messages.')

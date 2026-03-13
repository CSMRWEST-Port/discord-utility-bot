import discord, time;

async def purge(message):
    if (message.author.guild_permissions.administrator):
        try:
            amount = int(message.content.split(" ")[1])
        except (IndexError, ValueError):
            await message.channel.send(f'<@{message.author.id}>, you need to specify the number of messages to delete.')
            return
        await message.channel.purge(limit=amount + 1)
        await message.channel.send(f'{amount} messages have been deleted by {message.author}.')
        time.sleep(5)
        await message.channel.purge(limit=1)
    else:
        await message.channel.send(f'<@{message.author.id}>, you do not have permission to delete messages.')

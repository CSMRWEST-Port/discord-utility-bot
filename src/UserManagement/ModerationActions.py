import discord
import re
import datetime

async def onBan(self, message):
    if (message.mentions == []):
        await message.channel.send(f'<@{message.author.id}>, you need to mention a user to ban.')
        return
    guild = message.guild
    content = " ".join(message.content.split(" ")[2:])
    if message.author.guild_permissions.ban_members:
        await guild.ban(message.mentions[0], reason=content)
        await message.channel.send(f'{message.mentions[0]} has been banned by {message.author} for reason {content}.')
    else:
        await message.channel.send(f'<@{message.author.id}>, you do not have permission to ban members.')

async def onUnban(self, message):
    if (message.content.split(" ")[1] == ""):
        await message.channel.send(f'<@{message.author.id}>, you need to mention a user to unban.')
        return
    guild = message.guild
    content = message.content.split(" ")[1]
    if (message.author.guild_permissions.ban_members):
        await guild.unban(discord.Object(id=int(content)))

async def onKick(self, message):
    if (message.mentions == []):
        await message.channel.send(f'<@{message.author.id}>, you need to mention a user to kick.')
        return
    guild = message.guild
    content = " ".join(message.content.split(" ")[2:])
    if message.author.guild_permissions.kick_members:
        await guild.kick(message.mentions[0], reason=content)
        await message.channel.send(f'{message.mentions[0]} has been kicked by {message.author} for reason {content}.')
    else:
        await message.channel.send(f'<@{message.author.id}>, you do not have permission to kick members.')

async def onMute(self, message):
    if (message.mentions == []):
        await message.channel.send(f'<@{message.author.id}>, you need to mention a user to mute.')
        return
    guild = message.guild
    givenTime = message.content.split(" ")[2]
    try:
        givenTime = int(givenTime)
    except ValueError:
        pattern = r'^(\d+)\s*([smhd])$'
        match = re.match(pattern, givenTime.strip().lower())
        
        if not match:
            raise ValueError(f"Invalid duration format: {givenTime}")
        
        value = int(match.group(1))
        unit = match.group(2)

        multipliers = {
            's': 1,
            'm': 60,
            'h': 3600,
            'd': 86400
        }
        givenTime = value * multipliers[unit]
    
    content = " ".join(message.content.split(" ")[3:]) or "No reason provided"

    if message.author.guild_permissions.mute_members:
        member = await guild.fetch_member(message.mentions[0].id)
        await message.channel.send(f'{message.mentions[0]} has been muted by {message.author} for reason {content}.')
        await member.timeout(datetime.timedelta(seconds=givenTime), reason=content)
    else:
        await message.channel.send(f'<@{message.author.id}>, you do not have permission to mute members.')

async def onUnmute(self, message):
    if (message.mentions == []):
        await message.channel.send(f'<@{message.author.id}>, you need to mention a user to unmute.')
        return
    guild = message.guild
    if message.author.guild_permissions.mute_members:
        member = await guild.fetch_member(message.mentions[0].id)
        await message.channel.send(f'{message.mentions[0]} has been unmuted by {message.author}')
        await member.timeout(None)
    else:
        await message.channel.send(f'<@{message.author.id}>, you do not have permission to unmute members.')
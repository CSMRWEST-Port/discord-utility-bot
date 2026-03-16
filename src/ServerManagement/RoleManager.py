import discord, PermissionsManager
from discord import Role


async def addRole(message: discord.Message):
    if not PermissionsManager.role_management_check(message):
        await message.channel.send(f"<@{message.author.id}>, you do not have permission to manage roles.")
        return
    if (message.mentions == []):
        await message.channel.send(f'<@{message.author.id}>, you need to mention a user to add a role to.')
        return
    role = getRole(message);
    if role is None:
        await message.channel.send(f'<@{message.author.id}>, the role given does not exist.')
        return
    await message.mentions[0].add_roles(role)
    await message.channel.send(f'{role} has been added to {message.mentions[0]} by {message.author}.')


async def removeRole(message: discord.Message):
    if not PermissionsManager.role_management_check(message):
        await message.channel.send(f"<@{message.author.id}>, you do not have permission to manage roles.")
        return

    if not message.mentions:
        await message.channel.send(f"<@{message.author.id}>, you need to mention a user whose role you want to remove.")
        return

    role = getRole(message);

    if role is None or role is not Role:
        await message.channel.send(f"<@{message.author.id}>, the role given does not exist.")
        return

    await message.mentions[0].remove_roles(role)
    await message.channel.send(f'{role} has been removed from {message.mentions[0]}.')


async def getRole(message: discord.Message) -> Role | None:
    guild = message.guild
    content = " ".join(message.content.split(" ")[2:])
    roleName = content.split(" ")[0]
    if roleName.startswith("<@&") and roleName.endswith(">"):
        try:
            roleId = int(roleName[3:-1])
        except (TypeError, ValueError):
            await message.channel.send(f"<@{message.author.id}>, the role given is invalid.")
            return None
        role = discord.utils.get(guild.roles, id=roleId)
    elif roleName.startswith('"') and roleName.endswith('"'):
        role = discord.utils.get(guild.roles, name=roleName[1:-1])
    else:
        role = discord.utils.get(guild.roles, name=roleName)
    return role
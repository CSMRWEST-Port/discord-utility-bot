import discord
from ServerManagement import PermissionChecks, RolePermissionDefaults
from discord import Role

import re


async def addRole(message: discord.Message):
    if not PermissionChecks.role_management_check(message):
        await message.channel.send(f"<@{message.author.id}>, you do not have permission to manage roles.")
        return
    if (message.mentions == []):
        await message.channel.send(f'<@{message.author.id}>, you need to mention a user to add a role to.')
        return
    role = await getRole(message);
    if role is None:
        await message.channel.send(f'<@{message.author.id}>, the role given does not exist.')
        return
    await message.mentions[0].add_roles(role)
    await message.channel.send(f'{role} has been added to {message.mentions[0]} by {message.author}.')


async def removeRole(message: discord.Message):
    if not PermissionChecks.role_management_check(message):
        await message.channel.send(f"<@{message.author.id}>, you do not have permission to manage roles.")
        return

    if not message.mentions:
        await message.channel.send(f"<@{message.author.id}>, you need to mention a user whose role you want to remove.")
        return

    role = await getRole(message);

    if role is None:
        await message.channel.send(f"<@{message.author.id}>, the role given does not exist.")
        return

    await message.mentions[0].remove_roles(role)
    await message.channel.send(f'{role} has been removed from {message.mentions[0]}.')


async def createRole(message: discord.Message):
    if not PermissionChecks.role_management_check(message):
        await message.channel.send(f"<@{message.author.id}>, you do not have permissions to perform this command.")
        return

    guild = message.guild
    role_permissions = await RolePermissionDefaults.get_default_role_permissions(message)
    if role_permissions is None:
        return

    regexpattern = r'"(.*?)"'
    matches = re.findall(regexpattern, message.content)
    role_name = matches[0]

    if role_name is None:
        role_name = message.content.split(" ")[1]

    await guild.create_role(name=role_name,mentionable=True,hoist=True, permissions=role_permissions)
    await message.channel.send(f'{role_name} has been created.')


async def deleteRole(message: discord.Message):
    role: discord.Role
    if not PermissionChecks.role_management_check(message):
        await message.channel.send(f"<@{message.author.id}>, you do not have permissions to perform this command.")
        return

    guild = message.guild
    role_id = message.content.split(" ")[1][3:-1]
    try:
        role_id = int(role_id)
    except (TypeError, ValueError):
        role = discord.utils.get(guild.roles, name=role_id)
        if role is None:
            await message.channel.send(f"{message.author.mention}, the role given does not exist.")
            return
    await message.guild.get_role(role_id).delete()
    await message.channel.send(f'The given role has been deleted.')




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
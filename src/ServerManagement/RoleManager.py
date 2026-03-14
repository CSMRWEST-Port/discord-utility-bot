import discord

async def addRole(message):
    if (message.mentions == []):
        await message.channel.send(f'<@{message.author.id}>, you need to mention a user to add a role to.')
        return
    guild = message.guild
    content = " ".join(message.content.split(" ")[2:])
    roleName = content.split(" ")[0]
    if roleName.startswith("<@&") and roleName.endswith(">"):
        roleId = int(roleName[3:-1])    
        role = discord.utils.get(guild.roles, id=roleId)
    else:
        role = discord.utils.get(guild.roles, name=roleName)
    if role is None:
        await message.channel.send(f'<@{message.author.id}>, the role "{roleName}" does not exist.')
        return
    if message.author.guild_permissions.manage_roles:
        await message.mentions[0].add_roles(role)
        await message.channel.send(f'{role} has been added to {message.mentions[0]} by {message.author}.')
    else:
        await message.channel.send(f'<@{message.author.id}>, you do not have permission to manage roles.')
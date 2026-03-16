import discord

async def get_default_role_permissions(message: discord.Message) -> discord.Permissions | None:
    try:
        role_type = message.content.split(" ")[2]
    except IndexError:
        await message.channel.send(f"{message.author.mention}, defaulting to no permissions on role.")
        return discord.Permissions.none()

    match role_type:
        case "administrator":
            if message.author.guild_permissions.administrator:
                return discord.Permissions(administrator=True)
            else:
                await message.channel.send(f"{message.author.mention}, you cannot create a role with greater permissions than your own.")
                return None
        case "moderator":
            perms = discord.Permissions(manage_roles=True,
                                       manage_messages=True,
                                       manage_events=True,
                                       manage_channels=True,
                                       manage_threads=True,
                                       manage_expressions=True,
                                       manage_nicknames=True,
                                       kick_members=True,
                                       mute_members=True,
                                       view_audit_log=True,
                                       view_channels=True,
                                       send_messages=True,
                                       send_polls=True,
                                       send_messages_in_threads=True,
                                       embed_links=True,
                                       use_external_emojis=True,
                                       use_reactions=True,
                                       use_application_commands=True)
            if message.author.guild_permissions in perms:
                return perms
            else:
                await message.channel.send(f"{message.author.mention}, you cannot create a role with greater permissions than your own.")
                return None
        case "general":
            return discord.Permissions.general()
    return discord.Permissions.none()
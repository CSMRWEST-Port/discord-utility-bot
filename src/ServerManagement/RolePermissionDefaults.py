import discord
import re

async def get_default_role_permissions(message: discord.Message) -> discord.Permissions | None:
    content = message.content
    result = re.sub(r'"(.*?)"', '', content)
    result = result.replace('  ', ' ').strip()
    try:
        role_type = result.split(' ')[1]
    except IndexError:
        await message.channel.send(f"{message.author.mention}, defaulting to no permissions on role.")
        return discord.Permissions.none()

    match role_type.lower():
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
                                       use_application_commands=True,
                                        mention_everyone=True)
            if message.author.guild_permissions.is_superset(perms):
                return perms
            else:
                await message.channel.send(f"{message.author.mention}, you cannot create a role with greater permissions than your own.")
                return None
        case "general":
            perms = discord.Permissions.none()
            perms.update(
                view_channel=True,
                send_messages=True,
                send_messages_in_threads=True,
                embed_links=True,
                use_reactions=True,
                read_message_history=True,
                connect=True,
                speak=True
            )
            if message.author.guild_permissions.is_superset(perms) or message.author.guild_permissions.administrator:
                return perms
            else:
                await message.channel.send(f"{message.author.mention}, you cannot create a role with greater permissions than your own.")
                return None
        case _:
            perms = discord.Permissions.none()
            return perms
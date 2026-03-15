import discord


def guild_management_check(message: discord.Message):
    author_perms = message.author.guild_permissions
    return author_perms.administrator or author_perms.manage_guild

def message_deletion_check(message: discord.Message):
    author_perms = message.author.guild_permissions
    return author_perms.administrator or author_perms.manage_messages

def user_management_check(message: discord.Message, action: str):
    author_perms = message.author.guild_permissions
    match action:
        case 'mute':
            return author_perms.mute_members or author_perms.administrator
        case 'unmute':
            return author_perms.mute_members or author_perms.administrator
        case 'kick':
            return author_perms.kick_members or author_perms.administrator
        case 'ban':
            return author_perms.ban_members or author_perms.administrator
    return False
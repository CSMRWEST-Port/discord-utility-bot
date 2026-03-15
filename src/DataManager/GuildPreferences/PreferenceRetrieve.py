from DataManager.GuildPreferences.PreferenceStore import check_guild_exists, make_guild_if_not_exists


def get_guild_preferences(guild_id, connection):
    if (check_guild_exists(guild_id, connection) == False):
        make_guild_if_not_exists(guild_id, connection)
    with connection.cursor() as cursor:
        cursor.execute("SELECT auto_role, welcome_channel, goodbye_channel, moderator_roles, welcome_message, goodbye_message FROM guild_preferences WHERE guild_id = %s", (str(guild_id),))
        result = cursor.fetchone()
        preferences = {'auto_role': result[0], 'welcome_channel': result[1], 'goodbye_channel': result[2], 'moderator_roles': result[3], 'custom_welcome_message': result[4], 'custom_goodbye_message': result[5]}
    return preferences


def get_welcome_channel(guild_id, connection):
    if (check_guild_exists(guild_id, connection) == False):
        make_guild_if_not_exists(guild_id, connection)
        return 'None'
    else:
        with connection.cursor() as cursor:
            cursor.execute("SELECT welcome_channel FROM guild_preferences WHERE guild_id = %s", (str(guild_id),))
            result = cursor.fetchone()
            return result[0]


def get_custom_welcome_message(guild_id, connection):
    if (check_guild_exists(guild_id, connection) == False):
        make_guild_if_not_exists(guild_id, connection)
        return 'None'
    with connection.cursor() as cursor:
        cursor.execute("SELECT welcome_message FROM guild_preferences WHERE guild_id = %s", (str(guild_id),))
        result = cursor.fetchone()
        return result[0]


def get_goodbye_channel(guild_id, connection):
    if (check_guild_exists(guild_id, connection) == False):
        make_guild_if_not_exists(guild_id, connection)
        return 'None'
    with connection.cursor() as cursor:
        cursor.execute("SELECT goodbye_message FROM guild_preferences WHERE guild_id = %s", (str(guild_id),))
        result = cursor.fetchone()
        return result[0]


def get_custom_goodbye_message(guild_id, connection):
    if (check_guild_exists(guild_id, connection) == False):
        make_guild_if_not_exists(guild_id, connection)
        return 'None'
    with connection.cursor() as cursor:
        cursor.execute("SELECT goodbye_message FROM guild_preferences WHERE guild_id = %s", (str(guild_id),))
        result = cursor.fetchone()
        return result[0]

def check_guild_exists(guild_id, connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM guild_preferences WHERE guild_id = %s", (str(guild_id),))
        return cursor.fetchone() is not None


def make_guild_if_not_exists(guild_id, connection):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO guild_preferences (guild_id, auto_role, welcome_channel, goodbye_channel,welcome_message, goodbye_message) VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (guild_id) DO NOTHING", (str(guild_id), 'None', 'None', 'None', 'None', 'None'))
        connection.commit()


def set_welcome_channel(guild_id, channel_id, connection):
    if (check_guild_exists(guild_id, connection) == False):
        make_guild_if_not_exists(guild_id, connection)
    with connection.cursor() as cursor:
        cursor.execute("UPDATE guild_preferences SET welcome_channel = %s WHERE guild_id = %s", (str(channel_id), str(guild_id)))
        connection.commit()


def set_custom_welcome_message(guild_id, welcome_message, connection):
    if (check_guild_exists(guild_id, connection) == False):
        make_guild_if_not_exists(guild_id, connection)
    with connection.cursor() as cursor:
        cursor.execute("UPDATE guild_preferences SET welcome_message = %s WHERE guild_id = %s", (welcome_message, str(guild_id)))
        connection.commit()


def set_goodbye_channel(guild_id, channel_id, connection):
    if (check_guild_exists(guild_id, connection) == False):
        make_guild_if_not_exists(guild_id, connection)
    with connection.cursor() as cursor:
        cursor.execute("UPDATE guild_preferences SET goodbye_channel = %s WHERE guild_id = %s", (str(channel_id), str(guild_id)))
        connection.commit()

def set_custom_goodbye_message(guild_id, goodbye_message, connection):
    if (check_guild_exists(guild_id, connection) == False):
        make_guild_if_not_exists(guild_id, connection)
    with connection.cursor() as cursor:
        cursor.execute("UPDATE guild_preferences SET goodbye_message = %s WHERE guild_id = %s", (goodbye_message, str(guild_id)))
        connection.commit()


import psycopg2

def check_guild_exists(guild_id, connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM guild_preferences WHERE guild_id = %s", (str(guild_id),))
        return cursor.fetchone() is not None
    
def make_guild_if_not_exists(guild_id, connection):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO guild_preferences (guild_id, auto_role, welcome_channel, goodbye_channel,welcome_message, goodbye_message) VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (guild_id) DO NOTHING", (str(guild_id), 'None', 'None', 'None', 'None', 'None'))
        connection.commit()

def get_guild_preferences(guild_id, connection):
    if (check_guild_exists(guild_id, connection) == False):
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO guild_preferences (guild_id, auto_role, welcome_channel, goodbye_channel, welcome_message, goodbye_message) VALUES (%s, %s, %s, %s, %s, %s)", (str(guild_id), 'None', 'None', 'None', 'None', 'None'))
            connection.commit()
    with connection.cursor() as cursor:
        cursor.execute("SELECT auto_role, welcome_channel, goodbye_channel, moderator_roles, welcome_message, goodbye_message FROM guild_preferences WHERE guild_id = %s", (str(guild_id),))
        result = cursor.fetchone()
        preferences = {'auto_role': result[0], 'welcome_channel': result[1], 'goodbye_channel': result[2], 'moderator_roles': result[3], 'custom_welcome_message': result[4], 'custom_goodbye_message': result[5]}
    return preferences

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
import psycopg2


async def initialise_database(connection: psycopg2.extensions.connection):
    with connection.cursor() as cursor:
        cursor.execute('''CREATE TABLE IF NOT EXISTS guild_preferences (
                                guild_id INTEGER NOT NULL PRIMARY KEY,
                                auto_role TEXT NOT NULL,
                                welcome_channel TEXT NOT NULL,
                                welcome_message TEXT NOT NULL,
                                goodbye_channel TEXT NOT NULL,
                                goodbye_message TEXT NOT NULL
                            );
                ''')
        connection.commit();
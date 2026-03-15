from DataManager import Connection;


# Ensure tables are created before the bot activates
databaseConnection = Connection.DatabaseConnection();
while databaseConnection.connection is None:
    databaseConnection.connect();

with databaseConnection.connection.cursor() as cur:
    cur.execute('''CREATE TABLE IF NOT EXISTS guild_preferences (
                    guild_id INTEGER NOT NULL PRIMARY KEY,
                    auto_role TEXT NOT NULL,
                    welcome_channel TEXT NOT NULL,
                    welcome_message TEXT NOT NULL,
                    goodbye_channel TEXT NOT NULL,
                    goodbye_message TEXT NOT NULL
                );
    ''')
    databaseConnection.connection.commit();

# Add further table creations above this line
databaseConnection.connection.close();

import bot

bot()
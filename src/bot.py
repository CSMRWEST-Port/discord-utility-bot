import os

import discord; from discord.ext import commands;
from ServerManagement import RoleManager, WelcomeUsers
from UserManagement import ModerationActions;
from DataManager import Connection;
from MessageManagement import MessageDeletion;
from DataManager.GuildPreferences import PreferenceStore, PreferenceRetrieve


class Bot:

    def __init__(self, client):
        self.client = client
        self.databaseConnection = Connection.DatabaseConnection()
        self.databaseConnection.connect()
        self.createCommands(self.client)
        self.run()


    def createCommands(self, client: commands.Bot):

        @client.event
        async def on_ready():
            await client.change_presence(activity=discord.Game(name="Committing 50 different murders"))

        @client.event
        async def on_member_join(member):
            try:
                channel_id = int(PreferenceRetrieve.get_welcome_channel(member.guild.id, self.databaseConnection.connection))
            except (TypeError, ValueError):
                return
            channel = client.get_channel(channel_id)
            if channel:
                db_store_message = PreferenceRetrieve.get_custom_welcome_message(member.guild.id, self.databaseConnection.connection)
                welcome_message = db_store_message if db_store_message != "None" else "Welcome to the server"
                await channel.send(f'{welcome_message}, <@{member.id}>!')


    def run(self):
        self.client.run(os.getenv('BOT_TOKEN'))

if __name__ == '__main__':
    print('Class is not runnable')
    raise Exception('Class is not runnable')
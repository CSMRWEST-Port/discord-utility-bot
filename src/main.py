import asyncio;
import os

import discord
from discord.ext import commands;

from DataManager import Connection;
from DataManager import DatabaseInit;


def createIntents() -> discord.Intents:
    intents = discord.Intents.default()

    intents.members = True
    intents.message_content = True
    intents.guilds = True
    intents.presences = True

    return intents


class Bot(commands.Bot):
    def __init__(self):
        intents = createIntents();
        super().__init__(command_prefix="!", intents=intents)
        self.database = None;

    async def load_extensions(self):
        for f in os.listdir('COGs'):
            if f.endswith('.py'):
                await self.load_extension(f'COGs.{f[:-3]}');

    async def setup_hook(self):
        connection = Connection.DatabaseConnection();
        while connection.connection is None:
            connection.connect();

        self.database = connection;
        await DatabaseInit.initialise_database(self.database.connection);

        await self.load_extensions();


async def main():
    bot = Bot()
    async with bot:
        await bot.start(os.getenv('BOT_TOKEN'));

if __name__ == '__main__':
    asyncio.run(main())
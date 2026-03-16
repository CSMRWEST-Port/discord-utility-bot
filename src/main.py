import os

from DataManager import Connection;
import bot
import discord
from discord.ext import commands;
import asyncio;

def createIntents():
    intents = discord.Intents.default()

    intents.members = True
    intents.message_content = True
    intents.guilds = True
    intents.presences = True

    return intents


async def load_extensions():
    for f in os.listdir('COGs'):
        if f.endswith('.py'):
            await client.load_extension(f'COGs.{f[:-3]}');


async def main():
    async with client:
        await load_extensions()
        await client.start(os.getenv('BOT_TOKEN'));

client = commands.Bot(command_prefix = '!', intents = createIntents());

if __name__ == '__main__':
    asyncio.run(main());
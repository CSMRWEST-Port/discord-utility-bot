from main import Bot
from discord.ext import commands
import discord

from DataManager.GuildPreferences import PreferenceRetrieve

class EventListeners(commands.Cog):
    def __init__(self, client: Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Game(name="Committing 50 different murders"))

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        try:
            channel_id = int(PreferenceRetrieve.get_welcome_channel(member.guild.id, self.client.database.connection))
        except (TypeError, ValueError):
            return
        channel = self.client.get_channel(channel_id)
        if channel:
            db_store_message = PreferenceRetrieve.get_custom_welcome_message(member.guild.id, self.databaseConnection.connection)
            welcome_message = db_store_message if db_store_message != "None" else "Welcome to the server"
            await channel.send(f'{welcome_message}, <@{member.id}>!')

async def setup(client: commands.Bot):
    await client.add_cog(EventListeners(client))
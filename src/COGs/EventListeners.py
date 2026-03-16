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
            db_store_message = PreferenceRetrieve.get_custom_welcome_message(member.guild.id, self.client.database.connection)
            welcome_message = db_store_message if db_store_message != "None" else "Welcome to the server"
            await channel.send(f'{welcome_message}, <@{member.id}>!')

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        guild_id = member.guild.id
        channel_id = PreferenceRetrieve.get_goodbye_channel(guild_id, self.client.database.connection)
        if channel_id != "None":
            channel_id = int(channel_id)
        else:
            return
        channel = await self.client.fetch_channel(channel_id)
        if channel:
            goodbye_message = PreferenceRetrieve.get_custom_goodbye_message(member.guild.id, self.client.database.connection)
            await channel.send(f'{goodbye_message}, <@{member.id}>!')
        else:
            return

async def setup(client: commands.Bot):
    await client.add_cog(EventListeners(client))
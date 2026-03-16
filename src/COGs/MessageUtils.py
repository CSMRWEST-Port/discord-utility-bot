import discord
from discord.ext import commands

from MessageManagement import MessageDeletion

class MessageUtils(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='purge', description='Deletes a specified number of messages from the channel')
    async def purge(self, ctx):
        await MessageDeletion.purge(message=ctx.message)



async def setup(client):
    await client.add_cog(MessageUtils(client))
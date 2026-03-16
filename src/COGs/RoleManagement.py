import discord
from discord.ext import commands

from ServerManagement import RoleManager

class RoleManagement(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(name='addrole', description='Adds a specified role to a mentioned user')
    async def addrole(self, ctx: commands.Context):
        await RoleManager.addRole(message=ctx.message)


async def setup(client: commands.Bot):
    await client.add_cog(RoleManagement(client))
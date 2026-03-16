import discord
from discord.ext import commands

from ServerManagement import RoleManager

class RoleManagement(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='addrole', description='Adds a specified role to a mentioned user')
    async def addrole(self, ctx):
        await RoleManager.addRole(message=ctx.message)


async def setup(client):
    await client.add_cog(RoleManagement(client))
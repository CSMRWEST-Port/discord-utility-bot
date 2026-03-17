from discord.ext import commands

from ServerManagement import RoleManager

class RoleManagement(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(name='addrole', description='Adds a specified role to a mentioned user')
    async def addrole(self, ctx: commands.Context):
        await RoleManager.addRole(message=ctx.message)

    @commands.command(name='removerole', description='Removes a specified role from a mentioned user')
    async def removerole(self, ctx: commands.Context):
        await RoleManager.removeRole(message=ctx.message)

    @commands.command(name='createrole', description='Creates a role')
    async def createrole(self, ctx: commands.Context):
        await RoleManager.createRole(message=ctx.message)

    @commands.command(name='deleterole', description='Deletes a specified role from the guild.')
    async def deleterole(self, ctx: commands.Context):
        await RoleManager.deleteRole(message=ctx.message)


async def setup(client: commands.Bot):
    await client.add_cog(RoleManagement(client))
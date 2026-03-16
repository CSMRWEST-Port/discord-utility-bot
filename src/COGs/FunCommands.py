import discord
from discord.ext import commands


# noinspection PyMethodParameters,PyRedundantParentheses
class FunCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='benice', description='Tells the user to be nice')
    async def benice(self, ctx: commands.Context):
        if (ctx.message.mentions == []):
            await ctx.send(f'<@{ctx.message.author.id}>, be nice to yourself ig')
        elif (ctx.message.mentions[0].guild_permissions.administrator):
            await ctx.send(f'<@{ctx.message.author.id}>, you cannot tell an administrator to be nice!')
        elif (ctx.message.author.guild_permissions.administrator):
            await ctx.send(f'<@{ctx.message.mentions[0].id}>, please be nice!')
        else:
            await ctx.send(f'<@{ctx.message.author.id}> shut up non')


async def setup(client):
    await client.add_cog(FunCommands(client))
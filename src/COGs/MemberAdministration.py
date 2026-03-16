import discord
from discord.ext import commands

from UserManagement import ModerationActions


# noinspection PyMethodParameters
class MemberAdministration(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='ban', description='Bans a user from the server')
    async def ban(self, ctx):
        await ModerationActions.onBan(message=ctx.message)


    @commands.command(name='unban', description='Unbans a user from the server')
    async def unban(self, ctx):
        await ModerationActions.onUnban(message=ctx.message)


    @commands.command(name='kick', description='Kicks a user from the server')
    async def kick(self, ctx):
        await ModerationActions.onKick(message=ctx.message)


    @commands.command(name='mute', description='Mutes a user in the server')
    async def mute(self, ctx):
        await ModerationActions.onMute(message=ctx.message)


    @commands.command(name='unmute', description='Unmutes a user in the server')
    async def unmute(self, ctx):
        await ModerationActions.onUnmute(message=ctx.message)


async def setup(client):
    await client.add_cog(MemberAdministration(client))
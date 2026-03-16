import discord
from discord.ext import commands
from main import Bot

from ServerManagement import WelcomeUsers

class GreetingsAndGoodbyes(commands.Cog):
    def __init__(self, client: Bot):
        self.client = client

    @commands.command(name='setwelcomechannel', description='Sets a custom welcome channel for the server')
    async def setwelcomechannel(self, ctx: commands.Context):
        await WelcomeUsers.setWelcomeChannel(ctx.message, self.client.database)

    @commands.command(name='setwelcomemessage', description='Sets a custom welcome message for the server')
    async def setwelcomemessage(self, ctx: commands.Context):
        await WelcomeUsers.setCustomWelcomeMessage(ctx.message, self.client.database)

    @commands.command(name='setgoodbyechannel', description='Sets a custom goodbye channel for the server')
    async def setgoodbyechannel(self, ctx: commands.Context):
        await WelcomeUsers.setGoodbyeChannel(ctx.message, self.client.database)

    @commands.command(name='setgoodbyemessage', description='Sets a goodbye message for the server')
    async def setgoodbyemessage(self, ctx: commands.Context):
        await WelcomeUsers.setCustomGoodbyeMessage(ctx.message, self.client.database)


async def setup(client: commands.Bot):
    await client.add_cog(GreetingsAndGoodbyes(client))
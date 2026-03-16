import discord
from discord.ext import commands

from ServerManagement import WelcomeUsers

class GreetingsAndGoodbyes(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='setwelcomechannel', description='Sets a custom welcome channel for the server')
    async def setwelcomechannel(self, ctx):
        await WelcomeUsers.setWelcomeChannel(ctx.message, self.databaseConnection)

    @commands.command(name='setwelcomemessage', description='Sets a custom welcome message for the server')
    async def setwelcomemessage(self, ctx):
        await WelcomeUsers.setCustomWelcomeMessage(ctx.message, self.databaseConnection)


async def setup(client):
    await client.add_cog(GreetingsAndGoodbyes(client))
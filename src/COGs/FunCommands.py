import discord
from discord.ext import commands

import FunnyCommands.MiniGames as MiniGames


# noinspection PyMethodParameters,PyRedundantParentheses
class FunCommands(commands.Cog):
    def __init__(self, client: commands.Bot):
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


    @commands.command(name='diceroll', description='Rolls a dice of the user\'s specification')
    async def diceroll(self, ctx: commands.Context):
        message = ctx.message
        dicetype: str = "d4"
        try:
            dicetype = message.content.split(" ")[1]
        except IndexError:
            res = await MiniGames.diceroll("d4");
        else:
            res = await MiniGames.diceroll(dicetype)

        await message.channel.send(f"{res} was rolled on a {dicetype}")





async def setup(client: commands.Bot):
    await client.add_cog(FunCommands(client))
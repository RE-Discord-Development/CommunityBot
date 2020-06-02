from discord.ext import commands
import discord
import logging


# Setup is required by discord.py for registration of the cog
def setup(bot):
    bot.add_cog(Greetings(bot))


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        logging.debug("Starting Hello with {0}".format(ctx.author.id))
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hello {0.name}~'.format(member))
        else:
            await ctx.send('Hello {0.name}... This feels familiar.'.format(member))
        self._last_member = member

        logging.debug("Ending Hello with {0}".format(ctx.author.id))

from discord.ext import commands
import discord
import logging
import prometheus_client


# Set up some metrics for monitoring purposes
hello_response_time = prometheus_client.Summary('communitybot_hello_response_time', 'The time hello takes to run')


# Setup is required by discord.py for registration of the cog
def setup(bot):
    bot.add_cog(Greetings(bot))


class Greetings(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=['contribute'])
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello and share information about myself"""
        with hello_response_time.time():
            logging.debug("Starting Hello with {0}".format(ctx.author.id))
            message = "Hello <@{0}>! \n I am <@{1}>, a community driven project "\
                "for the Real Engineering Discord. If you want to get involved, my source "\
                "can be found at https://github.com/RE-Discord-Development/CommunityBot "\
                "Feel free to write a new Cog to make me do something and submit a pull request\n"\
                "If you have any questions, then feel free to ping CatButtes or Potzerus for "\
                "more information"\
                .format(ctx.author.id, self.bot.user.id)

            await ctx.send(message)
            logging.debug("Ending Hello with {0}".format(ctx.author.id))

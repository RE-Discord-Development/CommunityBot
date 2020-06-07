from discord.ext import commands
import logging
import prometheus_client


# Set up some metrics for monitoring purposes
mod_response_time = prometheus_client.Summary('communitybot_mod_response_time',
                                              'The time hello takes to run')
ls_response_time = prometheus_client.Summary('communitybot_ls_response_time',
                                             'The time "mod ls" takes to run')
unload_response_time = prometheus_client.Summary('communitybot_unload_response_time',
                                                 'The time "mod unload" takes to run')


# Setup is required by discord.py for registration of the cog
def setup(bot):
    bot.add_cog(Moderation(bot))


class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.group(invoke_without_command=False)
    async def mod(self, ctx):
        """Manage CommunityBot plugins"""
        pass

    @mod.command()
    @commands.has_guild_permissions(manage_roles=True)
    async def ls(self, ctx) -> None:
        with ls_response_time.time():
            logging.debug("listing plugins")
            """List the loaded plugins"""
            for ext in self.bot.extensions:
                await ctx.send(ext)

    @mod.command()
    @commands.has_guild_permissions(manage_roles=True)
    async def unload(self, ctx, plugin) -> None:
        with unload_response_time.time():
            logging.debug("unloading plugin {0}".format(plugin))
            """Unload a loaded plugin"""
            if plugin in self.bot.extensions:
                self.bot.unload_extension(plugin)
                logging.debug("unloaded plugin {0}".format(plugin))
                await ctx.send("unloaded plugin {0}".format(plugin))

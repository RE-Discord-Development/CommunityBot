from discord.ext import commands
# This Cog is made by Potzerus#3950 and is meant to facilitate a little game


class SpaceShips(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.players = {}

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        await ctx.send(error)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Yes I am alive hi")

    def get_player(self, id):
        if id not in self.players:
            self.players[id] = {}
        return self.players[id]

    def get_stat(self, id, stat):
        player = self.get_player(id)
        if stat not in player:
            player[stat] = 0
        return player[stat]

    def set_stat(self, id, stat, value):
        player = self.get_player(id)
        player[stat] = value


# Setup is required by discord.py for registration of the cog
# Can be at the bottom of a file too, make sure to change the name to reflect the name of your Cog Class
def setup(bot):
    bot.add_cog(SpaceShips(bot))

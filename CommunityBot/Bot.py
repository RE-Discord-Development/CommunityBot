from discord.ext import commands
import os
from typing import List


class Bot(commands.Bot):
    def __init__(self, config):
        super().__init__(commands.bot.when_mentioned)
        self.config = config
        self.load_plugins()

    def run(self, **kwargs):
        if len(kwargs) == 0:
            super().run(self.config["bot_token"])
        else:
            super().run(self.config["bot_token"], kwargs)

    def load_plugins(self) -> None:
        plugins: List() = []
        for item in os.listdir("Cogs"):
            if os.path.isdir("Cogs/{0}".format(item)):
                if "__init__.py" in os.listdir("Cogs/{0}".format(item)):
                    plugins.append("Cogs.{0}".format(item))
            else:
                plugins.append("Cogs.{0}".format(item))

        for plugin in plugins:
            self.load_extension(plugin)

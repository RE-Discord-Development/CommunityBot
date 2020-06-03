from discord.ext import commands
import os
from typing import List
import logging
import traceback


class Bot(commands.Bot):
    def __init__(self, config):
        super().__init__(commands.bot.when_mentioned)
        logging.debug("Initialising Bot")
        self.config = config
        self.load_plugins()
        logging.debug("Initialised Bot")

    def run(self, **kwargs):
        logging.debug("Starting event loop")
        if len(kwargs) == 0:
            super().run(self.config["bot_token"])
        else:
            super().run(self.config["bot_token"], kwargs)

    def load_plugins(self) -> None:
        logging.debug("Scanning ./Cogs for cogs")
        plugins: List() = []
        for item in os.listdir("Cogs"):
            logging.debug("Found item: {0}".format(item))
            if os.path.isdir("Cogs/{0}".format(item)):
                if "__init__.py" in os.listdir("Cogs/{0}".format(item)):
                    logging.debug("Found Cog: {0}".format(item))
                    plugins.append("Cogs.{0}".format(item))
            else:
                logging.debug("Found Cog: {0}".format(item))
                item = str.replace(item, ".py", "")
                plugins.append("Cogs.{0}".format(item))

        for plugin in plugins:
            logging.debug("Loading {0}".format(plugin))
            try:
                self.load_extension(plugin)
                logging.debug("Loaded {0}".format(plugin))
            except Exception as err:
                logging.exception("Error loading {0}: {1}".format(plugin, err))

        logging.debug("Scanned ./Cogs for cogs")

    def on_command_error(self, cxt, error):
        logging.exception("A command error occurred: {0}".format(
            ''.join(traceback.format_exception(None, value=error, tb=error.__traceback__))))

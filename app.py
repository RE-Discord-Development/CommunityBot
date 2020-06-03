#!/usr/bin/env python3
import CommunityBot
import os
import yaml
import logging
import logging.config


def main():

    with open("logging.yml", 'rt') as f:
        logging_config = yaml.safe_load(f.read())
        logging.config.dictConfig(logging_config)

    config = dict()
    config["bot_token"] = os.environ['BOT_TOKEN']
    config["bot_storage"] = os.environ['BOT_STORAGE']

    bot = CommunityBot.Bot(config)
    bot.run()


if __name__ == "__main__":

    main()

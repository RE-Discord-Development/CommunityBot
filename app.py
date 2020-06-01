#!/usr/bin/env python3
import CommunityBot
import os


def main():

    config = dict()
    config["bot_token"] = os.environ['BOT_TOKEN']

    bot = CommunityBot.Bot(config)
    bot.run()


if __name__ == "__main__":
    main()

import json

import discord
from discord.ext import commands
from pathlib import Path

from typing import List


def get_or_make_file():
    path_string = "../Data/Moderation/banned_words.json"
    my_file = Path(path_string)
    if not my_file.exists():
        with open(path_string, "w+") as file:
            file.write("[]")
    with open(path_string, "r") as file:
        return file.read()


def save_file(words):
    path_string = "../Data/Moderation/banned_words.json"
    with open(path_string, "w+") as file:
        file.write(json.dumps(words))


class ModerationCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.banned_word_list: List[str] = json.loads(get_or_make_file())

    @commands.Cog.listener()
    async def on_message(self, message):
        if isinstance(message.author, discord.Member):
            if not message.author.permissions_in(message.channel).manage_messages:
                for word in self.banned_word_list:
                    if word in message.content:
                        await message.delete()

    @commands.group(invoke_without_command=True)
    @commands.check(commands.has_permissions(manage_messages=True))
    async def wordfilter(self, ctx):
        await ctx.send(self.banned_word_list)

    @wordfilter.command(name="add")
    @commands.check(commands.has_permissions(manage_messages=True))
    async def wordfilter_add(self, ctx, *, term: str):
        self.banned_word_list.append(term)
        save_file(self.banned_word_list)
        await ctx.send(f"Successfully added {term}")

    @wordfilter.command(name="remove", aliases=["rem"])
    @commands.check(commands.has_permissions(manage_messages=True))
    async def wordfilter_remove(self, ctx, *, term: str):
        self.banned_word_list.remove(term)
        save_file(self.banned_word_list)
        await ctx.send(f"Successfully removed {term}")


def setup(bot):
    bot.add_cog(ModerationCog(bot))

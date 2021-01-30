from datetime import datetime
import logging

import discord
import discord.ext.commands as commands
from discord.ext.commands import converter

from bot.data.remind_repository import RemindRepository
from bot.utils import converters

log = logging.getLogger(__name__)


class RemindCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.current = []

    @commands.command()
    async def remind(self, ctx: commands.Context, wait: converters.Duration, message: str):
        user = {}
        user["id"] = ctx.message.author
        user["time"] = wait:while
        user["Message"] = message
        self.current.append(user)
        self.bot.scheduler.schedule_at(self.test(wait), time=user["time"])

    async def test(self, time: datetime):
        for user in self.current:
            if user["time"] == time:
                await user["id"].send(user["Message"])
                self.current.remove(user)

def setup(bot):
    bot.add_cog(RemindCog(bot))

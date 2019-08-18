import logging

from discord.ext.commands import Cog, Context, group


logger = logging.getLogger(__name__)


class EventSchedulerCog(Cog):
    """Cog that handles event registration, editing, deletion and alerting."""

    def __init__(self, bot):
        self.bot = bot

    @group(name='scheduler', invoke_without_command=True)
    async def scheduler_group(self, ctx: Context):
        """Command group used to create subcommands."""
        await ctx.invoke(self.bot.get_command("help"), 'scheduler')

    @scheduler_group.command(name='event')
    async def event_command(self, ctx: Context, method: str, event_type: str, name: str):
        pass


def setup(bot):
    bot.add_cog(EventSchedulerCog(bot))

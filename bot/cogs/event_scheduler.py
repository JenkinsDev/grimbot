class EventSchedulerCog:
    """Cog that handles event registration, editing, deletion and alerting."""

    prefix = 'scheduler'

    def __init__(self, bot):
        self.bot = bot

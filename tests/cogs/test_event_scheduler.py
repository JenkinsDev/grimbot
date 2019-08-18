from bot.cogs.event_scheduler import EventSchedulerCog
from ..fixtures import FauxGrimBot


class TestEventSchedulerCog:

    def setup(self):
        self.scheduler = EventSchedulerCog(FauxGrimBot())

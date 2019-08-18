from bot.cogs.event_scheduler import EventSchedulerCog
from ..fixtures import FauxGrimBot


class TestEventSchedulerCog:

    def setup(self):
        self.scheduler = EventSchedulerCog(FauxGrimBot())

    def test_prefix_is_set_to_scheduler(self):
        assert self.scheduler.prefix == 'scheduler'

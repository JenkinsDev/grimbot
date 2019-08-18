import pytest

from unittest.mock import MagicMock
from discord import Client
from bot.bot import GrimBot


@pytest.fixture()
def patched_grimbot(monkeypatch):
    """Provides a monkeypatched discord.Client.run for use with testing GrimBot
    since we inherit from discord.Client. This allows us to not have to worry
    about the bot attempting to connect to the discord server.
    """
    with monkeypatch.context() as m:
        m.setattr("bot.bot.Client.run", MagicMock())
        yield GrimBot


class TestGrimBot:

    def setup(self):
        self.faux_config = {"DISCORD_SECRET": "xyz"}

    def test_listen_raises_valueerror_if_config_not_set(self, patched_grimbot):
        no_config_bot = patched_grimbot()
        with pytest.raises(ValueError):
            no_config_bot.listen()

    def test_listen_raises_valueerror_if_discord_secret_does_not_exist(self, patched_grimbot):
        # Our config class, for the purposes of this test, is easily
        # interchangable with a dictionary. KISS.
        bot = patched_grimbot({})
        with pytest.raises(ValueError):
            bot.listen()

    def test_listen_calls_parents_run_with_config_secret(self, patched_grimbot):
        bot = patched_grimbot(self.faux_config)
        bot.listen()
        bot.run.assert_called_once_with(self.faux_config['DISCORD_SECRET'])

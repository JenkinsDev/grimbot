from discord import Client


class GrimBot(Client):
    """The meat of GrimBot, acts as the interface between Discord and the rest
    of our application.

    Properties:
        _config (config.Config): Configuration object for bot config.

    Parameters:
        config (config.Config): Used to set the _config object property.
    """

    def __init__(self, config=None):
        self._config = config

    async def on_ready(self):
        """Called when our bot has successfully connected to a server, and is
        ready to start processing commands."""
        print(f'We have logged in as {self.user}')

    async def on_message(self, msg):
        """Called when our bot has successfully intercepted a message sent
        to a server / channel that our bot can read from."""
        if msg.author == self.user:
            return

        await msg.channel.send(msg.content)


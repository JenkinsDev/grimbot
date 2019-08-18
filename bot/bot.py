from discord import Client


class GrimBot(Client):
    """The meat of GrimBot, acts as the interface between Discord and the rest
    of our application.

    Properties:
        _config (config.Config): Configuration object for bot config.

    Parameters:
        config (config.Config): Used to set the _config object property.
    """
    command_prefix = '!'

    def __init__(self, config=None):
        super().__init__()
        self._config = config

    def listen(self):
        """Connect to Discord and start listening on all channels the bot
        has access to.

        Note: This function is blocking and will start an event loop.

        Raises:
            ValueError: If _config or _config['DISCORD_SECRET'] is not set.
        """
        if self._config is None:
            raise ValueError("_config must be set before running GrimBot")

        if 'DISCORD_SECRET' not in self._config:
            raise ValueError("_config must contain a DISCORD_SECRET key")

        self.run(self._config['DISCORD_SECRET'])

    async def on_ready(self):
        """Called when our bot has successfully connected to a guild, and is
        ready to start processing commands."""
        print(f'We have logged in as {self.user}')

    async def on_message(self, msg):
        """Called when our bot has successfully intercepted a message sent
        to a guild / channel the bot can read from."""
        if msg.author == self.user:
            return

        await msg.channel.send(msg.content)

    async def on_error(self, err):
        print(f'error {err}')

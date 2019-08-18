import logging

from .bot import GrimBot
from .config import Config


if __name__ == "__main__":
    config = Config()
    config.load_file('.env')

    logger = logging.getLogger(__name__)

    # TODO: Implement a custom logging class so we can implement
    # colored output when in debug mode. Also, pass config
    logger.setLevel(logging.DEBUG)

    logger.info('[Starting GrimBot]')

    bot = GrimBot(config=config)
    bot.listen()

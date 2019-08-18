import logging

from .bot import GrimBot
from .config import Config
from .__version__ import __version__


if __name__ == "__main__":
    config = Config()
    config.load_file('.env')

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    stdout_handler = logging.StreamHandler()
    stdout_handler.setLevel(logging.DEBUG)

    logger.addHandler(stdout_handler)
    logger.info(f'[Starting GrimBot v{__version__}]')

    bot = GrimBot(config=config)
    bot.listen()

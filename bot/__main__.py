from .bot import GrimBot
from .config import Config


if __name__ == "__main__":
    config = Config()
    bot = GrimBot(config=config)
    bot.run()

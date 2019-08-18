from .bot import GrimBot
from .config import Config


if __name__ == "__main__":
    config = Config()
    config.load_file('.env')
    bot = GrimBot(config=config)
    bot.listen()

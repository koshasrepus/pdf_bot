import logging
from telegram.ext import ApplicationBuilder, CommandHandler

from config import Config
from commands import commands

if __name__ == '__main__':
    conf = Config()
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.DEBUG
    )
    app = ApplicationBuilder().token(conf.bot_token).build()
    handlers = [CommandHandler(*command) for command in commands]
    app.add_handlers(handlers)
    app.run_polling()





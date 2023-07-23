import logging
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

from config import Config
from commands import commands, hand_pdf_to_txt

if __name__ == '__main__':
    conf = Config()
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.DEBUG
    )
    app = ApplicationBuilder().token(conf.bot_token).build()
    handlers = [CommandHandler(*command) for command in commands]
    app.add_handlers(handlers)
    app.add_handler(
        MessageHandler(filters.Document.TXT, hand_pdf_to_txt)
    )
    app.run_polling()
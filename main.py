import logging

from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

from commands import commands, hand_pdf_to_txt
from config import Config


def run():
    conf = Config()

    logging_level = logging.DEBUG if conf.debug else logging.ERROR
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging_level,
    )

    app = ApplicationBuilder().token(conf.bot_token).build()

    handlers = [CommandHandler(*command) for command in commands]
    app.add_handlers(handlers)

    app.add_handler(MessageHandler(filters.Document.PDF, hand_pdf_to_txt))

    app.run_polling()


if __name__ == "__main__":
    run()

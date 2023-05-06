from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    resp = '/start - информация о боте\nБот конвертирует файлы PDF в формат txt\n' \
           'Отправъте файл PDF в сообщении для конвертации в формат txt'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=resp)


commands = [
    ('start', start)
]

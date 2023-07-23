from asyncio import sleep

from telegram import Update
from telegram.ext import ContextTypes

import requests


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    resp = '/start - информация о боте\nБот конвертирует файлы PDF в формат txt\n' \
           'Отправъте файл PDF в сообщении для конвертации в формат txt'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=resp)


async def hand_pdf_to_txt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # file_id = update.message.document.file_id
    doc = update.effective_message.document
    front_file = await doc.get_file()
    file_to_convert = requests.get(front_file.file_path).content
    if doc.mime_type == 'text/plain':
        # convert_to_pdf(message, file_to_convert)
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Заебись!')
    if doc.mime_type == 'application/pdf':
        pass
        # pdf = text_pdf_from_txt(file_to_convert)
        # send_pdf_file(message, pdf)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Иди на хуй!')


commands = [
    ('start', start),
]

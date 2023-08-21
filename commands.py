import tempfile

import pdftotext
import requests
from telegram import Update
from telegram.ext import ContextTypes


def text_pdf_from_txt(content):
    """Сохраняет загруженный файл как временный, из которого потом вытаскивается текст."""
    with tempfile.NamedTemporaryFile(suffix=".txt") as temp_file_to_convert:
        temp_file_to_convert.write(content)
        temp_file_to_convert.seek(0)
        return pdftotext.PDF(temp_file_to_convert)


async def send_pdf_file(pdf, update, context):
    with tempfile.NamedTemporaryFile(mode="a+", suffix=".txt") as temp_pdf_file:
        for page in pdf:
            temp_pdf_file.write(page)
        temp_pdf_file.seek(0)
        await context.bot.send_document(
            chat_id=update.effective_chat.id, document=temp_pdf_file
        )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    resp = (
        "/start - информация о боте\nБот конвертирует файлы PDF в формат txt\n"
        "Отправъте файл PDF в сообщении для конвертации в формат txt"
    )
    await context.bot.send_message(chat_id=update.effective_chat.id, text=resp)


async def hand_pdf_to_txt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    doc = update.effective_message.document
    front_file = await doc.get_file()
    file_content = requests.get(front_file.file_path).content
    pdf = text_pdf_from_txt(file_content)
    await send_pdf_file(pdf, update, context)


commands = [
    ("start", start),
]

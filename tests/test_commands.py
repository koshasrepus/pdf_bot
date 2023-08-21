import unittest
from unittest import IsolatedAsyncioTestCase
from unittest.mock import AsyncMock, Mock

from commands import start


class Test(IsolatedAsyncioTestCase):
    async def test_start_command_can_sent_answer(self):
        update = Mock()
        update.effective_chat.id = 1

        context = AsyncMock()
        await start(update, context)

        self.assertEqual(
            context.bot.send_message.assert_awaited_once_with(
                chat_id=1,
                text="/start - информация о боте\n"
                "Бот конвертирует файлы PDF в"
                " формат txt\nОтправъте файл "
                "PDF в сообщении для конвертац"
                "ии в формат txt",
            ),
            None,
        )


if __name__ == "__main__":
    unittest.main()

from telebot.settings import app_settings as appset
from aiogram import Bot, Dispatcher, F
import logging
import asyncio
from telebot.handlers.main_handlers import get_start, get_answer
from aiogram.filters import Command
from telebot.keyboard.inline_keyboard_handlers import get_sex
from telebot.utils.states import States


async def start_bot(bot: Bot):
    await bot.send_message(appset.telegram_chat_id, 'Bot started!')


async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=appset.telegram_bot_token, parse_mode='HTML')
    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.message.register(get_start, Command(commands='start'))
    dp.callback_query.register(get_sex, F.data == 'man', F.data == 'woman')
    # dp.callback_query.register(get_sex, F.data == 'woman')
    dp.message.register(get_answer, States.size)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())

from telebot.settings import app_settings as appset
from aiogram import Bot, Dispatcher, F
import logging
import asyncio
from aiogram.filters import Command
from telebot.handlers.main_handlers import get_start
from telebot.handlers.callback import get_files, download_file, get_back


async def start_bot(bot: Bot):
    await bot.send_message(appset.telegram_chat_id, 'Bot started!')


async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=appset.telegram_bot_token, parse_mode='HTML')
    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.message.register(get_start, Command(commands=['start']))
    dp.callback_query.register(get_back, F.data.contains('back'))
    dp.callback_query.register(get_files, F.data.startswith('folder_'))
    dp.callback_query.register(download_file, F.data.startswith('file_'))
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())

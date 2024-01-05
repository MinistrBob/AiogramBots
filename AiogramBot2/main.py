from aiogram import Bot, Dispatcher, F
import asyncio
import logging
from telebot.handlers.basic import get_start, get_list, get_search, search_message
from aiogram.filters import Command
from settings import app_settings as appset
from telebot.utils.commands import set_commands
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(appset.telegram_chat_id, 'Bot started!')


async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=appset.telegram_bot_token, parse_mode='HTML')
    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.message.register(get_start, Command(commands=['start', 'run']))
    dp.message.register(get_list, Command(commands=['list']))
    dp.message.register(search_message, Command(commands=['search']))
    dp.message.register(get_search, F.text.startswith('Поиск:'))
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())

from telebot.settings import app_settings as appset
from aiogram import Bot, Dispatcher, F
import logging
import asyncio
from telebot.handlers.main_handlers import get_start
from aiogram.filters import Command
from telebot.handlers.inline_keyboard_handler import get_yes, get_no
import psycopg2


async def start():
    logging.basicConfig(level=logging.INFO)
    conn = None
    try:
        conn = psycopg2.connect(dbname=appset.postgres_dbname,
                                user=appset.postgres_user,
                                password=appset.postgres_password,
                                host=appset.postgres_host)
    except Exception as e:
        print(f"[ERROR]: Не могу соединится с БД:\n{e}")
    if not conn:
        raise Exception("Нет соединения с БД")
    bot = Bot(token=appset.telegram_bot_token, parse_mode='HTML')
    dp = Dispatcher()
    dp['conn'] = conn
    dp.message.register(get_start, Command(commands='start'))
    dp.callback_query.register(get_yes, F.data == 'yes')
    dp.callback_query.register(get_no, F.data == 'no')
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())

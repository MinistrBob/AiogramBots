from telebot.settings import app_settings as appset
from aiogram import Bot, Dispatcher, F
import logging
import asyncio
from telebot.handlers.main_handlers import get_start, get_answer
from aiogram.filters import Command
from telebot.keyboard.inline_keyboard_handlers import get_sex
from telebot.utils.states import States
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from telebot.handlers.apshed import send_message_time
from datetime import datetime, timedelta
from telebot.middlewares.apshedulermiddleware import SchedulerMiddleware


async def start_bot(bot: Bot):
    await bot.send_message(appset.telegram_chat_id, 'Bot started!')


async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=appset.telegram_bot_token, parse_mode='HTML')
    dp = Dispatcher()
    scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
    scheduler.add_job(send_message_time,
                      trigger='date',
                      run_date=datetime.now() + timedelta(seconds=3),
                      kwargs={'bot': bot})
    scheduler.start()
    dp.update.middleware.register(SchedulerMiddleware(scheduler))
    dp.startup.register(start_bot)
    dp.message.register(get_start, Command(commands='start'))
    dp.callback_query.register(get_sex, F.data == 'man')
    dp.callback_query.register(get_sex, F.data == 'woman')
    dp.callback_query.register(get_sex, F.data == 'middle')
    # dp.callback_query.register(get_sex, F.data == 'woman')
    dp.message.register(get_answer, States.size)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())

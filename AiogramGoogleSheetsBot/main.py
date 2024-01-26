from telebot.settings import app_settings as appset
from aiogram import Bot, Dispatcher, F
import logging
import asyncio
from telebot.handlers.main_handlers import get_on, get_off
from telebot.keyboards.replay import reply_keyboard_on


async def start_bot(bot: Bot):
    await bot.send_message(appset.telegram_chat_id, 'Bot started!', reply_markup=reply_keyboard_on)


async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=appset.telegram_bot_token, parse_mode='HTML')
    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.message.register(get_on, F.text == 'Включить')
    dp.message.register(get_off, F.text == 'Выключить')
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())

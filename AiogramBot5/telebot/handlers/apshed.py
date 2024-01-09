from aiogram import Bot
from telebot.keyboard.inline_keyboards import get_inline_keyboard3
from aiogram.types import CallbackQuery
from telebot.settings import app_settings as appset


async def send_message_time(bot: Bot):
    await bot.send_message(appset.telegram_chat_id, 'Сообщение через 3 сек. после старта бота')


async def send_message_middleware(answer: CallbackQuery):
    # await bot.send_message(appset.telegram_chat_id, 'Забыл предложить тебе выбрать третий пол', reply_markup=get_inline_keyboard3())
    await answer.message.answer('Забыл предложить тебе выбрать третий пол', reply_markup=get_inline_keyboard3())

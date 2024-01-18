from aiogram import Bot, Dispatcher
from aiogram.types import Message
from telebot.utils.parser3 import get_items


async def get_start(message: Message):
    result = await get_items()
    print(result)
    if result is None:
        await message.answer("Попробуйте ещё раз чуть позже")
    else:
        await message.answer(result, parse_mode="HTML")

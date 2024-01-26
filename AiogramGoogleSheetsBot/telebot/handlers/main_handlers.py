from aiogram import Bot, Dispatcher
from aiogram.types import Message
from telebot.keyboards.replay import reply_keyboard_on, reply_keyboard_off


async def get_on(message: Message):
    await message.answer("Бот включен", reply_markup=reply_keyboard_off)


async def get_off(message: Message):
    await message.answer("Бот выключен", reply_markup=reply_keyboard_on)

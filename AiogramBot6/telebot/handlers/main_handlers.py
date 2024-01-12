from aiogram import Bot, Dispatcher
from aiogram.types import Message
from telebot.keyboard.inline_keyboards import get_folder_keyboard


async def get_start(message: Message):
    await message.answer('Это бот Explorer.\nНиже ты увидишь кнопки с названиями папок и файлов.\nТы можешь '
                         'перемещаться по папкам и получить любой файл."', reply_markup=get_folder_keyboard())

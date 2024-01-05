from aiogram import Bot, Dispatcher
from aiogram.types import Message
import asyncio
import json
from core.keyboards.reply import reply_keyboard, loc_tel_poll_keyboard
from core.keyboards.inline import select_macbook, get_inline_keyboard


async def get_inline(message: Message, bot: Bot):
    await message.answer(f"Привет, {message.from_user.first_name} инлайн клава",
                         reply_markup=get_inline_keyboard())


async def get_start(message: Message, bot: Bot):
    # await bot.send_message(message.from_user.id, '<b>Hello1</b>, ' + message.from_user.first_name)
    # await message.answer('<s>Hello2</s>, ' + message.from_user.first_name)
    # await message.reply('<tg-spoiler>Hello3</tg-spoiler>, ' + message.from_user.first_name,
    #                     parse_mode='HTML')  # tg-spoilerHello3, ' + message.from_user.first_name)
    await message.answer(f'<s>Привет {message.from_user.first_name}. Рад тебя видеть!</s>',
                         reply_markup=loc_tel_poll_keyboard)


async def get_location(message: Message, bot: Bot):
    await message.answer(f"Ты отправил локацию\r\n"
                         f"{message.location.latitude}\r\n{message.location.longitude}")


async def get_photo(message: Message, bot: Bot):
    await message.answer("Cool! It's photo")
    file = await bot.get_file(message.photo[-1].file_id)
    file_path = file.file_path  # 'photos/file_2.jpg'
    print(file_path)
    file_name = file_path.split('/')[-1] if '/' in file_path else file_path
    await bot.download_file(file.file_path, file_name)


async def get_hello(message: Message, bot: Bot):
    await message.answer("И тебе привет!")
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)


async def get_help(message: Message, bot: Bot):
    await message.answer("Документация по боту")


async def get_cancel(message: Message, bot: Bot):
    await message.answer("Всё отменяется")

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_keyboard_on = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Включить"),
    ],
], resize_keyboard=True, one_time_keyboard=True, selective=True)

reply_keyboard_off = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Выключить"),
    ],
], resize_keyboard=True, one_time_keyboard=True, selective=True)

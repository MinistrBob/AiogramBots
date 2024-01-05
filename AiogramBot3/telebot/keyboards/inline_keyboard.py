# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="ДА", callback_data="yes")
    keyboard_builder.button(text="НЕТ", callback_data="no")
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()

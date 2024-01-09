# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="МУЖ", callback_data="man")
    keyboard_builder.button(text="ЖЕН", callback_data="woman")
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()


def get_inline_keyboard3():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="МУЖ", callback_data="man")
    keyboard_builder.button(text="СРЕДНИЙ", callback_data="middle")
    keyboard_builder.button(text="ЖЕН", callback_data="woman")
    keyboard_builder.adjust(3)
    return keyboard_builder.as_markup()

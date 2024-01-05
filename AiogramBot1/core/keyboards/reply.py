from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Ряд 1. Кнопка 1"),
        KeyboardButton(text="Ряд 1. Кнопка 2"),
        KeyboardButton(text="Ряд 1. Кнопка 3"),
    ],
    [
        KeyboardButton(text="Ряд 2. Кнопка 1"),
        KeyboardButton(text="Ряд 2. Кнопка 2"),
        KeyboardButton(text="Ряд 2. Кнопка 3"),
        KeyboardButton(text="Ряд 2. Кнопка 4"),
    ],
    [
        KeyboardButton(text="Ряд 3. Кнопка 1"),
        KeyboardButton(text="Ряд 3. Кнопка 2"),
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите пункт", selective=True)

loc_tel_poll_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Отправь геолокацию", required_location=True),
    ],
    [
        KeyboardButton(text="Отправь свой контакт", request_contact=True),
    ],
    [
        KeyboardButton(text="Создать викторину", request_poll=KeyboardButtonPollType(type="quiz")),
    ]
], resize_keyboard=True, one_time_keyboard=False, input_field_placeholder="Отправь локацию, номер телефона или создай викторину", selective=True)

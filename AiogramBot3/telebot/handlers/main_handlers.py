from aiogram import Bot, Dispatcher
from aiogram.types import Message
from telebot.keyboards.inline_keyboard import get_inline_keyboard


async def get_start(message: Message, conn):
    user = None
    try:
        with conn.cursor() as cursor:
            # list of users from table users
            print(f"Проверка пользователя {message.from_user.id} на участие в розыгрыше")
            sql_text = """SELECT * FROM users where chat_id = %s"""
            values_tuple = (message.from_user.id, )
            print(cursor.mogrify(sql_text, values_tuple))
            cursor.execute(sql_text, values_tuple)
            user = cursor.fetchone()
        # Если пользователя не участвовал в розыгрыше, то предлагаем ему розыгрыш.
        if not user:
            await message.answer("""Привет! Это беспроигрышное «Колесо фортуны» by PIMS👾💙
            Забрать подарок может только владелец карты PIMS. У тебя есть карта?""", reply_markup=get_inline_keyboard())
        else:
            await message.answer("""Привет! Рады тебя видеть. Ты уже участвовал в розыгрыше.""")
    except Exception as e:
        print(f"[ERROR]: {e}")


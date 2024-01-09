from aiogram import Bot, Dispatcher
from aiogram.types import Message
from telebot.keyboard.inline_keyboards import get_inline_keyboard
from telebot.utils.states import States
from aiogram.fsm.context import FSMContext


async def get_start(message: Message, state: FSMContext):
    print("get_start")
    await message.answer(f"Привет {message.from_user.full_name}! Введи свой пол.", reply_markup=get_inline_keyboard())
    await state.set_state(States.sex)


async def get_answer(message: Message, state: FSMContext):
    print("get_answer")
    await message.answer(f"Ты ввёл размер: {message.text}")
    if message.text.isdigit():
        size = int(message.text)
        await state.update_data(size=size)
    else:
        await message.answer(f"Для ввода размера используйте только числа!")
        return
    context_data = await state.get_data()
    # print(type(context_data['size']), context_data['size'])
    await message.answer(f"Данные: {str(context_data)}")
    if context_data['sex'] == "man" and context_data['size'] >= 18:
        await message.answer(f"Ты богатырь!")
    elif context_data['sex'] == "man" and context_data['size'] < 18:
        await message.answer(f"Тебе есть куда расти!")
    elif context_data['sex'] == "woman" and context_data['size'] >= 3:
        await message.answer(f"Ты красотка!")
    elif context_data['sex'] == "woman" and context_data['size'] < 3:
        await message.answer(f"Тебе нужно больше кушать капусты!")
    await state.clear()

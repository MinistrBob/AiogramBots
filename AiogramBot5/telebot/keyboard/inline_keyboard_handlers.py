from aiogram import Bot
from aiogram.types import CallbackQuery
from telebot.utils.states import States
from aiogram.fsm.context import FSMContext


async def get_sex(answer: CallbackQuery, bot: Bot, state: FSMContext):
    print("get_sex")
    print(answer.message.text)
    print(answer)
    print(answer.data)
    await answer.answer()
    await answer.message.answer(f"Твой пол {answer.data}?")
    await state.update_data(sex=answer.data)
    if answer.data == "man":
        await answer.message.answer(f"Какого размера твой член?")
    else:
        await answer.message.answer(f"Какой размер твой груди?")
    await state.set_state(States.size)


async def get_woman(answer: CallbackQuery, bot: Bot, state: FSMContext):
    await answer.answer()
    await answer.message.answer(f"Твой пол {answer.message.text}?")
    await answer.message.answer(f"Какой размер твоей груди?")
    await state.set_state(States.size)

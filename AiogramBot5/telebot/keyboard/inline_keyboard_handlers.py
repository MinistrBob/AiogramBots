from aiogram import Bot
from aiogram.types import CallbackQuery
from telebot.utils.states import States
from aiogram.fsm.context import FSMContext
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from telebot.handlers.apshed import send_message_middleware
from datetime import datetime, timedelta


async def get_sex(answer: CallbackQuery, bot: Bot, state: FSMContext, apscheduler: AsyncIOScheduler):
    print("get_sex")
    print(answer.message.text)
    print(answer)
    print(answer.data)
    await answer.answer()
    await answer.message.answer(f"Твой пол {answer.data}?")
    await state.update_data(sex=answer.data)
    if answer.data == "man":
        await answer.message.answer(f"Какого размера твой член?")
    elif answer.data == "woman":
        await answer.message.answer(f"Какой размер твой груди?")
    elif answer.data == "middle":
        await answer.message.answer(f"Какой размер твоей головы?")
    await state.set_state(States.size)
    if not answer.data == "middle":
        apscheduler.add_job(send_message_middleware,
                            trigger='date',
                            run_date=datetime.now() + timedelta(seconds=10),
                            kwargs={'answer': answer})

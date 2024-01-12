import os
from aiogram import Bot, Dispatcher
from aiogram.types import CallbackQuery, FSInputFile
from telebot.keyboard.inline_keyboards import get_files_keyboard, get_folder_keyboard
from telebot.settings import app_settings as appset
from aiogram.utils.chat_action import ChatActionSender


async def get_back(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=get_folder_keyboard())


async def get_files(callback: CallbackQuery):
    # print(callback.message)
    folder_name = callback.data.split('_')[1]
    # await callback.message.answer('Это бот Explorer.\nНиже ты увидишь кнопки с названиями папок и файлов.\nТы можешь '
    #                               'перемещаться по папкам и получить любой файл."',
    #                               reply_markup=get_files_keyboard(folder_name))
    await callback.answer()
    await callback.message.edit_reply_markup(reply_markup=get_files_keyboard(folder_name))


async def download_file(callback: CallbackQuery, bot: Bot):
    # print(callback.message)
    data = callback.data.split('_')
    file_path = os.path.join(appset.storage_path, data[1], data[2])
    match data[1]:
        case 'AudioFiles':
            audio_file = FSInputFile(file_path, filename=data[2])
            # await callback.message.reply_audio(audio_file)
            await bot.send_audio(chat_id=callback.message.chat.id, audio=audio_file)
        case 'VideoFiles':
            async with ChatActionSender.upload_video(chat_id=callback.message.chat.id, bot=bot):
                video_file = FSInputFile(file_path, filename=data[2])
                # await callback.message.reply_audio(video_file)
                await bot.send_video(chat_id=callback.message.chat.id, video=video_file)
        case 'PdfFiles':
            pdf_file = FSInputFile(file_path, filename=data[2])
            # await callback.message.reply_document(pdf_file)
            await bot.send_document(chat_id=callback.message.chat.id, document=pdf_file,
                                    disable_content_type_detection=True)
        case 'PhotoFiles':
            photo_file = FSInputFile(file_path, filename=data[2])
            # await callback.message.reply_photo(photo_file)
            await bot.send_photo(chat_id=callback.message.chat.id, photo=photo_file)
        case _:
            await callback.message.edit_reply_markup(reply_markup=get_files_keyboard(data[1]))
    # await callback.message.answer(f"Download file: {file_path}")
    await callback.answer()

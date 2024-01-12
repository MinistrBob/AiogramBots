import os
from aiogram.utils.keyboard import InlineKeyboardBuilder
from telebot.settings import app_settings as appset


def get_folder_keyboard():
    # print("get_folder_keyboard")
    keyboard_builder = InlineKeyboardBuilder()
    # walk through all files in the directory appset.storage_path
    if os.path.exists(appset.storage_path):
        for root, dirs, files in os.walk(appset.storage_path):
            # print(root, dirs, files)
            for folder in dirs:
                # print(folder)
                keyboard_builder.button(text=f"📁 {folder}", callback_data=f"folder_{folder}")
            # for file in files:
            #     file_path = os.path.join(root, file)
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup(resize_keyboard=True)


def get_files_keyboard(folder_name):
    # print("get_files_keyboard")
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text=f"⬅ НАЗАД", callback_data=f"back")
    # walk through all files in the directory appset.storage_path
    if os.path.exists(appset.storage_path):
        for root, dirs, files in os.walk(str(os.path.join(appset.storage_path, folder_name))):
            # print(root, dirs, files)
            # for folder in dirs:
            #     print(folder)
            #     keyboard_builder.button(text=f"📁 {folder}", callback_data=f"folder_{folder}")
            for file in files:
                # print(file)
                file_path = os.path.join(root, file)
                # print(file_path)
                keyboard_builder.button(text=f"● {file}", callback_data=f"file_{folder_name}_{file}")
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup(resize_keyboard=True)

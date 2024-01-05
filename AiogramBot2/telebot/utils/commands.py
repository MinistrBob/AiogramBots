from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Начало работы"),
        BotCommand(command="list", description="Список пользователей"),
        BotCommand(command="search", description="Поиск пользователя по фамилии"),
    ]
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())

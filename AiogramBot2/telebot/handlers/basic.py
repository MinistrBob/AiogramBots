from aiogram import Bot, Dispatcher
from aiogram.types import Message
import asyncio
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from settings import app_settings as appset


async def get_start(message: Message, bot: Bot, ):
    # await bot.send_message(message.from_user.id, '<b>Hello1</b>, ' + message.from_user.first_name)
    # await message.answer('<s>Hello2</s>, ' + message.from_user.first_name)
    # await message.reply('<tg-spoiler>Hello3</tg-spoiler>, ' + message.from_user.first_name,
    #                     parse_mode='HTML')  # tg-spoilerHello3, ' + message.from_user.first_name)
    conn = psycopg2.connect(dbname=appset.postgres_dbname,
                            user=appset.postgres_user,
                            password=appset.postgres_password,
                            host=appset.postgres_host)

    try:
        # Create the table (if not exists)
        with conn.cursor() as cursor:
            print(f"Создание таблицы users")
            cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                              id serial PRIMARY KEY,
                              chat_id bigint, 
                              first_name varchar(50), 
                              last_name varchar(50))""")
            conn.commit()
            print(f"Таблица users создана")
    except Exception as e:
        print(f"[ERROR]: {e}")
    await message.answer(f'Привет {message.from_user.first_name}. Рад тебя видеть! Занесу тебя в таблицу')
    try:
        # Create the table (if not exists)
        with conn.cursor() as cursor:
            print(f"Создание таблицы users")
            cursor.execute("""INSERT INTO users (chat_id, first_name, last_name) VALUES (%s, %s, %s) RETURNING id;""",
                           (message.from_user.id, message.from_user.first_name, message.from_user.last_name))
            user_id = cursor.fetchone()[0]
            conn.commit()
            await message.answer(f'Добавил тебя с id {user_id}')
    except psycopg2.errors.UniqueViolation as e:
        print(f"[ERROR]: Такой пользователь уже есть")


async def get_list(message: Message, bot: Bot, ):
    conn = psycopg2.connect(dbname=appset.postgres_dbname,
                            user=appset.postgres_user,
                            password=appset.postgres_password,
                            host=appset.postgres_host)
    try:
        # Create the table (if not exists)
        with conn.cursor() as cursor:
            # list of users from table users
            cursor.execute("""SELECT * FROM users""")
            rows = cursor.fetchall()
            text = '<code>'
            for row in rows:
                text = text + f"Id: {row[0]} Chat_id: {row[1]} First_name: {row[2]} Last_name: {row[3]}\n"
            text = text + '</code>'
            await message.answer(text, parse_mode='HTML')
    except Exception as e:
        print(f"[ERROR]: {e}")


async def search_message(message: Message, bot: Bot, ):
    await message.reply(f'Для поиска по фамилии введите "Поиск: Фамилия"')


async def get_search(message: Message, bot: Bot, ):
    conn = psycopg2.connect(dbname=appset.postgres_dbname,
                            user=appset.postgres_user,
                            password=appset.postgres_password,
                            host=appset.postgres_host)
    last_name = message.text.split(':')[1].strip()
    print(last_name)

    # Search for users with the given last name
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE last_name ILIKE %s", (f"%{last_name}%",))
        search_results = cursor.fetchall()

    # Send the search results to the chat
    if search_results:
        results_text = "\n".join(f"{result[0]} {result[1]} {result[2]} {result[3]}" for result in search_results)
        results_text = f"<code>{results_text}</code>"
        await message.reply(f"Search results for '{last_name}':\n{results_text}", parse_mode='HTML')
    else:
        await message.reply(f"No results found for '{last_name}'.")

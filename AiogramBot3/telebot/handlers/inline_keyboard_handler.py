from aiogram import Bot
from aiogram.types import CallbackQuery
import random
import psycopg2


async def get_yes(answer: CallbackQuery, bot: Bot, conn):
    key = random.choice(list(gifts_list.keys()))
    await answer.answer()
    await answer.message.answer(
        f"И вы получаете приз...\n\n<b>{key}</b>\n{gifts_list[key]}\n\n"
        f"*чтобы забрать подарок напиши нам в чат @pims_tea")
    try:
        # Create the table (if not exists)
        with conn.cursor() as cursor:
            print(
                f"Добавление пользователя {answer.message.chat.id}|"
                f"{answer.message.chat.first_name}|"
                f"{answer.message.chat.last_name} в таблицу users")
            sql_text = """INSERT INTO users (chat_id, first_name, last_name) VALUES (%s, %s, %s) RETURNING id;"""
            values_tuple = (answer.message.chat.id,
                            answer.message.chat.first_name,
                            answer.message.chat.last_name)
            print(cursor.mogrify(sql_text, values_tuple))
            cursor.execute(sql_text, values_tuple)
            _id = cursor.fetchone()[0]
            conn.commit()
            print(f'Пользователь добавлен с id {_id}')
    except psycopg2.errors.UniqueViolation as e:
        print(f"[ERROR]: Такой пользователь уже есть")


async def get_no(answer: CallbackQuery, bot: Bot):
    await answer.message.answer("Регистрируй и <a href='https://www.google.com/'>добавляй</a> в wallet👛")
    await answer.answer()


gifts_list = {
    "Тапиока": "Всем тапиока! Забирай тапиоку до конца года в подарок!",
    "Повышенный кэшбек": "Пей все напитки с двойным кэшбеком до конца года!",
    "Мерч Твинби": "Пока кто-то ищет любовь на улицах больших городов, мы нашли её на Twinby💙 Дарим мерч, "
                   "который притягивает дружбу и любовь!",
    "Молоко": "Кокосовое молоко – это больше не на богатом. Пей PIMS на любом молоке до конца года без доплат!",
    "Настя Галакс": "Лови любимый PIMS Насти Галакс Berries x Berries с двойным кэшбеком до конца года🔥",
    "Роза Фест": "Psss...откроем тебе секрет! Мы создали лимитированный напиток для РозаФест, и ты его попробуешь "
                 "первым! Покупай билеты и собирай вещи, мы дарим тебе проходку на РозаФест в Сочи!🏔️",
    "Таша": "Устал листать пинтерест для поиска идеальной заставки на телефон? Мы с Ташей создали идеальные "
            "волпейперы сезона, <a href='https://drive.google.com/drive/folders/1aPlpbBHs5bueJSCiGdxDpCIQE9RVHvp4?usp"
            "=sharing'>забирай</a>",
    "Sortage": "«Стильно, модно, молодёжно» – это твой подарок. С этого дня твоё второе имя – фэшн. Наш подарок для "
               "тебя шмот от OMANKO😱",
    "На шуме": "Вас посетила полиция музыкального вкуса, в этот раз обойдёмся предупреждением! И дарим <a "
               "href='https://music.apple.com/ru/playlist/%D0%BD%D0%B0-%D1%88%D1%83%D0%BC%D0%B5-%D0%B4%D0%BB%D1%8F"
               "-pims/pl.u-Zmblx9rU0Ao1dbg'>музыкальную подборку</a> НАШУМЕ🎧",
}

if __name__ == "__main__":
    # print(random.randint(0, 8))

    key = random.choice(list(gifts_list.keys()))
    print(key, gifts_list[key])

import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from allKeyboards import auth, gender, mebel, cosmetics, animals, toys, men_clothes, \
    women_clothes
from allStates import StartWork, MainMenu

dp = Dispatcher()
TOKEN = '7082511023:AAErpzdNuLsweduo_c-Ss_sbRDUtCQvnlms'
# Флаг для отслеживания состояния пользователя
writing_review = {}


@dp.message(F.photo)
async def photo_handler(
        message: Message) -> None:  # функция для получения id файла, чтобы бот отправлял файлы
    photo_data = message.photo[-1]
    await message.answer(f'{photo_data}')


@dp.message(Command("start"), F.from_user)
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await message.answer(
        f"Привет, {message.from_user.username}. Это бот-каталог магазина. Вы можете выбрать раздел, чтобы просмотреть необходимые товары и цены на них, а также оставить отзыв либо просмотреть их.",
        reply_markup=auth().as_markup(resize_keyboard=True, one_time_keyboard=True))
    await state.set_state(StartWork.start_work)


@dp.message(StartWork.start_work, F.text == "Одежда")
async def clothes(message: types.Message, state: FSMContext) -> None:
    await message.answer("Выберите какая одежда",
                         reply_markup=gender().as_markup(resize_keyboard=True,
                                                         one_time_keyboard=True),
                         )
    await state.set_state(MainMenu.main_menu)


@dp.message(F.text == "Мужская")
async def clothes(message: types.Message) -> None:
    await message.answer("Выберите тип одежды",
                         reply_markup=men_clothes().as_markup(resize_keyboard=True,
                                                              one_time_keyboard=True),
                         )


@dp.message(F.text == "Футболки, толстовки")
async def clothes(message: types.Message) -> None:
    await message.answer("Цветная футболка, 1000р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAICeWYf6OzB0XkOjHd_hvuaK5KX7LJFAAJ22zEbz8QBScLFajYKyCHjAQADAgADeQADNAQ')

    await message.answer("Футболка с воротником, 1000р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAICe2Yf6SK5tQa8rDD8vGC7nBEVssH4AAJ32zEbz8QBSeskopuhKdbkAQADAgADeAADNAQ')

    await message.answer("Толстовка, 3000р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAICfWYf6Vyophjjwi8ExL4C20YX0suBAAJ82zEbz8QBSXQNfJ_OrTC0AQADAgADeAADNAQ')


@dp.message(F.text == "Штаны, шорты")
async def clothes(message: types.Message) -> None:
    await message.answer("Шорты, 2000р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAICw2Yf6qrKupruKQqCoLq2tqZvhstZAAKB2zEbz8QBSa_fy3-4AAFVUAEAAwIAA3kAAzQE')
    await message.answer("Красные шорты NIKE, 2000р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAICIWYf40YDNCXW16K8U3JxsEEXnnADAAJI2zEbz8QBSfW114pipCGaAQADAgADeQADNAQ')

    await message.answer("Штаны, 5000р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAICv2Yf6mSXkd7v6ERi0sF5qrqBbmcJAAKA2zEbz8QBSY8LSRRR-cuvAQADAgADeAADNAQ')



@dp.message(F.text == "Обувь")
async def clothes(message: types.Message) -> None:
    await message.answer("Кроссовки SPORT, 2999р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAICxWYf6tl6NINQfRUXWgtA9kUr2MdmAAKD2zEbz8QBScXCi_a1ZsskAQADAgADeAADNAQ')

    await message.answer("Коричневые осенние ботинки, 4999р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAICKWYf46klbsx85e5URWqyFfUsqEZjAAJO2zEbz8QBSTG7d5_PLX_qAQADAgADeAADNAQ')

    await message.answer("Тапочки BALENCIAGA, 99990р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAICK2Yf48auuGU_n1DjKFdmljg_Aey6AAJQ2zEbz8QBSThIiGH_Mi26AQADAgADeAADNAQ')


@dp.message(F.text == "Женская")
async def clothes(message: types.Message) -> None:
    await message.answer("Выберите тип одежды",
                         reply_markup=women_clothes().as_markup(resize_keyboard=True,
                                                                one_time_keyboard=True),
                         )


@dp.message(F.text == "Блузки, толстовки")
async def clothes(message: types.Message) -> None:
    await message.answer("Цветная футболка, 1000р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAICaWYf5mk1QtYJ28W_4xWbIGi0TJwlAAJk2zEbz8QBSTafRMhCQD6UAQADAgADeAADNAQ')

    await message.answer("Цветная блузка, 1499р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAICa2Yf5skNfq6FvZnBOohkRuTuQScoAAJm2zEbz8QBSTwMLcbXX9t9AQADAgADeAADNAQ')

    await message.answer("Толстовка, 1999р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAICcWYf5zsouRsG43uZDSvhAiCjvUhsAAJp2zEbz8QBSeow9kAw-X83AQADAgADeQADNAQ')


@dp.message(F.text == "Брюки, шорты, юбки")
async def clothes(message: types.Message) -> None:
    await message.answer("Брюки женские, 2999р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAICY2Yf5dlmw5QFBKaTwKMVsIThU6VVAAJe2zEbz8QBScGtG_M-beMzAQADAgADeAADNAQ')

    await message.answer("Шорты женские, 499р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAICZWYf5hswDC-WiizvtcC3U0fFzVSmAAJh2zEbz8QBSaTXx1o_HUAyAQADAgADeAADNAQ')

    await message.answer("Юбка с цветами, 1499р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAICZ2Yf5jVDcYb2W6j1AqJTwQYWUBhiAAJi2zEbz8QBSTaaYlxj99FLAQADAgADeAADNAQ')


@dp.message(F.text == "Туфли, кроссовки")
async def clothes(message: types.Message) -> None:
    await message.answer("Туфли, 2999р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAICc2Yf6Ep9WprobQt8bWGyXAJ98lALAAJx2zEbz8QBSW1n7F7bsimrAQADAgADeQADNAQ')

    await message.answer("Кроссовки NIKE, 4999р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAICdWYf6Hcx_2Lv5VPD9t4rwrYxSFnZAAJy2zEbz8QBSVzLtTPbmvw7AQADAgADeAADNAQ')

    await message.answer("Тапочки, 9999р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAICd2Yf6LXUAAGzReVrgkCDxCxdE5grHAACdNsxG8_EAUmTQuK2qApx1wEAAwIAA3gAAzQE')


@dp.message(StartWork.start_work, F.text == "Мебель")
async def clothes(message: types.Message, state: FSMContext) -> None:
    await message.answer("Выберите тип мебели",
                         reply_markup=mebel().as_markup(resize_keyboard=True,
                                                        one_time_keyboard=True),
                         )
    await state.set_state(MainMenu.main_menu)


@dp.message(F.text == "Кухонная мебель")
async def clothes(message: types.Message) -> None:
    await message.answer("Оранжевый гарнитур, 14999р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAICx2Yf6y9LuBfsmFwAAXG18BTHKImrqQAChNsxG8_EAUk-6jFQqYpWbwEAAwIAA3cAAzQE')

    await message.answer("Красный гарнитур, 19999р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAICyWYf6zmt0L1h5b6IEGQhAAGIMNeZ9QAChdsxG8_EAUkIyVzxUuqh_gEAAwIAA3kAAzQE')

    await message.answer("Розовый гарнитур, 24999р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAICy2Yf60Dvhk5nxsQz5JTKVel3wh3zAAKG2zEbz8QBSVQW7jJZt7SgAQADAgADeQADNAQ')


@dp.message(F.text == "Мебель в гостинную и спальню")
async def clothes(message: types.Message) -> None:
    await message.answer("Большой угловой диван, 34999р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAIC52Yf7DD7jzw8q4nr24-sSK4GtTv6AAKP2zEbz8QBSaysSQxJ3C-CAQADAgADeQADNAQ')

    await message.answer("Металлическая двухъярусная кровать, 29999р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAIC6WYf7F62c3ke2J8M4t32BSvuKZYmAAKQ2zEbz8QBSQ7x9UuNtDHQAQADAgADeAADNAQ')

    await message.answer("Встроенный шкаф, 24999р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAIC62Yf7J8CMwsxvgrR0_sHbA728dhzAAKT2zEbz8QBSYeP3auwbE-LAQADAgADdwADNAQ')


@dp.message(F.text == "Декор")
async def clothes(message: types.Message) -> None:
    await message.answer("Шкаф,прикроватная тумба и часы, 44999р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAIC7WYf7Ozly6dzuLbifP3AZhFGr-KMAAKV2zEbz8QBSdc_Lg5QNuFVAQADAgADeQADNAQ')

    await message.answer("Декор листья, 2999р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAIC72Yf7SLEZq-T5XEJ4DQwBiho4qhfAAKh2zEbz8QBSWjSC2j17BseAQADAgADeQADNAQ')

    await message.answer("Зеркало, 4999р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAIC8WYf7VvSte1Jw2zDazLdiPAHcIRpAAKk2zEbz8QBSSLXaUCGs_x3AQADAgADdwADNAQ')

    await message.answer("Столик, 99999р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAIDkGYf74_kcubuVso-1QwULA_9hE3LAAJF1jEba0sAAUmGDB6Fatv2kgEAAwIAA3gAAzQE')


@dp.message(StartWork.start_work, F.text == "Косметика")
async def clothes(message: types.Message, state: FSMContext) -> None:
    await message.answer("Выберите, какая косметика вас интересует",
                         reply_markup=cosmetics().as_markup(resize_keyboard=True,
                                                            one_time_keyboard=True),
                         )
    await state.set_state(MainMenu.main_menu)


@dp.message(F.text == "Уходовая косметика")
async def clothes(message: types.Message) -> None:
    await message.answer("Набор для ухода за лицом, 4999р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAIDwGYjvtVKD6NjVj6LuWsAAX9mlgnnIwACzdkxG6whIUn20wHxPgmOQwEAAwIAA3kAAzQE')

    await message.answer("Набор для ухода за волосами, 2999р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAIDwmYjvwuLjcHq7X5x81V5p2PKub3IAALO2TEbrCEhSbvSDMYsOMdxAQADAgADeQADNAQ')

    await message.answer("Увлажняющий набор для лица, 4999р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAIDxGYjvzBLEfYMlXlWILecpRXjpaT8AALP2TEbrCEhSRcROfj6fyw6AQADAgADeQADNAQ')


@dp.message(F.text == "Декоративная косметика")
async def clothes(message: types.Message) -> None:
    await message.answer("Палитра теней для век, 88 цветов, 999р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAIDxmYjv32KlhdrzB7csSJFTmXiPkobAALR2TEbrCEhSWG-JQ6xZb-qAQADAgADeAADNAQ')

    await message.answer("Объемная тушь для ресниц, 599р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAIDyGYjv7L5lTu2bEiQ7Qy44SwoDE5pAALS2TEbrCEhSUqZJ6F70zafAQADAgADeAADNAQ')

    await message.answer("Набор стойких помад, 1999р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAIDymYjv-YJnrOOW7vuIZr79rUuH35kAALT2TEbrCEhSQHs8kyJHoa4AQADAgADeQADNAQ')


@dp.message(StartWork.start_work, F.text == "Животные")
async def clothes(message: types.Message, state: FSMContext) -> None:
    await message.answer("Выберите, какие животные вас интересуют",
                         reply_markup=animals().as_markup(resize_keyboard=True,
                                                          one_time_keyboard=True),
                         )
    await state.set_state(MainMenu.main_menu)


@dp.message(F.text == "Кошки")
async def clothes(message: types.Message) -> None:
    await message.answer("Мейн-кун, 14999р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAID82YjwKjEVXKZ7agwPKOrKuZp1Y0vAALV2TEbrCEhSc-heAeKUkVqAQADAgADdwADNAQ')

    await message.answer("Тигр, 99999р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAID9WYjwPsQeDR-wk-1sIJFdnNZvqKJAALY2TEbrCEhSVxozz0b7SM3AQADAgADdwADNAQ')

    await message.answer("Вислоухая кошка, 4999р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAID92YjwTCzBX8rCCvo4hIXAT1S0CLZAALZ2TEbrCEhSXiHombnpVKZAQADAgADeAADNAQ')


@dp.message(F.text == "Собаки")
async def clothes(message: types.Message) -> None:
    await message.answer("Чихуахуа, 4999р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAID-WYjwVrDbSQnCj-fOc6TPCJlfqxmAALd2TEbrCEhSbpTvqywr8hdAQADAgADeQADNAQ')

    await message.answer("Овчарка, 23999р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAID-2YjwYNAXNcdzjH0TmqXRmtkOGkdAALf2TEbrCEhSfm15iZdED45AQADAgADeQADNAQ')

    await message.answer("Хаски, 14999р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAID_WYjwctJXsaUM9aXqfsHV8LgYXTdAALg2TEbrCEhSdPtHByX3N3wAQADAgADeQADNAQ')


@dp.message(StartWork.start_work, F.text == "Игрушки")
async def clothes(message: types.Message, state: FSMContext) -> None:
    await message.answer("Выберите, какие игрушки вас интересуют",
                         reply_markup=toys().as_markup(resize_keyboard=True,
                                                       one_time_keyboard=True),
                         )
    await state.set_state(MainMenu.main_menu)


@dp.message(F.text == "Мягкие игрушки")
async def clothes(message: types.Message) -> None:
    await message.answer("Плюшевый медведь, 499-4999р (в зависимости от размера)")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAID_2YjwfU1TcwrdV9ydTfYLNwHZhzbAALi2TEbrCEhSfjxuUU2yeZQAQADAgADeAADNAQ')

    await message.answer("Рюкзак-игрушка кролик, 1499р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAIEA2YjwmmkUTY6SeIOXv0rF8CVUvQOAALn2TEbrCEhSS0QBeIhwXRhAQADAgADeQADNAQ')

    await message.answer("Свинка, 799р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAIEBWYjwtZTOGwgRKkHjtew-0iB7yFSAALr2TEbrCEhSUqoSnfce44zAQADAgADdwADNAQ')


@dp.message(F.text == "Настольные игры")
async def clothes(message: types.Message) -> None:
    await message.answer("Игра Мафия, 499р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAIEB2Yjwvm0Psy7Op6qzz0UxT3v7bWAAALs2TEbrCEhSV_iSx7TCk3oAQADAgADdwADNAQ')

    await message.answer("Настольная игра Большая бродилка, 999р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAIEC2Yjw2_rIwKyXfmIQO2F1WAt6bhkAALy2TEbrCEhSarWKDG_5HFfAQADAgADeQADNAQ')

    await message.answer("Настольная игра Монополия, 1299р")
    await message.answer_photo(
        photo='AgACAgIAAxkBAAIECWYjwzvZ-eDqVAeLuanhtqVott-pAALu2TEbrCEhSc_ISRwDGOGIAQADAgADdwADNAQ')


@dp.message(MainMenu.main_menu, F.text == "Отмена")
async def back_menu(message: types.Message, state: FSMContext) -> None:
    await message.answer("Выберите раздел",
                         reply_markup=auth().as_markup(resize_keyboard=True,
                                                       one_time_keyboard=True))
    await state.set_state(StartWork.start_work)


@dp.message(F.text == "Написать отзыв")
async def clothes(message: types.Message) -> None:
    # Устанавливаем флаг, что пользователь начал писать отзыв
    writing_review[message.chat.id] = True
    await message.answer("Напишите ваш отзыв")


@dp.message(F.text == "Отзывы")
async def show_reviews(message: types.Message) -> None:
    # Читаем содержимое файла и отправляем его пользователю
    with open("reviews.txt", "r") as file:
        reviews = file.read()
    await message.answer(f"Вот все отзывы:\n{reviews}")


@dp.message()
async def process_message(message: types.Message) -> None:
    # Проверяем, начал ли пользователь писать отзыв
    if message.chat.id in writing_review and writing_review[message.chat.id]:
        # Сбрасываем флаг и выводим отзыв
        writing_review[message.chat.id] = False
        review_text = message.text
        # Записываем отзыв в файл
        with open("reviews.txt", "a") as file:
            file.write(review_text + "\n")
        await message.answer(f"Отзыв '{review_text}' сохранен")
    else:
        # Если пользователь пишет не во время написания отзыва, просто игнорируем сообщение
        pass


@dp.message()
async def echo(message: Message):
    await message.answer("Неизвестная команда")


async def main():
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

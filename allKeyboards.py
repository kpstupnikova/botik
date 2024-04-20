from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardBuilder


def auth() -> ReplyKeyboardBuilder:
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="Одежда"),
    )
    builder.row(
        KeyboardButton(text="Мебель")
    )
    builder.row(
        KeyboardButton(text="Косметика")
    )
    builder.row(
        KeyboardButton(text="Животные")
    )
    builder.row(
        KeyboardButton(text="Игрушки")
    )
    builder.row(
        KeyboardButton(text="Написать отзыв")
    )
    builder.row(
        KeyboardButton(text="Отзывы")
    )
    return builder


def gender() -> ReplyKeyboardBuilder:
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="Мужская"),
    )
    builder.row(
        KeyboardButton(text="Женская")
    )
    builder.row(
        KeyboardButton(text="Отмена")
    )
    return builder

def men_clothes() -> ReplyKeyboardBuilder:
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="Футболки, толстовки"),
    )
    builder.row(
        KeyboardButton(text="Штаны, шорты")
    )
    builder.row(
        KeyboardButton(text="Обувь")
    )
    builder.row(
        KeyboardButton(text="Отмена")
    )
    return builder
def women_clothes() -> ReplyKeyboardBuilder:
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="Блузки, толстовки"),
    )
    builder.row(
        KeyboardButton(text="Брюки, шорты, юбки")
    )
    builder.row(
        KeyboardButton(text="Туфли, кроссовки")
    )
    builder.row(
        KeyboardButton(text="Отмена")
    )
    return builder
def mebel() -> ReplyKeyboardBuilder:
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="Кухонная мебель"),
    )
    builder.row(
        KeyboardButton(text="Мебель в гостинную и спальню")
    )
    builder.row(
        KeyboardButton(text="Декор")
    )
    builder.row(
        KeyboardButton(text="Отмена")
    )
    return builder


def cosmetics() -> ReplyKeyboardBuilder:
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="Уходовая косметика"),
    )
    builder.row(
        KeyboardButton(text="Декоративная косметика")
    )
    builder.row(
        KeyboardButton(text="Отмена")
    )
    return builder


def animals() -> ReplyKeyboardBuilder:
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="Кошки"),
    )
    builder.row(
        KeyboardButton(text="Собаки")
    )
    builder.row(
        KeyboardButton(text="Отмена")
    )
    return builder


def toys() -> ReplyKeyboardBuilder:
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="Мягкие игрушки"),
    )
    builder.row(
        KeyboardButton(text="Настольные игры")
    )
    builder.row(
        KeyboardButton(text="Отмена")
    )
    return builder


class Keyboards:
    pass

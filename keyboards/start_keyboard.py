from aiogram.utils.keyboard import ReplyKeyboardBuilder

from config import (
    VOICES_MESSAGE,
    LAST_SELFIE_MESSAGE,
    SCHOOL_PHOTO_MESSAGE,
    SOURCES_MESSAGE,
    POST_MESSAGE,
)


def start_keyboard():
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text=VOICES_MESSAGE)
    keyboard.button(text=LAST_SELFIE_MESSAGE)
    keyboard.button(text=SCHOOL_PHOTO_MESSAGE)
    keyboard.button(text=SOURCES_MESSAGE)
    keyboard.button(text=POST_MESSAGE)
    keyboard.adjust(3, 2)
    return keyboard.as_markup(resize_keyboard=True)

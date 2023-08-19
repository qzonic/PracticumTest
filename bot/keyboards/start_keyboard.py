from aiogram.utils.keyboard import ReplyKeyboardBuilder

from bot import config


def start_keyboard():
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text=config.VOICES_MESSAGE)
    keyboard.button(text=config.LAST_SELFIE_MESSAGE)
    keyboard.button(text=config.SCHOOL_PHOTO_MESSAGE)
    keyboard.button(text=config.SOURCES_MESSAGE)
    keyboard.button(text=config.POST_MESSAGE)
    keyboard.adjust(3, 2)
    return keyboard.as_markup(resize_keyboard=True)

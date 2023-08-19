from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot import config
from bot.callback_data.voice_callback_data import VoiceCallBackData


def voices_keyboard():
    questions = {
        config.WHAT_IS_GPT_CALLBACK: config.WHAT_IS_GPT,
        config.DIFFERENCE_BETWEEN_SQL_NOSQL_CALLBACK: config.DIFFERENCE_BETWEEN_SQL_NOSQL,
        config.FIRST_LOVE_CALLBACK: config.FIRST_LOVE
    }
    keyboard = InlineKeyboardBuilder()
    for item in questions.items():
        keyboard.button(
            text=item[1],
            callback_data=VoiceCallBackData(
                question=item[0]
            )
        )
    keyboard.adjust(1, 1)
    return keyboard.as_markup()

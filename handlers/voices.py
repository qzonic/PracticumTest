from aiogram import types

import config
from callback_data.voice_callback_data import VoiceCallBackData
from keyboards.voices_keyboard import voices_keyboard


VOICES = {
    config.WHAT_IS_GPT_CALLBACK: config.WHAT_IS_GPT_VOICE_ID,
    config.DIFFERENCE_BETWEEN_SQL_NOSQL_CALLBACK: config.DIFFERENCE_BETWEEN_SQL_NOSQL_VOICE_ID,
    config.FIRST_LOVE_CALLBACK: config.FIRST_LOVE_VOICE_ID,
}


async def send_available_voices(message: types.Message):
    await message.answer('Доступные голосовые:', reply_markup=voices_keyboard())


async def send_voice(call: types.CallbackQuery, callback_data: VoiceCallBackData):
    await call.message.answer_voice(voice=VOICES[callback_data.question])

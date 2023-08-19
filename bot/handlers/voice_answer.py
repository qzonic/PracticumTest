from aiogram import types
from speech_recognition import UnknownValueError

from bot.config import RECOGNITION_ERROR, OPENAI_ANSWER
from bot.recognition.voice_recognition import AudioConverter


async def recognise_and_send_answer(message: types.Message):
    if message.content_type == types.ContentType.VOICE:
        voice_id = message.voice.file_unique_id
        file_path = f'voices/{voice_id}.ogg'
        try:
            audio_converter = AudioConverter(file_path)
            text = audio_converter.convert()
            await message.answer(OPENAI_ANSWER.format(text))
            response = audio_converter.openai_response(text)
            await message.answer(response)
            audio_converter.delete()
        except UnknownValueError:
            await message.answer(RECOGNITION_ERROR)


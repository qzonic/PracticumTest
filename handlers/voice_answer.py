from aiogram import types
from speech_recognition import UnknownValueError

from config import RECOGNITION_ERROR, OPENAI_ANSWER
from recognition.voice_recognition import AudioConverter


async def recognise_and_send_answer(message: types.Message):
    if message.content_type == types.ContentType.VOICE:
        voice_id = message.voice.file_unique_id
        file_path = f'{voice_id}.ogg'
        audio_converter = AudioConverter(file_path)
        try:
            text = audio_converter.convert()
            await message.answer(OPENAI_ANSWER.format(text))
            response = audio_converter.openai_response(text)
            await message.answer(response)
        except UnknownValueError:
            await message.answer(RECOGNITION_ERROR)
        finally:
            audio_converter.delete()


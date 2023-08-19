__all__ = ['register_user_commands']

from aiogram import Router, F
from aiogram.filters import Command, CommandStart

import config
from callback_data.voice_callback_data import VoiceCallBackData
from handlers.start import start
from handlers.help import help_command
from handlers.photos import last_selfie, school_photo
from handlers.post import send_post
from handlers.sources import sources
from handlers.voices import send_available_voices, send_voice
from middlewares.download_voice import DownloadVoiceMiddleware
from handlers.voice_answer import recognise_and_send_answer


def register_user_commands(router: Router) -> None:
    router.message.register(start, CommandStart())
    router.message.register(help_command, Command(commands=['help']))
    router.message.register(last_selfie, F.text == config.LAST_SELFIE_MESSAGE)
    router.message.register(school_photo, F.text == config.SCHOOL_PHOTO_MESSAGE)
    router.message.register(send_post, F.text == config.POST_MESSAGE)
    router.message.register(sources, F.text == config.SOURCES_MESSAGE)
    router.message.register(send_available_voices, F.text == config.VOICES_MESSAGE)

    router.callback_query.register(send_voice, VoiceCallBackData.filter())

    router.message.middleware(DownloadVoiceMiddleware())

    router.message.register(recognise_and_send_answer)

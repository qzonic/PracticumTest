from aiogram.filters.callback_data import CallbackData


class VoiceCallBackData(CallbackData, prefix='voices'):
    question: str

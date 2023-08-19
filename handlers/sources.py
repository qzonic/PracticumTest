from aiogram import types

from config import SOURCES_ANSWER


async def sources(message: types.Message):
    await message.answer(SOURCES_ANSWER, parse_mode='html', disable_web_page_preview=True)

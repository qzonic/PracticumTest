from aiogram import types

from config import LAST_SELFIE_URL, SCHOOL_PHOTO_URL


async def last_selfie(message: types.Message):
    await message.answer_photo(LAST_SELFIE_URL)


async def school_photo(message: types.Message):
    await message.answer_photo(SCHOOL_PHOTO_URL)

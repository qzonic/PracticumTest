from aiogram import types

from config import POST


async def send_post(message: types.Message):
    await message.answer(POST)

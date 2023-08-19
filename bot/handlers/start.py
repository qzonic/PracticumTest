from aiogram import types

from bot.config import START_MESSAGE
from bot.keyboards.start_keyboard import start_keyboard


async def start(message: types.Message):
    await message.answer(START_MESSAGE, reply_markup=start_keyboard())

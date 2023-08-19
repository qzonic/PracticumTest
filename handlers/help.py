from aiogram import types
from aiogram.filters import CommandObject

from config import COMMAND_INFO, HELP_COMMAND
from handlers.bot_commands import BOT_COMMANDS


async def help_command(message: types.Message, command: CommandObject):
    if command.args:
        if command.args in BOT_COMMANDS:
            return await message.answer(
                COMMAND_INFO.format(
                    command.args,
                    BOT_COMMANDS[command.args][0],
                    BOT_COMMANDS[command.args][1]
                )
            )
        else:
            return await message.answer('Команда не найдена')
    return await message.answer(HELP_COMMAND)

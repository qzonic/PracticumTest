from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message


class DownloadVoiceMiddleware(BaseMiddleware):

    def __init__(self):
        pass

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        if event.voice:
            file_info = await data['bot'].get_file(event.voice.file_id)
            voice_file_path = file_info.file_path
            file_path_ogg = f'{event.voice.file_unique_id}.ogg'
            await data['bot'].download_file(voice_file_path, file_path_ogg)
        return await handler(event, data)

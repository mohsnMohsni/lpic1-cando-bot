# Standard imports
import os

# Third-party imports.
from validators import url as url_validator
from pyrogram.client import Client
from pyrogram.filters import (
    group as filters_group,
    command as filters_command,
    private as filters_private,
)
from pyrogram.types.messages_and_media import Message

from .decorators import command_count_validator, command_validator
from .helpers import download_files_from_url
from .models.tables import CapturesVideo
from .constants import messages
from .supplier import app


@app.on_message(filters_private & filters_command('test_health'))
async def test_health(client: Client, message: Message) -> None:
    await message.reply(messages.HEALTH_PASS)


@app.on_message(filters_private & filters_command('add_capture'))
@command_count_validator(3)
@command_validator(2, url_validator, messages.NOT_VALID_URL)
async def add_capture_link(client: Client, message: Message) -> None:
    CapturesVideo.create_instance(capture_number=message.command[1], link=message.command[2])
    await message.reply(messages.CAPTURE_LINK_APPEND)


@app.on_message(filters_group & filters_command('capture'))
@command_count_validator(2)
async def get_capture_link(client: Client, message: Message) -> None:
    capture: CapturesVideo = CapturesVideo.filter_first(capture_number=message.command[1])
    message_instance: Message = await message.reply(messages.IS_SENDING)
    file_name: str = download_files_from_url(capture.link)
    await message.reply_document(
        caption=capture.link,
        document=file_name,
        force_document=True,
        quote=True,
    )
    await message_instance.delete()
    os.unlink(file_name)

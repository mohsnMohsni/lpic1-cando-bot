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

# Local imports with absolute path.
from .helpers import download_files_from_url
from .supplier import app
from .constants import messages
from .models.tables import CapturesVideo
from .validators.decorators import (
    test_health,
    command_validator,
    command_length_validator,
    retrieve_instance_and_instance_validator,
)


@app.on_message(filters_private & filters_command('test_health'))
@test_health()
async def test_health(client: Client, message: Message) -> None:
    await message.reply(messages.HEALTH_PASS)


@app.on_message(filters_private & filters_command('add_capture'))
@command_length_validator(3)
@command_validator(2, url_validator, messages.NOT_VALID_URL)
async def add_capture_link(client: Client, message: Message) -> None:
    CapturesVideo.create_instance(capture_number=message.command[1], link=message.command[2])
    await message.reply(messages.CAPTURE_LINK_APPEND)


@app.on_message(filters_group & filters_command('capture'))
@command_length_validator(2)
@retrieve_instance_and_instance_validator(CapturesVideo, 'capture_number', 1)
async def get_capture_link(client: Client, message: Message, model_instance: CapturesVideo) -> None:
    message_instance: Message = await message.reply(messages.IS_SENDING)
    file_name: str = download_files_from_url(model_instance.link)
    await message.reply_document(
        caption=model_instance.link,
        document=file_name,
        force_document=True,
        quote=True,
    )
    await message_instance.delete()
    os.unlink(file_name)

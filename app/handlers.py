# Standard imports
import os

# Third-party imports.
from validators import url as url_validator
from pyrogram.filters import (
    group as filters_group,
    command as filters_command,
    private as filters_private,
)

from .helpers import download_files_from_url
from .supplier import app
from .constants import messages
from .models.tables import CapturesVideo


@app.on_message(filters_private & filters_command('add_capture'))
async def add_capture_link(client, message):
    if not url_validator(message.command[2]):
        await message.reply(messages.NOT_VALID_URL)
        return
    CapturesVideo.create_instance(capture_number=message.command[1], link=message.command[2])
    await message.reply(messages.CAPTURE_LINK_APPEND)


@app.on_message(filters_group & filters_command('capture'))
async def get_capture_link(client, message):
    capture = CapturesVideo.filter_first(capture_number=message.command[1])
    message_instance = await message.reply(messages.IS_SENDING)
    file_name = download_files_from_url(capture.link)
    await message.reply_document(
        caption=capture.link,
        document=file_name,
        force_document=True,
        quote=True,
    )
    await message_instance.delete()
    os.unlink(file_name)

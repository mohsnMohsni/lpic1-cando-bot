# Standard imports
import os
from urllib.parse import urlparse
from urllib.request import urlretrieve

# Third-party imports.
from pyrogram.filters import command as filters_command

from .supplier import app
from .constants import messages
from .models.tables import CapturesVideo


@app.on_message(filters_command('add_capture'))
async def add_capture_link(client, message):
    CapturesVideo.create_instance(capture_number=message.command[1], link=message.command[2])
    await message.reply(messages.CAPTURE_LINK_APPEND)


@app.on_message(filters_command('capture'))
async def get_capture_link(client, message):
    capture = CapturesVideo.filter_first(capture_number=message.command[1])
    file_name = os.path.basename(urlparse(capture.link).path)
    urlretrieve(capture.link, file_name)
    await client.send_document(
        chat_id=message.chat.id,
        document=file_name,
        caption=capture.link,
        force_document=True,
    )
    os.unlink(file_name)

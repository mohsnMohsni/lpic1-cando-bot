# Standard imports
import urllib.request

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
    downloaded_file = urllib.request.urlopen(capture.link)
    await client.send_document(
        chat_id=message.chat.id,
        document=downloaded_file.read(),
        caption=capture.link,
        force_document=True,
    )

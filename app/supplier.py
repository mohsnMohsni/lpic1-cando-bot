# Standard imports
import os

# Third-party imports.
from pyrogram import Client


API_ID: str = os.getenv('API_ID')
API_HASH: str = os.getenv('API_HASH')
BOT_TOKEN: str = os.getenv('BOT_TOKEN')

app = Client('my_bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

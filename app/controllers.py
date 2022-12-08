# Standard imports
import os

# Third-party imports.
from dotenv import load_dotenv
from pyrogram import Client


load_dotenv(dotenv_path='envs/.env.development')
load_dotenv(dotenv_path='envs/.env.production')


API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')

app = Client('my_bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

app.run()

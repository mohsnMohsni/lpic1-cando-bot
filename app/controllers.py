# Standard imports
import asyncio

# Third-party imports.
from pyrogram import Client


API_ID = 5074998
API_HASH = '604e8a4d125e567edad04bbf5eee2abc'


async def main():
    async with Client('my_account', api_id=API_ID, api_hash=API_HASH) as app:
        await app.send_message('me', 'Greetings from **Pyrogram**!')


asyncio.run(main())

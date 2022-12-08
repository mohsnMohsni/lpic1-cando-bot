from .__main__ import app


@app.on_message()
async def test(client, message):
    await message.reply('hello', quote=True)

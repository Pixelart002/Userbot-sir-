from dotenv import load_dotenv
import os
from telethon import TelegramClient, events

load_dotenv()

API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
TARGET_CHANNEL = os.getenv('TARGET_CHANNEL')

client = TelegramClient('session', API_ID, API_HASH)

@client.on(events.NewMessage(chats=TARGET_CHANNEL))
async def handler(event):
    buttons = await event.get_buttons() or []
    for row in buttons:
        for button in row:
            if button.text and 'claim' in button.text.lower():
                await button.click()

client.start()
client.run_until_disconnected()
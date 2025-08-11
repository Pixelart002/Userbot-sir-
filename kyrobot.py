import os
from telethon import TelegramClient, events
c = TelegramClient('s', int(os.getenv('API_ID')), os.getenv('API_HASH'))
@c.on(events.NewMessage(chats=os.getenv('TARGET_CHANNEL')))
async def h(e): [await b.click() for r in (await e.get_buttons() or []) for b in r if 'claim' in (b.text or '').lower()]
c.start(); c.run_until_disconnected()
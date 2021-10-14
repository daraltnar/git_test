from telethon.sync import TelegramClient
from telethon.sessions import StringSession

from settings import (API_ID, API_HASH)

# print your session key
with TelegramClient(StringSession(), API_ID, API_HASH) as client:
    print(client.session.save())

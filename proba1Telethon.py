from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from settings import (API_ID, API_HASH, SESSION_STRING)

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

client.start()

# Узнаем немного о себе 
print(client.get_me().stringify())  
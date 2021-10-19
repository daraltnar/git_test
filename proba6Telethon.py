from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from settings import (API_ID, API_HASH, SESSION_STRING)

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

client.start()

o_sebe=client.get_me().stringify()

f=open('mess_from_teleg.txt', 'a') # сначала откроем файл на запись
f.write(o_sebe)
f.flush()  
f.close() # закроем файл после записи

# Узнаем немного о себе 
# print(client.get_me().stringify())  
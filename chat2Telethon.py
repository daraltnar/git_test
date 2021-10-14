from telethon.sync import TelegramClient, events 
from telethon.sessions import StringSession
from settings import (API_ID, API_HASH, SESSION_STRING)

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
 
@client.on(events.NewMessage(chats=(-1001199979298))) # создает событие, срабатывающее при появлении нового сообщения
async def normal_handler(event):

    user_mess=event.message.to_dict()['message'] # в переменную user_mess записываем сообщение из канала
    mess_date=event.message.to_dict()['date']  # в переменную mess_date Вытаскиваем из сообщения дату отправки

    print(user_mess, mess_date) # Печать информации

 # запишем сообщение:
    f.write(mess_date.strftime("%d-%m-%Y %H:%M")+"\n")
    f.write(user_mess+"\n\n")
    f.flush()    

client.start() # старт программы

f=open('messages_from_chat.txt', 'a') # сначала откроем файл на запись

client.run_until_disconnected() # Чтобы клиент не заканчивал работу
f.close() # закроем файл после записи
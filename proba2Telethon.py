from telethon import TelegramClient, sync # импортируем имя класса, чтобы мы могли создать экземпляр клиента
 
# Вставляем api_id и api_hash
api_id = 8063826
api_hash = '1b28e00d8dfa66234d5a9d89d01e22ec'

client = TelegramClient('parsTeleg', api_id, api_hash)

client.start()

# Узнаем немного о себе 
print(client.get_me().stringify())  
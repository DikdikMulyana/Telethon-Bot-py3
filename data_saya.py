from telethon import TelegramClient

#masukan api_id<int> dan api_hash<str> Api telegram anda
#yang telah dibuat di https://my.telegram.org/auth
api_id = xxxxx #int
api_hash = 'xxxxxxxxxxxx'

#masukan token  bot anda  yang telah dibuat di @BotFather
bot_token = 'xxxxxxxxxxxxxxx'

#methode untuk membuat session masuk api telegram user
#tulisan anon bisa di ganti sesuai keinginan anda
client = TelegramClient('anon', api_id, api_hash)

#methode untuk membuat session masuk bot telegram
#tulisan bot bisa diganti sesuai keinginan anda
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

#masukan id telegram teman atau grup anda
id_grup=xxxxxxx #id super grup diawali dengan -

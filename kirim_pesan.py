from data_saya import * # mengimport semua yang ada di script data_saya
import time
#function untuk membuat menu
def Menu():
    menu='''\033[92m
Selamat Datang di Bot Telegram Api

    1].kirim pesan dengan Api USER
    2].kirim pesan dengan bot Api
'''
    while True:
        time.sleep(0.1) # hapus baris ini
        print (menu)
        break
#....
async def main_user():
       print ('\n\033[93m============send Message USER=========')
       msg=str(input('Masukan Pesan ]>> '))
       await client.send_message(id_grup,msg)
#...
async def main_bot():
       print ('\n\033[95m===========send Message Bot===========')
       msg=str(input('masukan pesan ]>>'))
       await  bot.send_message(id_grup,msg)
#..,
def kirim_pesan_user():
       with client:
            client.loop.run_until_complete(main_user())
#....
def kirim_pesan_bot():
      with bot:
            bot.loop.run_until_complete(main_bot())

def run():
    Menu()
    pil= int(input('masukan pilihan :>> '))
    if pil == 1 :
         kirim_pesan_user()
    elif pil == 2 :
         kirim_pesan_bot()

if __name__==('__main__'):
     run()

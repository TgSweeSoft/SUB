#GitHub: TgSweeSoft

from time import sleep
from time import strftime, gmtime
from pyrogram.raw import functions
from phonenumbers import timezone
from phonenumbers import geocoder, carrier
from pyrogram import Client, filters, sync, idle
from simpledemotivators import Demotivatorimport os
import time
import random
import asyncio
import datetime
import colorama
import pyrogram
import speedtest
import memoryconv
import phonenumbers
import simpledemotivators
os.system("clear")

app = Client('SUB', api_id=1016382, api_hash='c27834e5683d50a9bacf835a95ec4763')

app.start()

app.stop()
os.system("clear")
print('''•·•·•·•·•·•·•·•·•·•·•·•·•·•·•··•·•·•·•·•·•·•·•·•·•·•·•·•·•·•
		   SweeUserBot-V1.4 alpha
		             ||
———————————————————————————Author———————————————————————————
                           
Telegram: @ROmAanChiG



•·•·•·•·•·•·•·•·•·•·•·•·•·•·•··•·•·•·•·•·•·•·•·•·•·•·•·•·•·•''')
print("")
print('''Скрипт SweeUserBot запущен теперь можешь зайти в 
telegram и в любом чате(группе) написать .help 
и ты получишь список всех анимаций!''')
print("")
print('''ЕСЛИ ЗАКРОЕШЬ Pydroid СКРИПТ РОБОТАТЬ НЕ БУДЕТ
(потому что он не черный)!''')
print()
print()

@app.on_message(filters.command("help", prefixes=".") & filters.me)
def help(app, message):
	app.send_message(message.chat.id,f'''
📙<b> Команды:</b> \n<b> 
1).plus
2).comps
3).care
4).random (0-∞) наример .random 100
5).
6).maslo
7).cat
8).nowar
9).otch
10).unfriend
11).like
12).dislike

13).spam (с новой строки любой текст и количевство сообщений) например:
.spam
текст
100

14).heart
15).mat
16).mk(любой текст) например: .mk привет
17).hack
18).hackp
19).gey
20).friend
21).pidor
22).confess
23).gule
23).numbers
24).eroglifs
25).rep
26).search
27).prof
28).snow
29).hui
30).withoutyou
31).MBI
32).or
33).ft (любой текст) например: .ft привет
34).zaeb (любой ник) например: .zaeb @username
37).time
38).timer (любое число) например: .timer 123
39).pi (номер) например: .pi +7123456 
7890
40).tl (дата и время) например: .tl 2022/10/20 9:05:51
41).date
42).timedate
43).kr (пример) например: .kr 2 * 5 / 9 - 6 + 8

💎 сделано: @ROmAanChiG
                                

''', disable_web_page_preview=True)

@app.on_message(filters.command("plus", prefixes=".") & filters.me)
def plus(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(f'''
➕
''')  
        sleep(3)  
        msg.edit(f'''
хуета..
''')
        sleep(2)  
        msg.edit(f'''
🔲
''')
        sleep(0.1)  
        msg.edit(f'''
🔲🔲
''')  
        sleep(0.1)  
        msg.edit(f'''
🔲🔲🔲⬜️⬜️
''')  
        sleep(0.1)  
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
''')  
        sleep(0.1)  
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲
''')  
        sleep(0.1)  
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲
''')  
        sleep(0.1)  
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
''')  
        sleep(0.1)  
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲
''')  
        sleep(0.1)  
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️
''')  
        sleep(0.1)
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲
''')  
        sleep(0.1)
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
''')  
        sleep(0.1)
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
⬜️⬜️⬜️
''')  
        sleep(0.1)
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
⬜️⬜️⬜️⬜️⬜️
''')  
        sleep(0.1)
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
⬜️⬜️⬜️⬜️⬜️⬜️⬜️
''')  
        sleep(0.1)
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️
''')  
        sleep(0.1)
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️
''')  
        sleep(0.1)
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️
''')  
        sleep(0.1)
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
🔲
''')  
        sleep(0.1)
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️
''')  
        sleep(0.1)
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲
''')  
        sleep(0.1)
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
''')  
        
  
  
  
  
 #❤️💙🧡💖💝💘💕💗💞
  
@app.on_message(filters.command("comps", prefixes=".") & filters.me)
def comps(app, message):
    for i in range(1):
        sleep(1)
        app.send_message(message.chat.id, f'<b>  ты моя бусиночка💗💞        </b>')
        sleep(0.1)
        app.send_message(message.chat.id, f'<b>  ты моё солнышко❤️💙        </b>')
        sleep(2)
        app.send_message(message.chat.id, f'<b>  ты мой лучик💖💝        </b>')
        sleep(3)
        app.send_message(message.chat.id, f'<b>  ты любовь всей моей жизни💘💕💗        </b>')
        sleep(1)
        app.send_message(message.chat.id, f'<b>  ты мой ангелочек💘💗🧡     </b>')
        sleep(4)
        app.send_message(message.chat.id, f'<b>  ты мое счастье💖        </b>')
        sleep(2)
        app.send_message(message.chat.id, f'<b>  когда ты мне пишешь у меня поднымаеться настроение        </b>')
        sleep(1)
        app.send_message(message.chat.id, f'<b>  ты самая красивая девачка😎💗        </b>')
        sleep(3)
        app.send_message(message.chat.id, f'<b>  ты моя звёздочка✨💟        </b>')
        sleep(3)
        app.send_message(message.chat.id, f'<b>  ты мой чертёночек🥺❤️‍🔥        </b>')
        sleep(2)
        app.send_message(message.chat.id, f'<b>  ты украла мое сердце💟❣       </b>')
        sleep(4)
        app.send_message(message.chat.id, f'<b>  ты мой цветочек🌹🌸💛       </b>')
        sleep(1)
        app.send_message(message.chat.id, f'<b>  ты мой котёнок😻        </b>')
        sleep(2)
        app.send_message(message.chat.id, f'<b>  ты не человек, ты сокровище        </b>')
        sleep(3)
        app.send_message(message.chat.id, f'<b>  люблю только тебя🥺❤️‍         </b>')



@app.on_message(filters.command("care", prefixes=".") & filters.me)
def care(app, message):
    for i in range(1):
        sleep(0.01)
        app.send_message(message.chat.id, f'<b>  приветик❤️❤️        </b>')
        sleep(3)
        app.send_message(message.chat.id, f'<b>  Как дела котик❤️😺?        </b>')
        sleep(3)
        app.send_message(message.chat.id, f'<b>  что делает мой котик?🥺        </b>')
        sleep(3)
        app.send_message(message.chat.id, f'<b>  моя зайка поела?❤️🍎        </b>')
        sleep(3)
        app.send_message(message.chat.id, f'<b>  как настроение?❤❤️        </b>')
        sleep(3)
        app.send_message(message.chat.id, f'<b>  нечего не болит?❤️        </b>')
        sleep(3)
        app.send_message(message.chat.id, f'''<b>  ──────────────────────
─────▄█▀█▄──▄███▄───── 
────▐█░██████████▌──── 
─────██▒█████████─────
──────▀████████▀────── 
─────────▀██▀─────────        </b>''')
        sleep(3)
        app.send_message(message.chat.id, f'''<b>  это ты:

../\„„./\.
.(='•'= ) .
.(")❤️(").
. \,\„„/,/
. │„„. „│
. /„/„ \„\

.(„)''l l''(„)
. .. ((...
. . . ))..
. . .((..        </b>''')



@app.on_message(filters.command("nowar", prefixes=".") & filters.me)
def nowar(_, msg):
    time = 1
    for i in range(1):
        msg.edit(f'''
🇷🇺🇷🇺🇷🇺🇷🇺 vs 🇺🇦🇺🇦🇺🇦🇺🇦
''')
        sleep(1)
        msg.edit(f'''
🇷🇺🇷🇺🇷🇺🇷🇺 vs 🇺🇦🇺🇦🇺🇦🇺🇦

эээ
''')
        sleep(1)
        msg.edit(f'''
🇷🇺🇷🇺🇷🇺🇷🇺 vs 🇺🇦🇺🇦🇺🇦🇺🇦

эээ ты что?
''')
        sleep(1.5)
        msg.edit(f'''
🇷🇺🇷🇺🇷🇺🇷🇺 🤝 🇺🇦🇺🇦🇺🇦🇺🇦

эээ ты что? 
какая война нахуй?
''')
        sleep(1)
        msg.edit(f'''
🇷🇺🇷🇺🇷🇺🇷🇺 🤝 🇺🇦🇺🇦🇺🇦🇺🇦

эээ ты что? 
какая война нахуй?
я за мир!
''')
        sleep(1)
        msg.edit(f'''
🇷🇺🇷🇺🇷🇺🇷🇺 🤝 🇺🇦🇺🇦🇺🇦🇺🇦

эээ ты что? 
какая война нахуй?
Я ЗА МИР!🥺
''')
        sleep(1)
        msg.edit(f'''
🇺🇦🇺🇦🇺🇦🇺🇦 🤝 🇺🇦🇺🇦🇺🇦🇺🇦

эээ ты что? 
какая война нахуй?
Я ЗА МИР!🥺

ОЙ
''')
        sleep(1)



@app.on_message(filters.command("snow", prefixes=".") & filters.me)
def snow(_, msg):
    time = 0.6
    for i in range(7):
        msg.edit(f'''
 ❄   
                              ❄
          ❄
                    ❄
         ❄                     ❄
                  ❄
''')
        sleep(0.1)
        msg.edit(f'''
  ❄   
                           ❄
        ❄
                      ❄
           ❄                  ❄
                     ❄
''')
        sleep(0.1)
        msg.edit(f'''
       ❄   
                              ❄
          ❄  
                          ❄
          ❄                     ❄
                
''')
        sleep(0.1)
        msg.edit(f'''
  ❄   
                               ❄
          ❄  
                     ❄
       ❄                    ❄
                  ❄
''')
        sleep(0.1)
        msg.edit(f'''
         ❄   
                      ❄
        ❄
                         ❄
                 ❄            ❄
          ❄
''')
        sleep(0.1)
        


@app.on_message(filters.command("MBI", prefixes=".") & filters.me)
def mbi(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(f'''
Стираем тебе память..
''')
        sleep(1)
        msg.edit(f'''
⚫
⚫
⚫
⚫
⚫
''')  
        sleep(0.5)
        msg.edit(f'''
🔴
⚫
⚫
⚫
⚫
''')  
        sleep(0.5)
        msg.edit(f'''
⚫
🔴
⚫
⚫
⚫
''')  
        sleep(0.5)
        msg.edit(f'''
⚫
⚫
🔴
⚫
⚫
''')  
        sleep(0.5)
        msg.edit(f'''
⚫
⚫
⚫
🔴
⚫
''')  
        sleep(0.5)
        msg.edit(f'''
⚫
⚫
⚫
⚫
🔴
''')  
        sleep(0.5)
        msg.edit(f'''
⚫
⚫
⚫
🔴
🔴
''')  
        sleep(0.5)
        msg.edit(f'''
⚫
⚫
🔴
🔴
🔴
''')  
        sleep(0.5)
        msg.edit(f'''
⚫
🔴
🔴
🔴
🔴
''')  
        sleep(0.5)
        msg.edit(f'''
🔴
🔴
🔴
🔴
🔴
''')  
        sleep(1)
        msg.edit(f'''
Загрузка..
''')
        sleep(3)
        msg.edit(f'''
✅Загрузка успешно завершена!
''')
        sleep(1)
        msg.edit(f'''
◼️◼️◼️◼️◼️◼️◼️◼️
◼️привет               ◼️
◼️                           ◼️
◼️                           ◼️
◼️                            ◼️
◼️◼️◼️◼️◼️◼️◼️◼️
''')
        sleep(0.5)
        msg.edit(f'''
◼️◼️◼️◼️◼️◼️◼️◼️
◼️привет               ◼️
◼️помнишь          ◼️
◼️                	       	  ◼️
◼️                            ◼️
◼️◼️◼️◼️◼️◼️◼️◼️
''')
        sleep(0.5)
        msg.edit(f'''
◼️◼️◼️◼️◼️◼️◼️◼️
◼️привет               ◼️
◼️помнишь          ◼️
◼️сотку занимал◼️
◼️                            ◼️
◼️◼️◼️◼️◼️◼️◼️◼️
''')






@app.on_message(filters.command("hui", prefixes=".") & filters.me)
def hui(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(f'''
    🍆🍆        🍆🍆
''')  
        sleep(0.1)
        msg.edit(f'''
 🍆🍆🍆  🍆🍆🍆
    🍆🍆        🍆🍆
''')  
        sleep(0.1)
        msg.edit(f'''
   🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆        🍆🍆
''')  
        sleep(0.1)
        msg.edit(f'''
          🍆🍆🍆
   🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆        🍆🍆
''')  
        sleep(0.1)
        msg.edit(f'''
        🍆🍆🍆
         🍆🍆🍆
   🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆        🍆🍆
''')  
        sleep(0.1)
        msg.edit(f'''
          🍆🍆🍆
           🍆🍆🍆
            🍆🍆🍆
   🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆        🍆🍆
''')  
        sleep(0.1)
        msg.edit(f'''
         🍆🍆🍆
          🍆🍆🍆
           🍆🍆🍆
            🍆🍆🍆
   🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆        🍆🍆
''')  
        sleep(0.1)
        msg.edit(f'''
        🍆🍆🍆
         🍆🍆🍆
          🍆🍆🍆
           🍆🍆🍆
            🍆🍆🍆
   🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆        🍆🍆
''')  
        sleep(0.1)
        msg.edit(f'''
       🍆🍆🍆
        🍆🍆🍆
         🍆🍆🍆
          🍆🍆🍆
           🍆🍆🍆
            🍆🍆🍆
   🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆        🍆🍆
''')  
        sleep(0.1)
        msg.edit(f'''
    🍆🍆🍆
      🍆🍆🍆
       🍆🍆🍆
        🍆🍆🍆
         🍆🍆🍆
          🍆🍆🍆
           🍆🍆🍆
            🍆🍆🍆
   🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆        🍆🍆
''')  
        sleep(0.1)
        msg.edit(f'''
🍆🍆
🍆🍆🍆
  🍆🍆🍆
    🍆🍆🍆
     🍆🍆🍆
      🍆🍆🍆
       🍆🍆🍆
        🍆🍆🍆
         🍆🍆🍆
          🍆🍆🍆
          🍆🍆🍆
    🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆        🍆🍆
''')  



@app.on_message(filters.command("otch", prefixes=".") & filters.me)
def otch(app, message):
    for i in range(1):
        sleep(1)
        app.send_message(message.chat.id, f'<b>  ПРИВЕТ        </b>')
        sleep(1)
        app.send_message(message.chat.id, f'<b>  Я ТВОЙ ОТЧИМ        </b>')
        sleep(1)
        app.send_message(message.chat.id, f'<b>  И ЕСЛИ ТЫ НЕ ЗАСНЁШЬ        </b>')
        sleep(1)
        app.send_message(message.chat.id, f'<b>  Я ПРИДУ К ТЕБЕ В КРОВАТКУ        </b>')
        sleep(1)
        app.send_message(message.chat.id, f'<b>  И ВЫЕБУ В ПОПКУ!!!!!!        </b>')





@app.on_message(filters.command("search", prefixes=".") & filters.me)
def search(app, message):
    for i in range(1):
        sleep(0.01)
        app.send_message(message.chat.id, f'<b>  👁‍🗨ПОИСК ТВОЕЙ МАМАШИ..        </b>')
        sleep(2)
        app.send_message(message.chat.id, f'<b>  ВНИМАНИЕ МАМАША НЕ НАЙДЕНА!❌        </b>')
        sleep(0.1)
        app.send_message(message.chat.id, f'<b>  🔍 ПОИСК ТВОЕГО БАТИ..        </b>')
        sleep(2)
        app.send_message(message.chat.id, f'<b>  БАТЯ НЕ НАЙДЕН! ❌        </b>')
        sleep(0.01)
        app.send_message(message.chat.id, f'<b>  🔍ПОИСК ТВОЕГО ОТЧИМА..        </b>')
        sleep(0.01)
        app.send_message(message.chat.id, f'<b>  ТВОЙ ОТЧИМ НАЙДЕН! ✅   </b>')
        
        
        
        
@app.on_message(filters.command("withoutyou", prefixes=".") & filters.me)
def withoutyou(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(f'''
МОЁ НАСТРОЕНИЕ БЕЗ ТЕБЯ🧡
''')     
        sleep(2)
        msg.edit(f'''
МОЁ НАСТРОЕНИЕ БЕЗ ТЕБЯ🧡
😀
''')     
        sleep(1)
        msg.edit(f'''
МОЁ НАСТРОЕНИЕ БЕЗ ТЕБЯ🧡
😀
🙃
''') 
        sleep(1)
        msg.edit(f'''
МОЁ НАСТРОЕНИЕ БЕЗ ТЕБЯ🧡
😀
🙃
😌
''') 

        sleep(1)
        msg.edit(f'''
МОЁ НАСТРОЕНИЕ БЕЗ ТЕБЯ🧡
😀
🙃
😌
😞
''') 

        sleep(2)
        msg.edit(f'''
МОЁ НАСТРОЕНИЕ БЕЗ ТЕБЯ🧡
😀
🙃
😌
😞
😔
''')  
        sleep(1.5)
        msg.edit(f'''
МОЁ НАСТРОЕНИЕ БЕЗ ТЕБЯ🧡
😀
🙃
😌
😞
😔
😓
''')  
        sleep(2)
        msg.edit(f'''
МОЁ НАСТРОЕНИЕ БЕЗ ТЕБЯ🧡
😀
🙃
😌
😞
😔
😓
🥺
''')  
        sleep(1.5)
        msg.edit(f'''
МОЁ НАСТРОЕНИЕ БЕЗ ТЕБЯ🧡
😀
🙃
😌
😞
😔
😓
🥺
😭
''')  
     
        
        
        
        
@app.on_message(filters.command("prof", prefixes=".") & filters.me)
def prof(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(f'''
ВАШ ПРОФИЛЬ
''')  
        sleep(1)
        msg.edit(f'''
ВАШ ПРОФИЛЬ

Загрузка...
''')  
        sleep(1)
        msg.edit(f'''
ВАШ ПРОФИЛЬ

ВЫ УЕБАН        
''')
        sleep(0.01)
        msg.edit(f'''
ВАШ ПРОФИЛЬ

ВЫ УЕБАН        
Загрузка...
''')
        sleep(1)
        msg.edit(f'''
ВАШ ПРОФИЛЬ

ВЫ УЕБАН  
ВАШ ВОЗРАСТ 8 ЛЕТ
''')
        sleep(0.001)
        msg.edit(f'''
ВАШ ПРОФИЛЬ

ВЫ УЕБАН  
ВАШ ВОЗРАСТ 8 ЛЕТ
Загрузка...
''')
        sleep(1)
        msg.edit(f'''
ВАШ ПРОФИЛЬ

ВЫ УЕБАН  
ВАШ ВОЗРАСТ 8 ЛЕТ
ВЫ  В 2-ОМ КЛАССЕ
''')    
        sleep(0.01)
        msg.edit(f'''
ВАШ ПРОФИЛЬ

ВЫ УЕБАН  
ВАШ ВОЗРАСТ 8 ЛЕТ
ВЫ  В 2-ОМ КЛАССЕ
Загузка...
''')
        sleep(1)
        msg.edit(f'''
ВАШ ПРОФИЛЬ

ВЫ УЕБАН  
ВАШ ВОЗРАСТ 8 ЛЕТ
ВЫ  В 2-ОМ КЛАССЕ
ВАШ БАТЯ УЕБАН
''')
        sleep(0.01)
        msg.edit(f'''
ВАШ ПРОФИЛЬ

ВЫ УЕБАН  
ВАШ ВОЗРАСТ 8 ЛЕТ
ВЫ  В 2-ОМ КЛАССЕ
ВАШ БАТЯ УЕБАН
Загрузка...
''')
        sleep(1)
        msg.edit(f'''
ВАШ ПРОФИЛЬ

ВЫ УЕБАН  
ВАШ ВОЗРАСТ 8 ЛЕТ
ВЫ  В 2-ОМ КЛАССЕ
ВАШ БАТЯ УЕБАН
ВАША МАМКА ШЛЮХА
''')
        sleep(0.01)
        msg.edit(f'''
ВАШ ПРОФИЛЬ

ВЫ УЕБАН  
ВАШ ВОЗРАСТ 8 ЛЕТ
ВЫ  В 2-ОМ КЛАССЕ
ВАШ БАТЯ УЕБАН
ВАША МАМКА ШЛЮХА
Загрузка...
''')
        sleep(1)
        msg.edit(f'''
ВАШ ПРОФИЛЬ

ВЫ УЕБАН  
ВАШ ВОЗРАСТ 8 ЛЕТ
ВЫ  В 2-ОМ КЛАССЕ
ВАШ БАТЯ УЕБАН
ВАША МАМКА ШЛЮХА
ВАШ БРАТ ЕБАЛ ВАС 9 РАЗ
''')
        sleep(0.01)
        msg.edit(f'''
ВАШ ПРОФИЛЬ

ВЫ УЕБАН  
ВАШ ВОЗРАСТ 8 ЛЕТ
ВЫ  В 2-ОМ КЛАССЕ
ВАШ БАТЯ УЕБАН
ВАША МАМКА ШЛЮХА
ВАШ БРАТ ЕБАЛ ВАС 9 РАЗ
Загрузка...
''')
        sleep(1)
        msg.edit(f'''
ВАШ ПРОФИЛЬ

ВЫ УЕБАН  
ВАШ ВОЗРАСТ 8 ЛЕТ
ВЫ В 2-ОМ КЛАССЕ
ВАШ БАТЯ УЕБАН
ВАША МАМКА ШЛЮХА
ВАШ БРАТ ЕБАЛ ВАС 9 РАЗ
ВЫ ГЕЙ!
''')
       
        
       
        
@app.on_message(filters.command("rep", prefixes=".") & filters.me)
def rep(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(f'''
Ты..''')  
        sleep(1)
        msg.edit(f'''
Говно''') 
        sleep(0.001)
        msg.edit(f'''
залупа''') 
        sleep(0.001)
        msg.edit(f'''
пенис''')  
        sleep(0.001)
        msg.edit(f'''
хер''')  
        sleep(0.001)
        msg.edit(f'''
давалка''')  
        sleep(0.001)
        msg.edit(f'''
хуй''')  
        sleep(0.001)
        msg.edit(f'''
Головка''')  
        sleep(0.001)
        msg.edit(f'''
шлюха''')  
        sleep(0.001)
        msg.edit(f'''
жопа''')  
        sleep(0.001)
        msg.edit(f'''
член''')  
        sleep(0.001)
        msg.edit(f'''
еблан''')  
        sleep(0.001)
        msg.edit(f'''
петух''')  
        sleep(0.001)
        msg.edit(f'''
мудила''')  
        sleep(0.001)
        msg.edit(f'''
Рукоблуд''')  
        sleep(0.001)
        msg.edit(f'''
ссанина''')  
        sleep(0.001)
        msg.edit(f'''
очко''')  
        sleep(0.001)
        msg.edit(f'''
блядун''')  
        sleep(0.001)
        msg.edit(f'''
вагина''')  
        sleep(0.001)
        msg.edit(f'''
Сука''')
        sleep(0.001)
        msg.edit(f'''
ебланище''')
        sleep(0.001)
        msg.edit(f'''
влагалище''')
        sleep(0.001)
        msg.edit(f'''
пердун''')
        sleep(0.001)
        msg.edit(f'''
дрочила(я тож)''')
        sleep(0.001)
        msg.edit(f'''
Пидор''')
        sleep(0.001)
        msg.edit(f'''
пизда''')
        sleep(0.001)
        msg.edit(f'''
туз''')
        sleep(0.001)
        msg.edit(f'''
мудила''')
        sleep(0.001)
        msg.edit(f'''
гомик''')
        sleep(0.001)
        msg.edit(f'''
малафья''')
        sleep(0.001)
        msg.edit(f'''
пилотка''')
        sleep(0.001)
        msg.edit(f'''
манда''')
        sleep(0.001)
        msg.edit(f'''
Анус''')
        sleep(0.001)
        msg.edit(f'''
вагина''')
        sleep(0.001)
        msg.edit(f'''
путана''')
        sleep(0.001)
        msg.edit(f''' 
педрила''')
        sleep(0.001)
        msg.edit(f'''
шалава''')
        sleep(0.001)
        msg.edit(f'''
хуила''')
        sleep(0.001)
        msg.edit(f'''
мошонка''')
        sleep(0.001)
        msg.edit(f'''
елда.''')



@app.on_message(filters.command("numbers", prefixes=".") & filters.me)
def numbers(_, msg):
    time = 0.6
    for i in range(9):
        msg.edit(f'''      
0 1 0 1 0 0 1 0 1 1 0 1 1 0 0
1 0 1 0 1 0 1 0 1 0 1 0 0 1 1
0 1 1 0 0 0 1 1 0 1 0 1 0 0 1
1 1 0 1 0 1 1 1 0 1 0 0 0 1 0
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
''')  
        sleep(0.001)
        msg.edit(f'''      
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
1 0 1 0 1 0 1 0 1 0 1 0 0 1 1
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
0 1 1 0 0 0 1 1 0 1 0 1 0 0 1
1 1 0 1 0 1 1 1 0 1 0 0 0 1 0
''')  
        sleep(0.001)
        msg.edit(f'''      
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
1 1 0 1 0 1 1 1 0 1 0 0 0 1 0
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
0 1 0 1 0 0 1 0 1 1 0 1 1 0 0
''')  
        sleep(0.001)
        msg.edit(f'''      
0 0 1 0 1 0 1 1 0 0 1 1 0 1 1
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
1 0 1 0 1 0 0 1 1 0 0 0 1 0 1
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
0 1 1 1 1 0 1 1 1 1 0 1 0 1 0
''')  
        sleep(0.001)
        msg.edit(f'''      
1 0 0 1 1 0 1 0 0 1 0 1 1 0 1
0 1 0 1 0 0 1 1 1 1 0 1 1 0 0
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
0 1 1 1 1 0 1 1 1 1 0 1 0 1 0
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
''')  
        sleep(0.001)
        msg.edit(f'''      
0 1 1 0 0 0 1 1 0 1 0 1 0 0 1
1 0 1 0 1 0 0 1 1 0 0 0 1 0 1
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
1 0 0 1 1 0 1 0 0 1 0 1 1 0 1
''')  
        sleep(0.001)
        msg.edit(f'''      
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
0 1 1 0 0 0 1 1 0 1 0 1 0 0 1
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
''') 
        sleep(0.001)
        msg.edit(f'''      
1 1 0 1 0 1 1 1 0 1 0 0 0 1 0
0 0 1 0 1 0 1 1 0 0 1 1 0 1 1
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
1 0 1 0 1 0 0 1 1 0 0 0 1 0 1
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
''')
        sleep(0.001)
        msg.edit(f'''      
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
1 0 0 1 1 0 1 0 0 1 0 1 1 0 1
0 1 0 1 0 0 1 1 1 1 0 1 1 0 0
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
0 1 1 1 1 0 1 1 1 1 0 1 0 1 0
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
''')
        sleep(0.001)
        msg.edit(f'''      
0 1 1 0 1 0 0 1 1 0 1 1 0 1 0
1 1 0 1 0 1 1 1 0 1 0 0 0 1 0
0 0 1 0 1 0 1 1 0 0 1 1 0 1 1
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
1 0 1 0 1 0 0 1 1 0 0 0 1 0 1
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
''')
        sleep(0.001)
        msg.edit(f'''      
1 0 0 1 0 1 1 0 1 0 1 0 1 1 0
0 0 1 0 1 0 1 1 0 0 1 1 0 1 1
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
1 0 1 0 1 0 0 1 1 0 0 0 1 0 1
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
''')
        sleep(0.001)
        msg.edit(f'''      
1 0 1 0 1 0 0 1 1 0 0 0 1 0 1
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
1 0 1 0 1 0 1 0 1 0 1 0 0 1 1
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
0 1 1 0 0 0 1 1 0 1 0 1 0 0 1
''')
        sleep(0.001)
        msg.edit(f'''      
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
1 1 0 1 0 1 1 1 0 1 0 0 0 1 0
0 0 1 0 1 0 1 1 0 0 1 1 0 1 1
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
1 0 1 0 1 0 0 1 1 0 0 0 1 0 1
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
''')




@app.on_message(filters.command("eroglifs", prefixes=".") & filters.me)
def eroglifs(_, msg):
    time = 0.6
    for i in range(9):
        msg.edit(f'''      
내가엿푸틴에서항문이빌
어먹을도대체나는해치지
않을것이그의빌어먹나문
나를메시서보낸도더런난
당신과그녀가그렇게니라
''')  
        sleep(0.001)
        msg.edit(f'''
난기다리고있을때기대에
대한지불을납품에어떤채
팅또는토요일에그것은로
봇을켜는현재에썼고그런
다음필요가없당신이일주 
''')
        sleep(0.001)
        msg.edit(f'''
그런데왜내가나에게필요
한모든일을한기회가있다
는것을내가모든일을했다
고당신의가족과아이들에
게말해야합니까일에그에
''')
        sleep(0.001)
        msg.edit(f'''
아니면너무오래전에이메
일주소로편지를쓸수있지
기회를가지고있지않았다
우리가만나고토론할수있
것입니다그후년되지않습
''')
        sleep(0.001)
        msg.edit(f'''
것입니다그후년되지않습
고당신의가족과아이들에
는것을내가모든일을했다
내가엿푸틴에서항문이빌
어먹을도대체나는해치지
''')
        







@app.on_message(filters.command("random", prefixes=".") & filters.me)
def rand(_, msg):
    random1 = msg.text.split(" ", maxsplit=2)
    
    del random1[0]
    
    random2 = random1[0]
    random3 = random1[1]
    
    random4 = random.randint(int(random2), int(random3))
    
    msg.edit(f"<b> Цыгане показали число: {random4}</b>")
        
        
    
@app.on_message(filters.command("gule", prefixes=".") & filters.me)
def gule(app, message):
    app.send_message(message.chat.id,f'<b>1000-7=?</b>')
    sleep(4)
    i = 1000
    while i > 0:
        try:
            app.send_message(message.chat.id, f'{i} - 7 = {i-7}')
        except FloodWait as e:
            sleep(e.x)

        i -= 7
        sleep(0)


@app.on_message(filters.command("spam", prefixes=".") & filters.me)
def spam(app, message):
    spam1 = message.text.split("\n", maxsplit=3)
    del spam1[0]
    print(spam1)
    spam2 = spam1[0]
    spam4 = spam1[1]
    for i in range(int(spam4)):
        app.send_message(message.chat.id, f"{spam2}")
        




@app.on_message(filters.command("go", prefixes=".") & filters.me)
def betaloves(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(f'''      
хммммм        ''')  
        sleep(3)
        msg.edit(f'''      
го..        ''')  
        sleep(3)
        msg.edit(f'''      
e..        ''')  
        sleep(3)
        msg.edit(f'''      
б..        ''')  
        sleep(3)
        msg.edit(f'''      
а..        ''')  
        sleep(3)
        msg.edit(f'''      
т..        ''')  
        sleep(3)
        msg.edit(f'''      
с..        ''')  
        sleep(3)
        msg.edit(f'''      
я..        ''')  
        sleep(2)
        msg.edit(f'''      
за шоколадку        ''')  
        sleep(1)
        msg.edit(f'''      
милку^^        ''')  
        sleep(3)
        msg.edit(f'''      
❤с орешками❤        ''')  
        sleep(2)
        msg.edit(f'''      
💚го?💚        ''')  
        






@app.on_message(filters.command("maslo", prefixes=".") & filters.me)
def betalove(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(f"<b>я</b>")  
        sleep(time)
        msg.edit(f"<b>я люблю</b>")  
        sleep(time)
        msg.edit(f"<b>я люблю когда</b>")  
        sleep(time)
        msg.edit(f"<b>я люблю когда волосатые</b>")  
        sleep(time)
        msg.edit(f"<b>я люблю когда волосатые мужики</b>")  
        sleep(time)
        msg.edit(f"<b>я люблю когда волосатые мужики обмазываются</b>")  
        sleep(time)
        msg.edit(f"<b>я люблю когда волосатые мужики обмазываются маслом 🧈</b>")  





@app.on_message(filters.command("like", prefixes=".") & filters.me)
def betaloves(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(f'''      
🟦''')  
        sleep(0.001)
        msg.edit(f'''
🟦🟦''')  
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦🟦🟦🟦''')
        sleep(5)



@app.on_message(filters.command("dislike", prefixes=".") & filters.me)
def betaloves(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(f'''
🟥''')  # 
        sleep(0.001)
        msg.edit(f'''
🟥🟥''')  
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥''')
        sleep(1)
        msg.edit(f'''
🈲🈲🈲🈲🈲🈲🈲🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲⬜️⬜️⬜️⬜️🈲⬜️🈲
🈲🈲🈲🈲⬜️🈲🈲🈲
🈲🈲🈲🈲🈲🈲🈲🈲''')
        sleep(1)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥
''')
        sleep(1)
        msg.edit(f'''
🈲🈲🈲🈲🈲🈲🈲🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲⬜️⬜️⬜️⬜️🈲⬜️🈲
🈲🈲🈲🈲⬜️🈲🈲🈲
🈲🈲🈲🈲🈲🈲🈲🈲''')
        sleep(4)


@app.on_message(filters.command("heart", prefixes=".") & filters.me)
def betalove(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n") 
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(1)


@app.on_message(filters.command("mat", prefixes=".") & filters.me)
def mat(app, message):
    app.send_message(message.chat.id,f'''
<b>помолчи хуета, сиди в обиде ребёнок мертвой шалавы</b>
''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>заебись невъебенным проебом тримандоблядская пиздопроебина воспиздозаолупоклинившаяся в собственном злопиздии.</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>пиздобратия мандопроушечная, уебище залупоглазое</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>дрочепиздище хуеголовое, пробиздоблядская мандопроушина</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>гнидопаскудная хуемандовина</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>ах ты блядь семитаборная чтоб тебя всем столыпином харили</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>охуевшее блядепиздопроёбище чтоб ты хуем поперхнулся долбоебическая пиздорвань</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>хуй тебе в глотку через анальный проход</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>распизди тебя тройным перебором через вторичный переёб пиздоблятское хуепиздрическое мудовафлоебище сосущее километры трипперных членов</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>трихломидозопиздоеблохуе блядеперепиздическая спермоблевотина</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>гандон с гонореей...</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>да разъебись ты троебучим проебом сперматоблятская пиздапроебина </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>охуевающая в своей пидарастической сущности похожаю на ебущегося в жопу енота </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>сортирующего яйца в пизде кастрированной кобылы</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>хуелептический пиздопрозоид, еблоухий мандохвост</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>ебун хуеголовый, пидрасня ебаная. </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Залупоголовая блядоящерица. .</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Трипиздоблядская промудохуина! </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Распроеб твою в крестище через коромысло в копейку мать! </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Что за блядская пиздопроебина, охуевающая своей пидорестической заебучестью невъебенной степени охуения. </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Заебись невъебенным проебом тримандоблядская пиздопроебина воспиздозаолупоклинившаяся в собственном злопиздии. </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Мордоблядина залупоглазая.  блядского невъебения! </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Шлюшья мразота приохуебенивающая от собственного недохуеплетского злоетрахания. </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Да произпездуй с 2000 этажа своей припиздоблядской тушей на землю в труху! </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Трипиздоблядское мудопроебное трипиздие, ебоблядище охуевающее от собственной злоебучести.  </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Облямуденный злоебучий страхопизднутый трихуемандаблядский </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>ебаквакнутый распиздаеб... </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Хуесосляблядивый расхуйдяй припиздоблядского четвертоногого происхождения </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>прошу завали свой хуеобрыганский блядозвукоговоритель. </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Промудохуепиздамразоблядское злоепиздие </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>ебоблядищая пиздопроебина сама ахуевающее от того какая оно пездоблядехуепроклятое.</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Обосробосанная пиздоблядмна двадцати головая семихуюлина припиздовывающее от хуеглотности своей трипиздговноглоталки.</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Облямудевшая хуеблядина четырестохуйная</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>вестипёздная мразотоблядская шлюхасосалка. </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Хуесосная мудохуепиздопроебная мудаблядина сука безмаманя </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>блядь шмара козельуебок сдохни </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>хуесоска  ебланафт чмырь пидорска манда тупая гандопляс пидрила ебалай долбоеб обмудок овцееб дауниха  </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>ненавижу гомодрилла сучка шлюха трахарила гавносос миньетчик </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>пидэраст пиздоеб хуеплет кончиглот ебище сын шлюхи гавноеб мудяра </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>еботрон вафлеглот ебалдуй захуятор имбицил подонок пиздопромудище </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>выебок ахуяэетер ебозер пиздолиз злоуебок хуиман ебил долбоебина пиндос мудазвон </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>хуеб амеба хуйло хуила пиздорвань смесь ебланства и говна ебанат </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>умалишенный дегенерат мандопроушина очкоблут порванный обрубок хуяраспиздяй свинозалупа</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>семиголовый восьмихуй ебоблядище свинохуярище вафлепиздище хуй лохматый жопа рванная мудопроеб </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>страхапиздище ебосос дурфанка косоуебище долбоногий лихохуетень</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>⭐️</b>
     ''')




@app.on_message(filters.command("mk", prefixes=".") & filters.me)
def mk(_, msg):
    orig_text = msg.text.split(".mk ", maxsplit=1)[1]
    text = orig_text
    tbp = "" # to be printed
    typing_symbol = "|"
 
    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05) # 50 ms
 
            tbp = tbp + text[0]
            text = text[1:]
 
            msg.edit(tbp)
            sleep(0.05)
 
        except FloodWait as e:
            sleep(e.x)
 

@app.on_message(filters.command("hack", prefixes=".") & filters.me)
def hack(_, msg):
    perc = 0
 
    while(perc < 100):
        try:
            text = "👮 Взлом вашего аккаунта в процессе ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🟢 Аккаунт успешно взломан!")
    sleep(3)
 
    msg.edit("📂Поиск данных пользователя ...")
    perc = 0
 
    while(perc < 100):
        try:
            text = "📂Поиск данных пользователя ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 5)
            sleep(0.15)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("📂Аккаунт взломан, все необходимые данные получены!")


@app.on_message(filters.command("hackp", prefixes=".") & filters.me)
def hackp(_, msg):
    perc = 0
 
    while(perc < 100):
        try:
            text = "👮Взлом Пентагона в процессе ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🟢 Пентагон успешно взломан!")
    sleep(3)
 
    msg.edit("📂Поиск данных на серверах Пентагона ...")
    perc = 0
 
    while(perc < 100):
        try:
            text = "📂Поиск данных на серверах Пентагона ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 5)
            sleep(0.15)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("📂Пентагон взломан, все необходимые данные получены!")
 

@app.on_message(filters.command("gey", prefixes=".") & filters.me)
def gey(_, msg):
    perc = 0
 
    while(perc < 100):
        try:
            text = "👮Превращаем вас в гея/лесбиянку ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(6, 12)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🟢 успешно, Вы гей/лесбиянка!")
    sleep(3)
 
    msg.edit("📂Поиск рядом находящихся Геев/Лесбиянок ...")
    perc = 0
 
    while(perc < 100):
        try:
            text = "📂Поиск рядом находящихся Геев/Лесбиянок ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(3, 6)
            sleep(0.15)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("📂Успешно Найдено, все необходимые данные получены И Обработаны. это ваш собеседник по чату! (совет: БЕГИТЕЕ!!)")


@app.on_message(filters.command("friend", prefixes=".") & filters.me)
def friend(_, msg):
    perc = 0
 
    while(perc < 100):
        try:
            text = "Наша дружба закончится через ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("...")
    sleep(2)
 
    msg.edit("Разрыв дружбы ...")
    perc = 0
 
    while(perc < 100):
        try:
            text = "Разрыв дружбы ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 5)
            sleep(0.15)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("Дружба разорвана, навеки, Прощай!")






@app.on_message(filters.command("unfriend", prefixes=".") & filters.me)
def friend(_, msg):
    perc = 0
 
    while(perc < 100):
        try:
            text = "Наша дружба закончится через ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("❌Ошибка, вы останетесь друзьями на вечно!")





@app.on_message(filters.command("pidor", prefixes=".") & filters.me)
def pidor(_, msg):
    perc = 0
 
    while(perc < 100):
        try:
            text = "Сканирование пользователя ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(4, 8)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("...")
    sleep(3)
 
    msg.edit("Пользователь успешно просканировался!")
    sleep(3)
    perc = 0
 
    while(perc < 100):
        try:
            text = "Сбор данных пользователя ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(7, 20)
            sleep(0.15)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("Пользователь пидорас")




@app.on_message(filters.command("confess", prefixes=".") & filters.me)
def confess(app, message):
    app.send_message(message.chat.id,f'''
<b>я..</b>
''')
    sleep(3)
    app.send_message(message.chat.id, f'''
    <b>давно хотел тебе сказать..</b>
    ''')
    sleep(4)
    app.send_message(message.chat.id, f'''
    <b>что...</b>
    ''')
    sleep(3)
    app.send_message(message.chat.id, f'''
    <b>очень.. очень сильно..</b>
    ''')
    sleep(1)
    app.send_message(message.chat.id, f'''
    <b>люблю тебя💙❤️</b>
    ''')
    sleep(1)
    app.send_message(message.chat.id, f'''
    <b>я хочу с тобой прожить всю жизнь❤️</b>
    ''')
    sleep(2)
    app.send_message(message.chat.id, f'''
    <b>ты мой котик❤️</b>
    ''')
    sleep(2)
    app.send_message(message.chat.id, f'''
    <b>мой ангелочек❤️</b>
    ''')
    sleep(2)
    app.send_message(message.chat.id, f'''
    <b>моя звёздочка⭐️</b>
    ''')
    sleep(2)
    app.send_message(message.chat.id, f'''
    <b>люблю тебя безумно❤️</b>
    ''')
    sleep(2)
    app.send_message(message.chat.id, f'''
    <b>жить без тебя не могу❤️</b>
    ''')
    sleep(2)
    app.send_message(message.chat.id, f'''
    <b>ты моя любовь..❤️</b>
''')   



@app.on_message(filters.command("zaeb", prefixes=".") & filters.me)
def test(app, message):
	orig_te1t = message.text.split(".zaeb ", maxsplit=1)[1]
	user_text = orig_te1t
	user_txt = user_text.replace("@", "")
	message.delete(message.chat.id)
	for i in range(50):
		try:
			app.send_message(message.chat.id, f"[бесим)](https://t.me/{user_txt})", disable_web_page_preview=True)
		except FloodWait as e:
			sleep(e.x)
		
		sleep(0.5)







@app.on_message(filters.command("ft", prefixes=".") & filters.me)
def fancy_text(app, message):
    message.delete(message.chat.id)
    or_ft = message.text.split(".ft ", maxsplit=1)[1]
    ft = or_ft
    ft1 = ft.replace("А","Ꭺ")
    ft2 = ft1.replace("Б","Ꮾ")
    ft3 = ft2.replace("В","Ᏼ")
    ft4 = ft3.replace("Г","Ꮁ")
    ft5 = ft4.replace("Д","Ꭰ")
    ft6 = ft5.replace("Е","Ꭼ")
    ft7 = ft6.replace("Ё","Ё")
    ft8 = ft7.replace("Ж","Ж")
    ft9 = ft8.replace("З","З")
    ft10 = ft9.replace("И","И")
    ft11 = ft10.replace("Й","Й")
    ft12 = ft11.replace("К","Ꮶ")
    ft13 = ft12.replace("Л","Ꮧ")
    ft14 = ft13.replace("М","Ꮇ")
    ft15 = ft14.replace("Н","Ꮋ")
    ft16 = ft15.replace("О","Ꮻ ")
    ft17 = ft16.replace("П","П")
    ft18 = ft17.replace("Р","Ꮲ")
    ft19 = ft18.replace("С","Ꮯ")
    ft20 = ft19.replace("Т","Ꭲ")
    ft21 = ft20.replace("У","Ꭹ")
    ft22 = ft21.replace("Х","Ꮱ")
    ft23 = ft22.replace("Ц","Ц")
    ft24 = ft23.replace("Ч","Ꮞ")
    ft25 = ft24.replace("Ш","Ꮗ ")
    ft26 = ft25.replace("Щ","Ꮗ ")
    ft27 = ft26.replace("Ь","Ꮟ")
    ft28 = ft27.replace("Ы","ᏏᏓ")
    ft29 = ft28.replace("Ъ","Ъ ")
    ft30 = ft29.replace("Э","Э")
    ft31 = ft30.replace("Ю","ᎰᏫ")
    ft32 = ft31.replace("Я","Я")
    ft33 = ft32.replace("a","ᴀ")
    ft34 = ft33.replace("а","ᴀ")
    ft35 = ft34.replace("б","б")
    ft36 = ft35.replace("в","ʙ")
    ft37 = ft36.replace("г","ᴦ")
    ft38 = ft37.replace("д","д")
    ft39 = ft38.replace("е","ᴇ")
    ft40 = ft39.replace("ё","ё")
    ft41 = ft40.replace("ж","ж")
    ft42 = ft41.replace("з","ɜ")
    ft43 = ft42.replace("и","и")
    ft44 = ft43.replace("й","й")
    ft45 = ft44.replace("к","к")
    ft46 = ft45.replace("л","ᴧ")
    ft47 = ft46.replace("м","ʍ")
    ft48 = ft47.replace("н","н")
    ft49 = ft48.replace("о","ᴏ")
    ft50 = ft49.replace("п","ᴨ")
    ft51 = ft50.replace("р","ᴩ")
    ft52 = ft51.replace("с","ᴄ")
    ft53 = ft52.replace("т","ᴛ")
    ft54 = ft53.replace("у","у")
    ft55 = ft54.replace("ш","ɯ")
    ft56 = ft55.replace("щ","щ")
    ft57 = ft56.replace("ь","ь")
    ft58 = ft57.replace("ы","ы")
    ft59 = ft58.replace("ъ","ъ")
    ft60 = ft59.replace("э","϶")
    ft61 = ft60.replace("ю","ю")
    ft62 = ft61.replace("я","я")
    ft63 = ft62.replace("ф","ɸ")
    ft64 = ft63.replace("A","Ꭺ")
    ft65 = ft64.replace("B","Ᏼ")
    ft66 = ft65.replace("C","Ꮯ")
    ft67 = ft66.replace("D","Ꭰ")
    ft68 = ft67.replace("E","Ꭼ")
    ft69 = ft68.replace("F","Ꮀ")
    ft70 = ft69.replace("G","Ꮐ")
    ft71 = ft70.replace("H","Ꮋ")
    ft72 = ft71.replace("I","Ꮖ")
    ft73 = ft72.replace("J","Ꭻ")
    ft74 = ft73.replace("K","Ꮶ")
    ft75 = ft74.replace("L","Ꮮ")
    ft76 = ft75.replace("M","Ꮇ")
    ft77 = ft76.replace("N","N")
    ft78 = ft77.replace("O","Ꮻ")
    ft79 = ft78.replace("P","Ꮲ")
    ft80 = ft79.replace("Q","Ꭷ")
    ft81 = ft80.replace("R","Ꮢ")
    ft82 = ft81.replace("S","Ꮪ")
    ft83 = ft82.replace("T","Ꭲ")
    ft84 = ft83.replace("U","Ꮜ")
    ft85 = ft84.replace("V","Ꮩ")
    ft86 = ft85.replace("W","Ꮃ")
    ft87 = ft86.replace("X","Ꮱ")
    ft88 = ft87.replace("Y","Ꭹ")
    ft89 = ft88.replace("Z","Ꮓ")
    ft90 = ft89.replace("a","ᴀ")
    ft91 = ft90.replace("b","ʙ")
    ft92 = ft91.replace("c","ᴄ")
    ft93 = ft92.replace("d","d")
    ft94 = ft93.replace("e","ᴇ")
    ft95 = ft94.replace("f","f")
    ft96 = ft95.replace("g","g")
    ft97 = ft96.replace("h","h")
    ft98 = ft97.replace("i","i")
    ft99 = ft98.replace("j","j")
    ft100 = ft99.replace("k","ᴋ")
    ft101 = ft100.replace("l","l")
    ft102 = ft101.replace("m","ʍ")
    ft103 = ft102.replace("n","n")
    ft104 = ft103.replace("o","ᴏ")
    ft105 = ft104.replace("p","ᴩ")
    ft106 = ft105.replace("q","q")
    ft107 = ft106.replace("r","r")
    ft108 = ft107.replace("s","s")
    ft109 = ft108.replace("t","ᴛ")
    ft110 = ft109.replace("u","u")
    ft111 = ft110.replace("v","v")
    ft112 = ft111.replace("w","w")
    ft113 = ft112.replace("x","x")
    ft114 = ft113.replace("y","y")
    ft115 = ft114.replace("z","z")
    ft116 = ft115.replace("1","𝟷")
    ft117 = ft116.replace("2","𝟸")
    ft118 = ft117.replace("3","𝟹")
    ft119 = ft118.replace("4","𝟺")
    ft120 = ft119.replace("5","𝟻")
    ft121 = ft120.replace("6","𝟼")
    ft122 = ft121.replace("7","𝟽")
    ft123 = ft122.replace("8","𝟾")
    ft124 = ft123.replace("9","𝟿")
    ft125 = ft124.replace("0","𝟶")
    ft126 = ft125.replace("SUB","SweeUserBot")
    app.send_message(message.chat.id, f"{ft126}")


@app.on_message(filters.command("or", prefixes=".") & filters.me)
def orel_reshka(app, message):
    message.delete(message.chat.id)
    app.send_message(message.chat.id, "⌛️")
    sleep(3)
    
    o_r = ['Монетка показала сторону с решкой', 'Монетка показала сторону с орлом', 'Монетка показала сторону с решкой', 'Монетка показала сторону с орлом', 'Монетка застряла в воздухе', 'Монетка показала сторону с решкой', 'Монетка показала сторону с орлом', 'Монетка показала сторону с решкой', 'Монетка показала сторону с орлом']
    o_r2 = random.choice(o_r)
    app.send_message(message.chat.id, f"{o_r2}")



@app.on_message(filters.command("time", prefixes=".") & filters.me)
def time(app, message):
	while True:
		try:
			time1 = strftime("%H:%M:%S")
			message.edit(f"{time1}")
		
		except FloodWait as e:
			
			sleep(e.x)
			
		sleep(1)

@app.on_message(filters.command("date", prefixes=".") & filters.me)
def date(app, message):
	while True:
		try:
			date1 = strftime("%Y %m %d")
			message.edit(f"{date1}")
		
		except FloodWait as e:
			
			sleep(e.x)
		
		sleep(1)		


@app.on_message(filters.command("timedate", prefixes=".") & filters.me)
def timedate(app, message):
	while True:
		try:
			timedate1 = strftime("%a, %Y/%m/%d %Y:%m:%d")
			message.edit(f"{timedate1}")
			
		except FloodWait as e:
			
			sleep(e.x)
		
		sleep(1)




	
	
@app.on_message(filters.command("timer", prefixes=".") & filters.me)
def  timer(app, message):
	times1 = message.text.split(".timer ", maxsplit=1)[1]
	tm1 = times1
	for i in range(int(tm1)):
	   	message.edit(tm1)
	   	tm1 = int(tm1) - 1
	   	sleep(1)
	app.send_message(message.chat.id, 'Конец таймера')
	

@app.on_message(filters.command("test", prefixes=".") & filters.me)
def test(app, message):
    times2 = message.text.split(".test ", maxsplit=1)[1]
    tm2 = times2
    while int(tm2) > 0:
        try:
            message.edit(message.chat.id, f'{tm2}')
        except FloodWait as e:
            sleep(e.x)
            
        tm2 = int(tm2) - 1
        sleep(1)



@app.on_message(filters.command("pi", prefixes=".") & filters.me)
def phoneinfo(app, message):
    message.delete(message.chat.id)
    pi_text = message.text.split(".pi ", maxsplit=1)[1]
    pi_txt = pi_text
    pi_nomer = pi_txt.replace(" ", "")
    numb_tel_pi = phonenumbers.parse(f'{pi_nomer}')
    if pi_nomer == '+380687891388':
    	app.send_message(message.chat.id, "Ошибка - 69")
    	
    elif pi_nomer == '380687891388':
    	app.send_message(message.chat.id, "Ошибка - 69")
    
    else:
    	valid_pi = phonenumbers.is_valid_number(numb_tel_pi)
    	if valid_pi == False:
    		app.send_message(message.chat.id, 'Не известный номер')
    	elif valid_pi == True:
    		zone_tel = timezone.time_zones_for_number(numb_tel_pi)
    		operator = carrier.name_for_number(numb_tel_pi, 'eu')
    		region = geocoder.description_for_number(numb_tel_pi, 'eu')
    		app.send_message(message.chat.id, f'''Часовой пояс: {' ' .join(zone_tel)}
Оператор: {operator}
Регион: {region}
{numb_tel_pi}

Telegram: http://t.me/{pi_nomer}
Whatsapp: https://transitapp.com/redirect.html?url=whatsapp://send/?phone={pi_nomer}
Viber: https://transitapp.com/redirect.html?url=viber://chat?number={pi_nomer}''')
    	else:
    			app.send_message(message.chat.id, 'Не известная ошибка')



@app.on_message(filters.command("tl", prefixes=".")& filters.me)
def timelove(app, message):
	
	while True:
	           		try:
	           			d1 = message.text.split(".tl ", maxsplit=1)[1]
	           			d2 = d1
	           			
	           			d3 = datetime.datetime.today()
	           			d4 = datetime.datetime.strptime(d1, '%Y/%m/%d %H:%M:%S')
	           			
	           			d5 = d3 - d4
	           			d6 = f'{d5}'
	           			
	           			d7 = d6.replace('days', 'Дней')
	           			d8 = d7[:18]
	           			d9 = d8.replace('.', '')
	           			
	           			message.edit(f"{d9}")
	           		except FloodWait as e:
	           			sleep(e.x)
	           		
	           		sleep(1)


@app.on_message(filters.command("kr", prefixes=".") & filters.me)
def kalcutalor(app, message):
	
	kalcutalor1 = message.text.split(".kr ", maxsplit=1)[1]
	kalcutalor2 = kalcutalor1
	
	kalcutalor3 = eval(kalcutalor2)
	
	message.edit(f"{kalcutalor2} = {kalcutalor3}")




@app.on_message(filters.command("tlm", prefixes=".")& filters.me)
def timeloveme(app, message):
	while True:
	           		try:
	           			d1 = "2021/10/12 18:42:00"
	           			d2 = d1
	           			
	           			d3 = datetime.datetime.today()
	           			d4 = datetime.datetime.strptime(d1, '%Y/%m/%d %H:%M:%S')
	           			
	           			d5 = d3 - d4
	           			d6 = f'{d5}'
	           			
	           			d7 = d6.replace('days', 'Дней')
	           			d8 = d7[:18]
	           			d9 = d8.replace('.', '')
	           			
	           			message.edit(f"{d9}")
	           		except FloodWait as e:
	           			sleep(e.x)
	           		
	           		sleep(1)



@app.on_message(filters.command("277353", prefixes="") & filters.me)
def pasxalka(app, message):
	message.edit("пасхалка!")
	sleep(3)
	app.send_message(message.chat.id, '''⣿⣿⣿⣿⠛⠛⠉⠄⠁⠄⠄⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡇⠄⠄⠄⠐⠄⠄⠄⠄⠄⠄⠄⠠⣿⣿⣿⣿⣿⣿
⣿⣿⡇⠄⢀⡀⠠⠃⡐⡀⠠⣶⠄⠄⢀⣿⣿⣿⣿⣿⣿
⣿⣿⣶⠄⠰⣤⣕⣿⣾⡇⠄⢛⠃⠄⢈⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡇⢀⣻⠟⣻⣿⡇⠄⠧⠄⢀⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣟⢸⣻⣭⡙⢄⢀⠄⠄⠄⠈⢹⣯⣿⣿⣿⣿⣿
⣿⣿⣿⣭⣿⣿⣿⣧⢸⠄⠄⠄⠄⠄⠈⢸⣿⣿⣿⣿⣿
⣿⣿⣿⣼⣿⣿⣿⣽⠘⡄⠄⠄⠄⠄⢀⠸⣿⣿⣿⣿⣿
⡿⣿⣳⣿⣿⣿⣿⣿⠄⠓⠦⠤⠤⠤⠼⢸⣿⣿⣿⣿⣿
⡹⣧⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⢇⣓⣾⣿⣿⣿⣿⣿
⡞⣸⣿⣿⢏⣼⣶⣶⣶⣶⣤⣶⡤⠐⣿⣿⣿⣿⣿⣿⣿
⣯⣽⣛⠅⣾⣿⣿⣿⣿⣿⡽⣿⣧⡸⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡷⠹⠛⠉⠁⠄⠄⠄⠄⠄⠄⠐⠛⠻⣿⣿⣿⣿
⣿⣿⣿⠃⠄⠄⠄⠄⠄⣠⣤⣤⣤⡄⢤⣤⣤⣤⡘⠻⣿
⣿⣿⡟⠄⠄⣀⣤⣶⣿⣿⣿⣿⣿⣿⣆⢻⣿⣿⣿⡎⠝
⣿⡏⠄⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡎⣿⣿⣿⣿⠐
⣿⡏⣲⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢇⣿⣿⣿⡟⣼
⣿⡠⠜⣿⣿⣿⣿⣟⡛⠿⠿⠿⠿⠟⠃⠾⠿⢟⡋⢶⣿
⣿⣧⣄⠙⢿⣿⣿⣿⣿⣿⣷⣦⡀⢰⣾⣿⣿⡿⢣⣿⣿
⣿⣿⣿⠂⣷⣶⣬⣭⣭⣭⣭⣵⢰⣴⣤⣤⣶⡾⢐⣿⣿
⣿⣿⣿⣷⡘⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⢃⣼⣿⣿''')
	sleep(1)
	app.send_message(message.chat.id, '''⠄⠄⠄⠄⠄⠄⠄⠄⣀⣠⣤⣤⣤⣄⡀⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⣠⣿⣿⣿⡿⣿⡿⣗⢌⢳⡀⠄⠄⠄
⠄⠄⠄⠄⠄⣼⣿⡇⣿⠹⡸⡹⣷⡹⡎⣧⢳⠄⠄⠄
⠄⠄⠄⠄⠄⣿⣿⠱⡙⠰⣢⡱⢹⡇⡷⢸⢸⠄⠄⠄
⠄⠄⠄⠄⠄⢿⢸⡈⣉⣤⠠⣴⡄⡇⠁⠄⢸⠄⠄⠄
⠄⠄⠄⠄⠄⠸⡆⡃⡙⢍⣹⡿⢓⠄⠤⣐⡟⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠙⠾⠾⠮⢵⢸⡔⢷⣍⠉⠄⠄⠄⠄
⠄⠄⠄⠄⢀⣴⣾⣿⣷⡶⡋⢞⣎⣚⣭⣴⣶⣶⣤⡀
⠄⠄⠄⠄⢘⣛⣩⣾⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⣿⣷
⠄⠄⣀⠺⣿⣿⣿⠟⣡⣾⠿⢿⣿⣿⡎⢋⠻⣿⣿⣿
⠄⠄⣉⣠⣿⣿⡏⣼⣿⠁⠶⠄⣿⣿⡇⡼⠄⠈⠛⢿
⠄⠄⣈⠻⠿⠟⢁⠘⢿⣷⣶⣾⣿⠟⡰⠃⠄⠄⠄⠄
⠄⣴⣿⣧⢻⣿⣿⣷⣦⣬⣉⣩⣴⠞⠁⠄⠄⠄⠄⠄
⠄⠘⠿⠿⢸⣿⢸⣿⣿⣿⣿⣿⠁⠄⠄⠄⠄⠄⠄⠄
⠄⢤⡝⣧⠘⣿⢸⣿⡿⢻⣿⡿⠄⠄⠄⠄⠄⠄⠄⠄
⣜⢧⠻⣰⢇⣸⢠⣿⡅⣿⠏⣴⣧⡀⠄⠄⠄⠄⠄⠄
⠹⠢⢾⣿⣸⣿⣿⣿⢡⡏⣸⣿⣿⣷⠄⠄⠄⠄⠄⠄
⠄⣷⣦⡉⠛⠻⠿⠿⠾⠿⠿⠿⠛⢋⣁⠄⠄⠄⠄⠄
⢸⣿⣿⣿⣦⡀⠄⠄⠄⢀⣤⣶⣾⣿⣿⡆⠄⠄⠄⠄
⢸⣿⣿⣿⣿⣿⣄⠄⣾⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄
⠸⣿⣿⣿⣿⣿⣿⠄⢿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄
⠄⣿⣿⣿⣿⣿⣿⠄⠈⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄
⠄⢹⣿⣿⣿⣿⡟⠄⠄⠹⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄''')
	sleep(1)
	app.send_message(message.chat.id, '''⠄⠄⠄⠄⠸⣼⢣⢏⡴⠋⣺⣴⣷⠞⠛⢿⣿⠐⠂
⠄⠄⠄⠄⢸⢸⠄⡕⢄⢾⣿⣿⣿⣿⣿⣿⣛⣁⡇
⠄⠄⠄⠄⠈⣇⠃⡉⠉⠅⣿⣿⣿⣿⣿⣟⣍⣀⡃
⠄⠄⠄⠄⠄⣟⠷⡅⢸⣿⣬⣛⡻⠿⣿⣿⣿⡿⠃
⠄⠄⠄⠄⠄⢱⡭⠞⢻⣿⣿⣿⣿⣿⣿⠆⢰⡞⢝⡂
⠄⢀⣀⣤⣤⣶⢴⢃⣿⣿⣿⣿⡏⣿⠟⡄⣌⢷⣖⢭⣀
⣿⣿⣿⣿⣿⣿⠃⣸⣿⣿⣿⡏⢸⢣⣾⣿⡹⣾⠋⣷⠹⡀⠙⡄
⣿⣿⣿⣿⣿⡟⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠙⡣⣿⣆⣗⠄⣿⡄
⢸⣿⣿⣿⠿⡴⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢳⣌⢿⡘⢗⠻⢇⠄
⢸⣧⢩⣕⡔⡄⣿⣿⣿⣿⣷⠻⢫⣼⣿⣿⣿⣧⠘⡮⠓⣷⠠⡱⣤⠙
⠈⢣⡟⡌⠄⢳⢻⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⢏⠦⣧⢣⡟⡀⢸⡉⠉
⠿⠸⢹⣤⠄⠄⠓⡝⢿⣿⣿⠇⣿⣿⣿⠟⡥⠊⣤⠄⠞⣼⣇⠤⠓⠄
⣫⡄⢆⢀⠄⠄⠄⠈⠢⡙⢫⣾⡜⢫⠕⠋⠄⠄⠄⢀⣾⣿⡇
⣿⣿⠈⠣⣗⡀⡄⢆⢀⣨⣞⣥⣊⣀⣀⣀⣤⠴⠚⣿⣿⣿⡇''')
	sleep(1)
	app.send_message(message.chat.id, '''⠄⠄⠄⠄⠄⠄⣠⢼⣿⣷⣶⣾⡷⢸⣗⣯⣿⣶⣿⣶⡄⠄⠄⠄
⠄⠄⣀⣤⣴⣾⣿⣷⣭⣭⣭⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠄⠄
⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⣿⣧⠄⠄
⠄⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢻⣿⣿⡄⠄
⠄⢸⣿⣮⣿⣿⣿⣿⣿⣿⣿⡟⢹⣿⣿⣿⡟⢛⢻⣷⢻⣿⣧⠄
⠄⠄⣿⡏⣿⡟⡛⢻⣿⣿⣿⣿⠸⣿⣿⣿⣷⣬⣼⣿⢸⣿⣿⠄
⠄⠄⣿⣧⢿⣧⣥⣾⣿⣿⣿⡟⣴⣝⠿⣿⣿⣿⠿⣫⣾⣿⣿⡆
⠄⠄⢸⣿⣮⡻⠿⣿⠿⣟⣫⣾⣿⣿⣿⣷⣶⣾⣿⡏⣿⣿⣿⡇
⠄⠄⢸⣿⣿⣿⡇⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣿⣿⣿⡇
⠄⠄⢸⣿⣿⣿⡇⠄⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⠄
⠄⠄⣼⣿⣿⣿⢃⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣿⣿⡇''')
	sleep(1)
	app.send_message(message.chat.id, '''⣿⣿⣿⣿⣿⣿⣿⡇⡌⡰⢃⡿⡡⠟⣠⢹⡏⣦⢸⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⢰⠋⡿⢋⣐⡈⣽⠟⢀⢻⢸⡂⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣋⠴⢋⡘⢰⣄⣀⣅⣡⠌⠛⠆⣿⡄⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣶⣁⣐⠄⠹⣟⠯⢿⣷⠾⠁⠥⠃⣹⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠟⠋⡍⢴⣶⣶⣶⣤⣭⡐⢶⣾⣿⣶⡆⢨⠛⠻⣿⣿⣿
⣿⣿⣿⢏⣘⣚⣣⣾⣿⣿⣿⣿⣿⣿⢈⣿⣿⣿⣧⣘⠶⢂⠹⣿⣿
⣿⣿⠃⣾⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⡀⢿⣿⣿⣿⣿⣿⣿⡇⣿⣿
⣿⣿⡄⣿⣿⣿⣿⣿⣿⡯⠄⠄⠾⠿⠿⢦⣝⠻⣿⣿⣿⣿⠇⣿⣿
⣿⣿⣷⣜⠿⢿⣿⡿⠟⣴⣾⣿⡇⢰⣾⣦⡹⣷⣮⡙⢟⣩⣾⣿⣿
⣿⣿⣿⣿⣿⣆⢶⣶⣦⢻⣿⣿⣷⢸⣿⣿⣷⣌⠻⡷⣺⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡜⢿⣿⡎⢿⣿⣿⡬⣿⣿⣿⡏⢦⣔⠻⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠎⠻⣷⡈⢿⣿⡇⢛⣻⣿⣿⢸⣿⣷⠌⡛⢿⣿
⣿⣿⣿⣿⣿⣿⡏⢰⣷⡙⢷⣌⢻⣿⣿⣿⣿⣿⢸⡿⢡⣾⣿⡶⠻
⣿⣿⣿⣿⣿⡟⣰⣶⣭⣙⠊⣿⣷⣬⣛⠻⣿⣿⠈⣴⣿⣿⣿⠃⠄
⣿⣿⣿⣿⡟⠄⠹⢿⣿⣿⣿⣤⠻⠟⠋⠡⠘⠋⢸⣿⣿⡿⠁⠄⠄
⣿⣿⣿⣿⠁⠄⠄⠄⠙⢻⣿⣿⣇⠄⠄⠄⠄⠄⣺⡿⠛⠄⠄⠄⠄
⣿⣿⣿⡏⠄⠄⠄⠄⠄⠄⠄⠉⠻⠷⠄⢠⣄⠄⠋⠄⠄⠄⠄⠄⠄
⣿⣿⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠸⣿⠄⠄⠄⠄⠄⠄⠄⠄''')
	sleep(1)
	app.send_message(message.chat.id, ''' ⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄ ⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥ ⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿ ⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵ ⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿ ⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁ ⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄ ⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄⠄ ⣶⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⠄ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⢉⢉⠉⠉⠻⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣿⠟⠠⡰⣕⣗⣷⣧⣀⣅⠘⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⠃⣠⣳⣟⣿⣿⣷⣿⡿⣜⠄⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⡿⠁⠄⣳⢷⣿⣿⣿⣿⡿⣝⠖⠄⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⠃⠄⢢⡹⣿⢷⣯⢿⢷⡫⣗⠍⢰⣿⣿⣿⣿⣿ ⣿⣿⣿⡏⢀⢄⠤⣁⠋⠿⣗⣟⡯⡏⢎⠁⢸⣿⣿⣿⣿⣿ ⣿⣿⣿⠄⢔⢕⣯⣿⣿⡲⡤⡄⡤⠄⡀⢠⣿⣿⣿⣿⣿⣿ ⣿⣿⠇⠠⡳⣯⣿⣿⣾⢵⣫⢎⢎⠆⢀⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⠄⢨⣫⣿⣿⡿⣿⣻⢎⡗⡕⡅⢸⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⠄⢜⢾⣾⣿⣿⣟⣗⢯⡪⡳⡀⢸⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⠄⢸⢽⣿⣷⣿⣻⡮⡧⡳⡱⡁⢸⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⡄⢨⣻⣽⣿⣟⣿⣞⣗⡽⡸⡐⢸⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⡇⢀⢗⣿⣿⣿⣿⡿⣞⡵⡣⣊⢸⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⡀⡣⣗⣿⣿⣿⣿⣯⡯⡺⣼⠎⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣧⠐⡵⣻⣟⣯⣿⣷⣟⣝⢞⡿⢹⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⡆⢘⡺⣽⢿⣻⣿⣗⡷⣹⢩⢃⢿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣷⠄⠪⣯⣟⣿⢯⣿⣻⣜⢎⢆⠜⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⡆⠄⢣⣻⣽⣿⣿⣟⣾⡮⡺⡸⠸⣿⣿⣿⣿ ⣿⣿⡿⠛⠉⠁⠄⢕⡳⣽⡾⣿⢽⣯⡿⣮⢚⣅⠹⣿⣿⣿ ⡿⠋⠄⠄⠄⠄⢀⠒⠝⣞⢿⡿⣿⣽⢿⡽⣧⣳⡅⠌⠻⣿ ⠁⠄⠄⠄⠄⠄⠐⡐⠱⡱⣻⡻⣝⣮⣟⣾⣿⠿⠿⠶⠿⢿''')


@app.on_message(filters.command("st", prefixes=".") & filters.me)
def speed_tests(app, message):
     message.edit("Тестирование скорости интернета...")
     ds = st.download()
     us = st.upload()
    
     servernames = []
     st.get_servers(servernames)
    
     message.edit(f'''Download: {memoryconv.convsize(ds)}\nUpload: {memoryconv.convsize(us)}\nPing: {st.results.ping} ms''')



@app.on_message(filters.command("dem", prefixes=".") & filters.me)
def demontivator(app, message):
	dem1 = message.text.split("\n")
	dem2 = dem1[1]
	dem3 = dem1[2]
	ph_id = message.reply_to_message.photo.file_id
	dem4 = app.download_media(message=ph_id,  in_memory=False)
	print(dem4)
	dem = Demotivator(f'{dem2}', f'{dem3}') 
	dem.create(f'{dem4}', font_name="Times New Roman.ttf")
	app.send_photo(message.chat.id, photo='1')


app.run()

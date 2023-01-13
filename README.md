# SweeUserBot

Telegram: [SweeSoft](http://t.me/SweeSoft)

# Установка:
> termux-setup-storage

> apt upgrade && apt update && pkg upgrade && pkg update

> pkg install git && pkg install libjpeg-turbo && pkg install python

> cd /storage/emulated/0/ && git clone https://github.com/TgSweeSoft/SUB && cd SUB

> pip install -r requirements.txt

> LDFLAGS="-L/system/lib64/" CFLAGS="-I/data/data/com.termux/files/usr/include/" pip install simpledemotivators

> python main.py


Когда будете запускать во второй раз:
> cd /storage/emulated/0/SUB && python main.py

# Обновить/переустановить:
> rm -rf /storage/emulated/0/SUB && cd /storage/emulated/0

> git clone https://github.com/TgSweeSoft/SUB

> cd SUB && python main.py

# Установка двумя командами(Не у всех работает!):
> termux-setup-storage

> apt upgrade && apt update && pkg upgrade && pkg update && pkg install git && pkg install libjpeg-turbo && pkg install python && cd /storage/emulated/0/ && git clone https://github.com/TgSweeSoft/SUB && cd SUB && pip install -r requirements.txt && LDFLAGS="-L/system/lib64/" CFLAGS="-I/data/data/com.termux/files/usr/include/" pip install simpledemotivators && python main.py
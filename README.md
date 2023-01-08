# SweeUserBot

TG: [SweeSoft](http://t.me/SweeSoft)

# Установка:
* apt upgrade && apt update
* pkg upgrade && pkg update
* pkg install git && pkg install libjpeg-turbo
* pkg install python
* cd /storage/emulated/0/
* mkdir SUB_SUB && cd SUB_SUB
* git clone https://github.com/TgSweeSoft/SUB
* cd SUB
* pip install -r requirements.txt
* LDFLAGS="-L/system/lib64/" CFLAGS="-I/data/data/com.termux/files/usr/include/" pip install simpledemotivators
* python main.py


Когда будете запускать во второй раз:
* cd /storage/emulated/0/SUB_SUB/SUB
* python main.py

# Обновить/переустановить:
* rm -rf /storage/emulated/0/SUB_SUB
* cd /storage/emulated/0
* mkdir SUB_SUB
* cd /storage/emulated/0/SUB_SUB
* git clone https://github.com/TgSweeSoft/SUB
* cd /storage/emulated/0/SUB_SUB/SUB
* pip install -r requirements.txt
* pkg install libjpeg-turbo
* LDFLAGS="-L/system/lib64/" CFLAGS="-I/data/data/com.termux/files/usr/include/" pip install simpledemotivators
* python main.py


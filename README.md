# SweeUserBot

Telegram: [ROmAanChiG](http://t.me/ROmAanChiG)

Telegram Channel: [SweeSoft](http://t.me/SweeSoft)

# Установка:
* termux-setup-storage
* cd /storage/emulated/0
* pkg install git && git clone https://github.com/TgSweeSoft/SUB && cd SUB && chmod +x install.sh && bash install.sh
* 
Запуск:
* chmod +x SUB.sh && bash SUB.sh

Когда будете запускать во второй раз:
* cd /storage/emulated/0/SUB && bash SUB.sh


# Обновить/переустановить:
* rm -rf /storage/emulated/0/SUB && cd /storage/emulated/0
* git clone https://github.com/TgSweeSoft/SUB
* cd SUB && bash SUB.sh

# Второй способ установки(Не у всех работает!):
* termux-setup-storage
* apt upgrade && apt update && pkg upgrade && pkg update && pkg install git && pkg install libjpeg-turbo && pkg install python && cd /storage/emulated/0/ && git clone https://github.com/TgSweeSoft/SUB && cd SUB && pip install -r requirements.txt && LDFLAGS="-L/system/lib64/" CFLAGS="-I/data/data/com.termux/files/usr/include/" pip install simpledemotivators && bash SUB.sh

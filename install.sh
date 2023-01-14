#! /storage/emulated/0/SUB

BLUE="$(printf '\033[34m')"
BLACK="$(printf '\033[30m')"
GREEN="$(printf '\033[32m')"
ORANGE="$(printf '\033[33m')"
GREENBG="$(printf '\033[42m')"
DEFAULT_BG="$(printf '\033[49m')"

clear
echo "installing SUB.."
sleep 4
clear
echo "update/upgrade apt and pkg.."
sleep 2
clear
apt upgrade -y
apt update -y
pkg upgrade -y
pkg update -y
clear
echo "${BLUE}[${ORANGE}SUB${BLUE}] ${GREEN}Succeful${RED}: ${GREEN}update/upgrade apt and pkg${WHITE}"
sleep 3
clear
echo "indtalling git.."
sleep 2
clear
pkg install git -y
clear
echo "${BLUE}[${ORANGE}SUB${BLUE}] ${GREEN}Succeful${RED}: ${GREEN}installing git${WHITE}"
sleep 3
clear
echo "installing libjpeg-turbo.."
sleep 2
clear
pkg install libjpeg-turbo -y
clear
echo "${BLUE}[${ORANGE}SUB${BLUE}] ${GREEN}Succeful${RED}: ${GREEN}installing libjpeg-turbo${WHITE}"
sleep 3
clear

echo "installing python.."
sleep 2
clear
pkg install python -y
clear
echo "${BLUE}[${ORANGE}SUB${BLUE}] ${GREEN}Succeful${RED}: ${GREEN}installing ${BLUE}pyt${ORANGE}hon${GREEN}${WHITE}"
sleep 3
clear

echo "transition path: '/storage/emulated/0/'.."
sleep 2
clear
cd /storage/emulated/0/
clear
echo "${BLUE}[${ORANGE}SUB${BLUE}] ${GREEN}Succeful${RED}: ${GREEN}transition path: '/storage/emulated/0/'${WHITE}"
sleep 3
clear
echo "cloning repositories: https://github.com/TgSweeSoft/SUB..${WHITE}"
sleep 2
clear
git clone https://github.com/TgSweeSoft/SUB
clear
echo "${BLUE}[${ORANGE}SUB${BLUE}] ${GREEN}Succeful${RED}: ${GREEN}cloning repositories: https://github.com/TgSweeSoft/SUB${WHITE}"
sleep 3
clear
echo "transition dir: 'SUB'.."
sleep 
clear
cd SUB
clear
echo "${BLUE}[${ORANGE}SUB${BLUE}] ${GREEN}Succeful${RED}: ${GREEN}transition dir: 'SUB'${WHITE}"
sleep 3
clear
echo "pip installing requirements.."
sleep 2
clear
pip install -r requirements.txt
echo "${BLUE}[${ORANGE}SUB${BLUE}] ${GREEN}Succeful${RED}: ${GREEN}pip installing requirements${WHITE}"
sleep 3
clear

echo "pip installing Pillow, Simpledemotivators.."
sleep 2
clear
LDFLAGS="-L/system/lib64/" CFLAGS="-I/data/data/com.termux/files/usr/include/" pip install simpledemotivators
clear
echo "${BLUE}[${ORANGE}SUB${BLUE}] ${GREEN}Succeful${RED}: ${GREEN}pip installing Pillow, Simpledemotivators${WHITE}"
sleep 3
clear
echo "Succeful installing✅"
echo " "
echo " "
echo " "
quits () {
    echo; read -p "${BLUE}[${ORANGE}SUB${BLUE}] ${GREEN}Нажмите ${GREENBG}${BLACK} Enter ${DEFAULT_BG}${GREEN} Чтобы завершить bash: ./install.sh${WHITE}";
    clear
    
}
quits
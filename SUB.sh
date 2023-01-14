#! /storage/emulated/0/SUB
#TG: @SweeSoft
## ANSI Colors (FG & BG)
RED="$(printf '\033[31m')"
GREEN="$(printf '\033[32m')"
ORANGE="$(printf '\033[33m')"
BLUE="$(printf '\033[34m')"
MAGENTA="$(printf '\033[35m')"
CYAN="$(printf '\033[36m')"
WHITE="$(printf '\033[37m')"
BLACK="$(printf '\033[30m')"
REDBG="$(printf '\033[41m')"
GREENBG="$(printf '\033[42m')"
ORANGEBG="$(printf '\033[43m')"
BLUEBG="$(printf '\033[44m')"
MAGENTABG="$(printf '\033[45m')"
CYANBG="$(printf '\033[46m')"
WHITEBG="$(printf '\033[47m')"
BLACKBG="$(printf '\033[40m')"
DEFAULT_FG="$(printf '\033[39m')"
DEFAULT_BG="$(printf '\033[49m')"
## accounts:

file="account.txt"




banner () {
    clear
    echo "          $BLUE░██████╗░██╗░░░░░░░██╗███████╗███████╗
          ██╔════╝░██║░░██╗░░██║██╔════╝██╔════╝
          ╚█████╗░░╚██╗████╗██╔╝█████╗░░█████╗░░
          ░╚═══██╗░░████╔═████║░██╔══╝░░██╔══╝░░
          ██████╔╝░░╚██╔╝░╚██╔╝░███████╗███████╗
          ╚═════╝░░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝$ORANGE
██╗░░░██╗░██████╗███████╗██████╗░██████╗░░█████╗░████████╗
██║░░░██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
██║░░░██║╚█████╗░█████╗░░██████╔╝██████╦╝██║░░██║░░░██║░░░
██║░░░██║░╚═══██╗██╔══╝░░██╔══██╗██╔══██╗██║░░██║░░░██║░░░
╚██████╔╝██████╔╝███████╗██║░░██║██████╦╝╚█████╔╝░░░██║░░░
░╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░$WHITE"
}


about_program () {
    clear
    echo "${BLUE}
░█████╗░██████╗░░█████╗░██╗░░░██╗████████╗
██╔══██╗██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝
███████║██████╦╝██║░░██║██║░░░██║░░░██║░░░
██╔══██║██╔══██╗██║░░██║██║░░░██║░░░██║░░░
██║░░██║██████╦╝╚█████╔╝╚██████╔╝░░░██║░░░
╚═╝░░╚═╝╚═════╝░░╚════╝░░╚═════╝░░░░╚═╝░░░"
    sleep 0.3
    echo "${MAGENTA}>>  ${BLUE}S${CYAN}U${MAGENTA}B ${GREEN}полное имя ${BLUE}Swee${CYAN}User${MAGENTA}Bot${GREEN} - это такое"
    sleep 0.3
    echo "приложение для ${GREENBG}${BLACK}Telegram ${DEFAULT_BG}${GREEN} которое работает"
    sleep 0.3
    echo "с помощью ${GREENBG}${BLACK}Telegram API${DEFAULT_BG}${GREEN} а именно ${BLACKBG}${BLUE}pyt${ORANGE}hon${DEFAULT_BG}${GREEN}"
    sleep 0.3
    echo "библиотеки ${GREENBG}${BLACK}Pyrogram${DEFAULT_BG}${GREEN} и имеет более ${MAGENTA}"
    sleep 0.3
    echo "50 ${GREEN}как веселых так и полезных
анимаций или же функций."
    sleep 0.15
    echo " "
    echo " "
    sleep 0.15
    echo "${MAGENTA}>>  ${ORANGE}Author${BLUE}: ${GREEN}ROmAanChig"
    sleep 0.3
    echo "${ORANGE}Twitter${BLUE}: ${GREEN}Coming soon..."
    sleep 0.3
    echo "${ORANGE}Github${BLUE}: ${GREEN}https://github.com/TgSweeSoft/"
    sleep 0.3
    echo "${ORANGE}Reddit${BLUE}: ${GREEN}Coming soon..."
    sleep 0.3
    echo "${ORANGE}Telegram${BLUE}: ${GREEN}https://t.me/ROmAanChiG"
    sleep 0.3
    echo "${ORANGE}Telegram channel${BLUE}: ${GREEN}https://t.me/SweeSoft"
    sleep 0.3
    { echo; read -p "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}Нажмите ${GREENBG}${BLACK} Enter ${DEFAULT_BG}${GREEN} Чтобы вернуться в главное меню."; }
}



start () {
    clear
    echo "${BLUE}[${ORANGE}*${BLUE}] ${GREEN} Загрузка данных.."
    sleep 1
    clear
    echo "${BLUE}[${ORANGE}*${BLUE}] ${GREEN} Загрузка данных пользователя.."
    sleep 2
    clear
    akaunt=`cat $file`
        echo "${BLUE}[${ORANGE}*${BLUE}] ${GREEN} Вход в аккаунт: ${MAGENTA}$akaunt${GREEN}..."
    sleep 2
    clear
    echo "${BLUE}[${ORANGE}*${BLUE}] ${GREEN} Успешно!$WHITE"
    
    python main.py
    exit
    
}

commands () {
    clear
    echo "$ORANGE
📙 Команды: 

1).plus
2).comps
3).care
4).random (0-∞) наример .random 100
5).sls  (с новой строки любое количевство стикеров и скортсть отправки стткеров в милисекундах) например: 
.sls
5
0.1

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
44).st
45).export_session_string
46).dem (с новой строки любой текст и любой текст) например:
.dem
SUB
лучший юзербот

47).fu
48).nrav
49).sauu


"
    { echo; read -p "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}Нажмите ${GREENBG}${BLACK} Enter ${DEFAULT_BG}${GREEN} Чтобы вернуться в главное меню."; }
}


textsesion () {
    echo "$ORANGE
   ░██████╗███████╗░██████╗░██████╗██╗░█████╗░███╗░░██╗
   ██╔════╝██╔════╝██╔════╝██╔════╝██║██╔══██╗████╗░██║
   ╚█████╗░█████╗░░╚█████╗░╚█████╗░██║██║░░██║██╔██╗██║
   ░╚═══██╗██╔══╝░░░╚═══██╗░╚═══██╗██║██║░░██║██║╚████║
   ██████╔╝███████╗██████╔╝██████╔╝██║╚█████╔╝██║░╚███║
   ╚═════╝░╚══════╝╚═════╝░╚═════╝░╚═╝░╚════╝░╚═╝░░╚══╝"
}


textswitch () {
    echo "$BLUE
        ░██████╗░██╗░░░░░░░██╗██╗░█████╗░██╗░░██╗
        ██╔════╝░██║░░██╗░░██║██║██╔══██╗██║░░██║
        ╚█████╗░░╚██╗████╗██╔╝██║██║░░╚═╝███████║
        ░╚═══██╗░░████╔═████║░██║██║░░██╗██╔══██║
        ██████╔╝░░╚██╔╝░╚██╔╝░██║╚█████╔╝██║░░██║
        ╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝"
}


import () {
    clear
    until [[ "$REPLY" =~ ^[6/six]$ ]]; do
    sleep 0.01
    clear
    textswitch
    textsesion
    sleep 0.2
    akauntt=`cat $file`
        echo "    ${BLUE}[${ORANGE}*${BLUE}] ${GREEN} Выбран аккаунт: ${MAGENTA}$akauntt${GREEN}"
    echo " "
    echo "    ${BLUE}[${ORANGE}1${BLUE}] ${GREEN}${MAGENTA}SUB ${ORANGE}- ${GREEN}основной акаунт"
    sleep 0.1
    echo "    ${BLUE}[${ORANGE}2${BLUE}] ${GREEN}${MAGENTA}accounttwo ${ORANGE}- ${GREEN}2 аккаунт"
    sleep 0.1
    echo "    ${BLUE}[${ORANGE}3${BLUE}] ${GREEN}${MAGENTA}accounttree ${ORANGE}- ${GREEN}3 аккаунт"
    sleep 0.1
    echo "    ${BLUE}[${ORANGE}4${BLUE}] ${GREEN}${MAGENTA}accountfour ${ORANGE}- ${GREEN}4 аккаунт"
    sleep 0.1
    echo "    ${BLUE}[${ORANGE}5${BLUE}] ${GREEN}${MAGENTA}accountfive ${ORANGE}- ${GREEN}5 аккаунт"
    sleep 0.1
    echo " "
    echo "    ${BLUE}[${ORANGE}6${BLUE}] ${GREEN}Вернуться в главное меню"
    echo " "
    sleep 0.3
    { read -p ${BLUE}"    [${ORANGE}Выберите параметр${BLUE}]: ${GREEN}"; echo; }

    if [[ "$REPLY" =~ ^[1/one/2/two/3/three/4/four/5/five/6/six]$ ]]; then      #validate input
        if [[ "$REPLY" =~ ^[1/one]$ ]]; then
            echo SUB > account.txt
            clear
            echo "Выбран 1 аккаунт"
            echo " "
            echo " "
            { echo; read -p "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}Нажмите ${GREENBG}${BLACK} Enter ${DEFAULT_BG}${GREEN} Чтобы вернуться в главное меню."; }
        elif [[ "$REPLY" =~ ^[2/two]$ ]]; then
            echo accounttwo > account.txt
            clear
            echo "Выбран 2 аккаунт"
            echo " "
            echo " "
            { echo; read -p "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}Нажмите ${GREENBG}${BLACK} Enter ${DEFAULT_BG}${GREEN} Чтобы вернуться в главное меню."; }
        elif [[ "$REPLY" =~ ^[3/three]$ ]]; then
            echo accounttree > account.txt
            clear
            echo "Выбран 3 аккаунт"
            echo " "
            echo " "
            { echo; read -p "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}Нажмите ${GREENBG}${BLACK} Enter ${DEFAULT_BG}${GREEN} Чтобы вернуться в главное меню."; }
        elif [[ "$REPLY" =~ ^[4/four]$ ]]; then
            echo accountfour> account.txt
            clear
            echo "Выбран 4 аккаунт"
            echo " "
            echo " "
            { echo; read -p "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}Нажмите ${GREENBG}${BLACK} Enter ${DEFAULT_BG}${GREEN} Чтобы вернуться в главное меню."; }
        elif [[ "$REPLY" =~ ^[5/five]$ ]]; then
            echo accountfive > account.txt
            clear
            echo "Выбран 5 аккаунт"
            echo " "
            echo " "
            { echo; read -p "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}Нажмите ${GREENBG}${BLACK} Enter ${DEFAULT_BG}${GREEN} Чтобы вернуться в главное меню."; }
            
        fi
    else
        echo -n "    ${ORANGE}[${RED}!${ORANGE}] ${GREEN}Неверный вариант, попробуйте еще раз."
        sleep 2
        fi
done
   mainmenu; }




comingsoon () {
    clear
    echo "$GREEN Comming Soon..."
    echo " "
    
    { echo; read -p "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}Нажмите ${GREENBG}${BLACK} Enter ${DEFAULT_BG}${GREEN} Чтобы вернуться в главное меню."; }
}

mainmenu () {
    until [[ "$REPLY" =~ ^[none/None]$ ]]; do
    clear
    sleep 0.01
    banner
    sleep 0.2
    echo " "
    echo "    ${BLUE}[${ORANGE}1${BLUE}] ${GREEN}Start"
    sleep 0.1
    echo "    ${BLUE}[${ORANGE}2${BLUE}] ${GREEN}Commands"
    sleep 0.1
    echo "    ${BLUE}[${ORANGE}3${BLUE}] ${GREEN}Coming soon..."
    sleep 0.1
    echo "    ${BLUE}[${ORANGE}4${BLUE}] ${GREEN}Import account"
    sleep 0.1
    echo "    ${BLUE}[${ORANGE}5${BLUE}] ${GREEN}About"
    sleep 0.1
    echo " "
    echo "    ${BLUE}[${ORANGE}6${BLUE}] ${GREEN}Quit"
    echo " "
    sleep 0.3
    { read -p ${BLUE}"    [${ORANGE}Выберите параметр${BLUE}]: ${GREEN}"; echo; }

    if [[ "$REPLY" =~ ^[1/one/2/two/3/three/4/four/5/five/6/six]$ ]]; then      #validate input
        if [[ "$REPLY" =~ ^[1/one]$ ]]; then
            start
        elif [[ "$REPLY" =~ ^[2/two]$ ]]; then
            commands
        elif [[ "$REPLY" =~ ^[3/three]$ ]]; then
            comingsoon
        elif [[ "$REPLY" =~ ^[4/four]$ ]]; then
            import
        elif [[ "$REPLY" =~ ^[5/five]$ ]]; then
            about_program
        elif [[ "$REPLY" =~ ^[6/six]$ ]]; then
            exits
            
        fi
    else
        echo -n "    ${ORANGE}[${RED}!${ORANGE}] ${GREEN}Неверный вариант, попробуйте еще раз."
        sleep 2
    fi
done
}
    
    
exits () {
    clear
    echo "${BLUE}["
    
    sleep 0.2
    clear
    echo "${BLUE}[${ORANGE}*"
    sleep 0.2
    clear
    echo "${BLUE}[${ORANGE}*${BLUE}]"
    sleep 0.2
    clear
    echo "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}Д"
    sleep 0.2
    clear
    echo "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}До"
    
    sleep 0.2
    clear
    echo "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}До "
    sleep 0.2
    clear
    echo "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}До с"
    sleep 0.2
    clear
    echo "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}До св"
    sleep 0.2
    clear
    echo "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}До сви"
    sleep 0.2
    clear
    echo "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}До свид"
    sleep 0.2
    clear
    echo "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}До свида"
    sleep 0.2
    clear
    echo "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}До свидан"
    sleep 0.2
    clear
    echo "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}До свидани"
    sleep 0.2
    clear
    echo "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}До свидания"
    sleep 0.2
    clear
    echo "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}До свидания,"
    sleep 0.2
    clear
    echo "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}До свидания, "
    sleep 0.2
    clear
    echo "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}До свидания, х"
    sleep 0.2
    clear
    echo "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}До свидания, хо"
    sleep 0.2
    clear
    echo "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}До свидания, хор"
    sleep 0.2
    clear
    echo "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}До свидания, хоро"
    sleep 0.2
    clear
    echo "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}До свидания, хорош"
    sleep 0.2
    clear
    echo "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}До свидания, хороше"
    sleep 0.2
    clear
    echo "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}До свидания, хорошег"
    sleep 0.2
    clear
    echo "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}До свидания, хорошего"
    sleep 0.2
    clear
    echo "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}До свидания, хорошего "
    sleep 0.2
    clear
    echo "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}До свидания, хорошего д"
    sleep 0.2
    clear
    echo "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}До свидания, хорошего дн"
    sleep 0.2
    clear
    echo "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}До свидания, хорошего дня"
    sleep 0.2
    clear
    echo "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}До свидания, хорошего дня!"
    sleep 0.01
    clear
    echo "${BLUE}[${ORANGE}*${BLUE}] ${GREEN}До свидания, хорошего дня!"
    exit 0
    
}




main () {
    mainmenu
}

main
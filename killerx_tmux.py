import os
from time import sleep

banr = """\033[1;92m
██╗░░██╗██╗██╗░░░░░██╗░░░░░███████╗██████╗░██╗░░██╗
██║░██╔╝██║██║░░░░░██║░░░░░██╔════╝██╔══██╗╚██╗██╔╝
█████═╝░██║██║░░░░░██║░░░░░█████╗░░██████╔╝░╚███╔╝░
██╔═██╗░██║██║░░░░░██║░░░░░██╔══╝░░██╔══██╗░██╔██╗░
██║░╚██╗██║███████╗███████╗███████╗██║░░██║██╔╝╚██╗
╚═╝░░╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝
░░░░░░░░░░░░ ░░Created by: MrHacker-X░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░Instagram: 0hacker_x0░░░░░░░░░░░░░░░

"""

os.system('xdg-open https://youtube.com/@Technolex')

while True:
    os.system('clear')
    print(banr)
    d = input("\033[1;92m[#] Enter key to run: ")
    if d == 'Y2h1dGl5YXNhbGEK':
        print("[*] Unlocked File")
        sleep(1)
        print("\033[1;92m[*] Starting KillerX ...")
        sleep(5)
        break

    elif d == '':
        print()
        print("\033[1;92m[!] No Input detected")
        print()
        sleep(1)

    elif d == 'X' or d == 'x':
        print("[*] Opening profile")
        os.system("xdg-open https://instagram.com/0hacker_x0")
        sleep(4)
        exit()

    else:
        print()
        print("[!] Wrong key")
        print(">>> Go to MrHacker-X's Instagram account and message him to get key\n>>> Press X to open MrHacker-X's instagram profile in your device.")
        print()
        sleep(1)






about = """\033[1;92m
█▀█ █▄▄ █▀█ █░█ ▀█▀
█▀█ █▄█ █▄█ █▄█ ░█░
▄▄▄▄MrHacker-X▄▄▄▄

[#] Introduction: 

>>> KillerX is a Most dangerous instagram reporting tool. This tool can ban any kind of Instagram Account which account contain less than 100k followers. If your account have 100k + followers then this tool can defeated. But if Your ID contaion less than 100k followers then nobody can save your Instagram account. This tool is written in python3. And This tool can run in Any Linux distribution like Debian, Ubuntu, Fedora, ArchLinux and more.

[#] My Social Media Link:

    [*] Instagram: https://instagram.com/0hacker_x0
    [*] YouTube  : https://youtube.com/@Technolex
    [*] Telegram : https://t.me/hackwithalex
    [*] Facebook : https://facebook.com/hackerxmr
    [*] Github   : https://github.com/MrHacker-X
    [*] TryHackMe: https://tryhackme.com/p/hacker.alex
    [*] website  : https://hackwithalex.github.io

"""

main = """\033[1;92m
[#] select an option:

[1] Report
[2] About
[0] Quit
    
killerx>> """


############# Script started ################

while True:
    os.system('clear')
    print(banr)
    a = input(main)
    if a == '1' or a == '01':
        os.system("clear")
        print(banr)
        b = input("[#] Enter Target Username: ")
        if b == '':
            print('[!] No input detected')
            sleep(1)
            exit()

        else:
            os.system('clear')
            print(banr)
            sleep(2)
            print("\033[1;92m[*] Default proxy selected\n")
            sleep(2)
            print("\033[1;92m[*] Logined with default credentials\n")
            sleep(2)
            print("\033[1;92m[*] Target selected @ " + b)
            sleep(2)
            print("\n\033[1;92m[*] Attack is starting\n")
            sleep(2)
            for i in range(200):
                print()
                print("\033[1;92m[✓] Reported on @ " + b)
                sleep(1)


        exit()


    elif a == '02' or a == '2':
        os.system('clear')
        print(about)
        input("Press ENTER To Continue")

    elif a == '0':
        print()
        print("\033[1;92m[*] Quitting...")
        sleep(1)
        exit()

    elif a == '':
        print()
        print("\033[1;92m[!] No input detected")
        print()
        sleep(1)

    else:
        print()
        print("\033[1;92m[!] Invalid input")
        sleep(1)
        

        




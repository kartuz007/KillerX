# coding=utf-8
#!/usr/bin/env python3

from colorama import Fore, Back, Style
from os import path
import re
import random
from requests import get
from sys import exit
import time
import os
        
def print_success(message, *argv):
    print(Fore.GREEN + "[~] " + Style.RESET_ALL + Style.BRIGHT, end="")
    print(message, end=" ")
    for arg in argv:
        print(arg, end=" ")
    print("")

def print_error(message, *argv):
    print(Fore.RED + "[!] " + Style.RESET_ALL + Style.BRIGHT, end="")
    print(message, end=" ")
    for arg in argv:
        print(arg, end=" ")
    print("")

def print_status(message, *argv):
    print(Fore.BLUE + "[*] " + Style.RESET_ALL + Style.BRIGHT, end="")
    print(message, end=" ")
    for arg in argv:
        print(arg, end=" ")
    print("")

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

def parse_proxy_file(fpath):
    if (path.exists(fpath) == False):
        print("")
        print_error("\033[1;91m Proxy file not found!")
        print_error("\033[1;92m Quitting...")
        exit(0)
    
    proxies = []
    with open(fpath, "r") as proxy_file:
        for line in proxy_file.readlines():
            line = line.replace(" ", "")
            line = line.replace("\r", "")
            line = line.replace("\n", "")
            
            if (line ==  ""):
                continue
            
            proxies.append(line)
    
    if (len(proxies) > 50):
        proxies = random.choices(proxies, 50)
        
    print("")
    print_success(str(len(proxies)) + " Proxies have been installed!")

    return proxies



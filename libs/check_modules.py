# coding=utf-8
#!/usr/bin/env python3

import sys

def check_modules():
    try:
        import requests
    except:
        print("\033[1;91m[-] 'requests' module not found!")
        print("\033[1;97m[*] Type 'pip install requests [socks]' to install")
        sys.exit(0)

    try:
        import colorama
    except Exception as e:
        print("\033[1;91m[-] 'colorama' package not installed!")
        print("\033[1;97m[*] Type 'pip install colorama' to install")
        print(e)
        sys.exit(0)

    try:
        import asyncio
    except:
        print("\033[1;91m[-] 'asyncio' package not installed!")
        print("\033[1;97m[*] Type 'pip install asyncio' to install")
        sys.exit(0) 

    try:
        import proxybroker
    except:
        print("\033[1;91m[-] 'proxybroker' package not installed!")
        print("\033[1;97m[*] Type 'pip install proxybroker' to install")
        sys.exit(0)

    try:
        import warnings
    except:
        print("\033[1;91m[-] 'warnings' package not installed!")
        print("\033[1;97m[*] Type 'pip install warnings' to install")
        sys.exit(0)

    import warnings
    warnings.filterwarnings("ignore")

    from colorama import init
    init()

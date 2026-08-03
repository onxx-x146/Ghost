import os
# Linux / Termux / macOS
os.system("clear")
import sys
import time
import re
import pyshorteners
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor
import subprocess
from datetime import datetime

current_time = datetime.now().strftime("%H:%M:%S")

print(f"\033[38;5;214m[{current_time}]\033[0m \033[1;32m[INFO]:\033[0m BY HARI OPEN")

try:
    subprocess.run([
        "am",
        "start",
        "-a", "android.intent.action.VIEW",
        "-d", "https://www.instagram.com/_insrnx_",
        "com.android.chrome"
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

except subprocess.CalledProcessError:
    print(f"\033[38;5;214m[{current_time}]\033[0m \033[1;33m[WARNING]:\033[0m BY OPEN.")
    
VERSION = "V1.3"

telegram = "https://t.me/onxx12"
github = "https://github.com/onxx-x146"
'clear'
R = '\033[31m'
G = '\033[32m'
C = '\033[36m'
Y = '\033[33m'
W = '\033[0m'
'clear'
banner = r'''
   ________  ______  _________________
  / ____/ / / / __ \/ ___/_  __/_  __/
 / / __/ /_/ / / / /\__ \ / /   / /
/ /_/ / __  / /_/ /___/ // /   / /
\____/_/ /_/\____//____//_/   /_/
    
       👻  Ghost by HARI  ⚔️
     ☢️ End is the Beginning ☢️
'''
def show_banner():
    print(f"{R}{banner}{R}")
    print(f"{G}Version : {W}{VERSION}")
    print(f"{G}Telegram: {W}{telegram}")
    print(f"{G}GitHub  : {W}{github}")
    print()

def loading():
    frames = ["⣾","⣽","⣻","⢿","⡿","⣟","⣯","⣷"]
    for _ in range(6):
        for f in frames:
            sys.stdout.write(f"\r{C}Generating ed links {f}{W}")
            sys.stdout.flush()
            time.sleep(0.1)
    print()

def tool_info():

    print(f"""{R}

👻 Ghost Info ⚔️
-------------------------
Tool       : URL ing Tool
Version    : {VERSION}
Creator    : Digital ONXX

Platforms  : Kali Linux / Termux

Description:
Ghost s URLs using
multiple shorteners to create
clean redirect links.

Telegram   : {telegram}
GitHub     : {github}

Tagline    : End is the Beginning
-------------------------
{W}""")

def _url(domain, keyword, url):
    parsed = urlparse(url)
    return f"{parsed.scheme}://{domain}-{keyword}@{parsed.netloc}{parsed.path}"

def generate():

    while True:
        web_url = input(f"{G}Enter original URL {W}(ex: https://example.com): ")
        if re.match(r'^(https?://)', web_url):
            break
        print(f"{R}Invalid URL format{W}")

    while True:
        domain = input(f"{Y}Enter custom domain {W}(ex: gmail.com): ")
        if "." in domain:
            break
        print(f"{R}Invalid domain{W}")

    while True:
        keyword = input(f"{Y}Enter ing keyword {W}(ex: login): ")
        if " " not in keyword and len(keyword) <= 15:
            break
        print(f"{R}Invalid keyword{W}")

    loading()

    s = pyshorteners.Shortener()

    shorteners = [
        s.tinyurl,
        s.dagd,
        s.clckru,
        s.osdb
    ]

    def shorten(service):
        try:
            return service.short(web_url)
        except:
            return None

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(shorten, shorteners))

    short_urls = [r for r in results if r]

    print(f"\n{R}Original URL:{W} {web_url}\n")
    print(f"{G}Generated ed URLs:{W}")

    for i, url in enumerate(short_urls):
        ed = _url(domain, keyword, url)
        print(f"{C}[{i+1}]{W} {ed}")

def menu():

    while True:

        print(f"""
{G}------------------------------
        👻 Ghost
------------------------------
[1] Generate ed URL
[2] Tool Info
[3] Exit
------------------------------{W}
""")

        choice = input("Select option > ")

        if choice == "1":
            generate()

        elif choice == "2":
            tool_info()

        elif choice == "3":
            print("Exiting Ghost...")
            sys.exit()

        else:
            print("Invalid option")

show_banner()
menu()
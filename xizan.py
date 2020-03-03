# !/usr/bin/python3
# -*- coding:utf-8 -*-

import requests
import telegram
import re


# from telegram.ext import Updater
# from telegram.ext import CommandHandler
# Q@7BCIStP5It12 Q@7BCIStP5It12
# login_url = 'https://pro.crosswall.cc/auth/login'
# check_url = 'https://pro.crosswall.cc/user/checkin'
# get_cell = 'https://pro.crosswall.cc/user'
sites = [
    {"name": "隔壁西站", "checkin": "https://pro.crosswall.cc/user/checkin", "login": "https://pro.crosswall.cc/auth/login",
     "user": "https://pro.crosswall.cc/user", "auth": {"email": "imyxiaocai@gmail.com", "passwd": "Q@7BCIStP5It12"}},
    {"name": "魅影", "checkin": "https://maying.co/user/checkin", "login": "https://maying.co/auth/login",
     "user": "https://maying.co/user", "auth": {"email": "imyxiaocai@gmail.com", "passwd": "S8c7i6CfkMJEL2x"}}
]

head = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Mobile Safari/537.36'}
form_data = {"email": "imyxiaocai@gmail.com", "passwd": "Q@7BCIStP5It12"}


def ss_check(site):
    s = requests.Session()
    login = s.post(site["login"], data=site["auth"], headers=head)
    if login.status_code == 200:

        resp = s.post(site["checkin"])
        res = 'fail'
        if resp.status_code == 200:
            # print(resp.text)
            res = resp.json()['msg']
            res = ｓite["name"] + ':\n' + res
            # print(res)
        cell_data = s.get(site["user"])
        if cell_data.status_code == 200:
            user = cell_data.text
            # print(user)
            # \s*(剩余|可用)(里程|流量|\s\d.+?%|：))[^B]+/)
            pattern = re.compile(r'(剩余|可用)(里程|流量|量)(:|：)[\s\r\n]*\d+(\.\d+)?[MGT]B')
            data = re.search(pattern, user)
            if data:
                data = data.group().split()

                res += '\n' + data[0] + data[-1]
        # print(data)
        return res


for site in sites:
    result = ss_check(site)
    bot = telegram.Bot(token='634725318:AAHyQ-QqiatPIIyyTwP-iuUmlNcXj2Ts6sM')
    bot.send_message(chat_id=351605510, text=result)



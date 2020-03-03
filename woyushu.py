# !/usr/bin/python3
# -*- coding:utf-8 -*-


import requests
# import gevent
# from gevent import monkey
import telegram

# monkey.patch_all()


class Check_in(object):

    def __init__(self, sign_url, check_url, form_data, name):
        self.sign_url = sign_url
        self.check_url = check_url
        self.form_data = form_data
        self.name = name
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Mobile Safari/537.36'}
        self.s = requests.Session()

    def checkin(self):
        login = self.s.post(self.sign_url, data=self.form_data, headers=self.header)
        if login.status_code == 200:
            res = self.s.get(self.check_url)

            return res.text if res.status_code == 200 else 'error'
        else:
            return 'error'

    def run(self):
        res = self.checkin()
        res = self.name + res
        # print(res)
        bot = telegram.Bot(token='634725318:AAHyQ-QqiatPIIyyTwP-iuUmlNcXj2Ts6sM')
        bot.send_message(chat_id=-270181072, text=res, parse_mode='Markdown')
        # https://api.telegram.org/bot634725318:AAHyQ-QqiatPIIyyTwP-iuUmlNcXj2Ts6sM/getUpdates


if __name__ == '__main__':
    wys_site = Check_in('http://www.woyushu.com/deal/login',
                        'http://www.woyushu.com/User/signin',
                        {'email': '2827265241@qq.com', 'password': '1!Ov^b%&jGqBEIdqYB'},
                        '*Yxiaocai* 我与书签到：\n'
                        )
    clj_wys_site = Check_in('http://www.woyushu.com/deal/login',
                            'http://www.woyushu.com/User/signin',
                            {'email': 'cyffuture@gmail.com', 'password': '5JgluAa77QCZ'},
                            '*Edward* 我与书签到：\n'
                            )
    wys_site.run()
    clj_wys_site.run()
    # g1 = gevent.spawn(wys_site.run)
    # g2 = gevent.spawn(clj_wys_site.run)
    # gevent.joinall([g1, g2])
    # print('done')
    # print(clj_wys_site.run()

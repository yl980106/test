# !/usr/bin/python3
# -*- coding:utf-8 -*-


import requests
from lxml import etree
import telegram


class Jww(object):
    """教务网信息抓取"""
    def __init__(self):
        self.url = 'http://jwbinfosys.zju.edu.cn/default2.aspx'
        self.headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Mobile Safari/537.36",}
        self.bot = telegram.Bot(token='634725318:AAHyQ-QqiatPIIyyTwP-iuUmlNcXj2Ts6sM')
        self.id = 351605510

    def get_html(self):
        resp = requests.get(self.url, headers=self.headers)
        return resp.text.encode('utf8').decode('utf8')

    def parse_html(self, html_str):
        html = etree.HTML(html_str)
        table = html.xpath('//table[@id="DataGrid1"]')[0]
        a_list = table.xpath('.//a[@onclick]')
        content = list()
        for a in a_list:
            title = a.xpath('./text()')[0].strip()
            file = a.xpath('./@onclick[1]')[0].split(',')[0].replace('window.open(','').replace('\'','')
            # 判断 title是否存在的逻辑
            with open('/root/tgbot/tz.txt', 'r') as f:
                last = f.read().strip()
                # print(last)
            if title == last:
                break
            if title != last:
                content.append([title, file])
        
        return content

    def send_news(self, content):
        if len(content) > 0:
            with open('/root/tgbot/tz.txt', 'w') as f:
                f.write(content[0][0])
            text = ''
            for news in content:
                text += '[{}]({})'.format(*news)
                text += '\n'
            # print(text)
            self.bot.sendMessage(chat_id=self.id, text=text, parse_mode='Markdown')
                # print(news)
            # print(content)

    def run(self):
        # 1.发送请求
        html_str = self.get_html()
        # print(html_str)
        # 2.解析内容
        content = self.parse_html(html_str)
        
        # 4. 发送内容
        self.send_news(content)
        # 通知逻辑
    

if __name__ == '__main__':
    jww = Jww()
    jww.run()

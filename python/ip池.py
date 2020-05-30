# -*- coding: utf-8 -*-
# 抓取代理 ip  西刺代理
import requests  # 请求
from bs4 import BeautifulSoup  # 解析 HTML
from fake_useragent import UserAgent  # 假代理
import time
import random

import re
if __name__ == '__main__':
    file = open('python/ip.txt', 'w', encoding='utf-8')
    session = requests.Session()
    ua = UserAgent()
    url = 'https://www.xicidaili.com/nn/'  # 待爬取网址
    request = session.get(url,  headers={'User-Agent': str(ua.random)})
    html = BeautifulSoup(request.text, 'html.parser')
    tr_list = html.find_all('tr')
    max_page = int(html.find('div', class_='pagination').find_all('a')[-2:-1][0].get_text())
   
    def acquire(num):
        """
        获取每页 ip

        num:页码 从 2 开始
        """
        request = session.get(
            url='https://www.xicidaili.com/nn/'+str(num), headers={'User-Agent': str(ua.random)})
        html = BeautifulSoup(request.text, 'html.parser')
        tr_list = html.find_all('tr')
        for item in tr_list[1:]:
            file.write(item.find_all('td')[5].string.lower(
            )+'://' + item.find_all('td')[1].string+':'+item.find_all('td')[2].get_text()+'\n')

    for i in range(max_page)[2:11]:
        acquire(i)
        time.sleep(10)
        print('%.1f %%' % (i/(max_page-1)*100),end='\r')
    for item in tr_list[1:]:
        file.write(item.find_all('td')[5].string.lower(
        )+'://' + item.find_all('td')[1].string+':'+item.find_all('td')[2].get_text()+'\n')

    file.close()
    print('***********完成****************')

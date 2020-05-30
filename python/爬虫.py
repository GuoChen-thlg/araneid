# -*- coding: utf-8 -*-
# https://www.veer.com/photo
# 储存为json
# Veer 图库 网站 photo类

import requests  # 请求
from bs4 import BeautifulSoup  # 解析 HTML
from fake_useragent import UserAgent  # 假代理
if __name__ == '__main__':
    session = requests.Session()
    ua = UserAgent()
    url = 'https://www.veer.com/photo/'  # 待爬取网址
    header = {'User-Agent': str(ua.random)}  # 随机生成 代理
    request = session.get(url, headers=header)
    html = BeautifulSoup(request.text, 'html.parser')
    pictureSet = []  # 图集
    clipper_list = html.find_all('div', class_='clipper')
    a_list = BeautifulSoup(str(clipper_list), 'html.parser').find_all('a')
    file = open('python/mapDepot.json', 'w', encoding='utf-8')
    file.write('[')
    i = 0
    for a_item in a_list:
        i = i+1
        z_request = session.get(
            url="https://www.veer.com" + a_item["href"], headers=header)
        z_img_box_list = BeautifulSoup(z_request.text, 'html.parser').find_all(
            'article', class_='mosaic_asset')
        for item in z_img_box_list:
            pictureSet.append({
                "name": item.img['alt'],
                "url": item.img['src']
            })
        file.write("{'title': '"+str(a_item["title"])+"','href': 'https://www.veer.com" +
                   a_item['href']+"',  "'pictureSet'":" + str(pictureSet) + "},")
        print('%.1f%%' % (i / len(a_list) * 100), end='\r')
    file.write(']')
    file.close()
    print('\n*****************************完成*******************************')

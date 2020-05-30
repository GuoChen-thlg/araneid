# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


# https://www.laomiao.com.cn/Home/Product/index/pid/41.html

url = 'https://www.laomiao.com.cn/Home/Product/index/pid/41.html'

request = requests.get(url)
html = BeautifulSoup(request.text, 'html.parser').find(
    'div', id='proInxContent')
a_list =html.find_all('a')

print ( html.get_text())
# for a_item in a_list:
#     print(a_item.find('div', class_='img_box').find('img')['src'])
#     print(a_item.find(class_='product_title').get_text().strip())



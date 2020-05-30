# -*- coding: utf-8 -*-
# 导包开始
import requests  # 导入 requests 包
import re
import json
from bs4 import BeautifulSoup

# 导包结束
# 配置开始
url = 'https://jdguoshu.jd.com/'  # 待爬取的网址
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
proxies = {
    
}

# 配置结束
# 开始获取数据
strhtml = requests.get(url, headers=headers)  # Get方式获取网页数据


# 获取数据结束


# encode(strhtml.encoding).decode('gbk').encode('utf-8').decode('utf-8')









# 数据处理
soup = BeautifulSoup(strhtml.text, 'lxml')

data = soup.select(
    '.j-module.d-goods > ul > li')
# for item in data:
#     result = {
#         'title': item.get_text(),
#         'link': item.get('href'),
#         'ID': re.findall('\d+', item.get('href'))
#     }
print(soup)



txt = open('C:\\Users\\Administrator\\Desktop\\Daily-project\\python\\txt.html',
           'w', encoding='utf-8')
txt.write(str(data)+'\n')
txt.close()


print('--------------------------采集结束---------------------------------')

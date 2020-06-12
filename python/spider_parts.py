# -*- coding: utf-8 -*-

import requests  # 请求
from bs4 import BeautifulSoup  # 解析 html
from fake_useragent import UserAgent  # 代理
from requests.exceptions import ConnectionError, Timeout, HTTPError
from retrying import retry

def get_ua():
    '''
    随机返回 代理
    '''
    return {'User-Agent': UserAgent().random}


def Beautiful_Soup(text):
    '''
    返回 HTML 解析对象

    text:响应文本
    '''
    return BeautifulSoup(text, 'html.parser')

# @retry()
def requests_gethtml(url):
    """
    返回 HTML 解析对象

    url:网址
    """
    try:
        r = requests.get(url, headers=get_ua())
        if r.status_code == 200:
            if r.encoding == 'ISO-8859-1':
                return Beautiful_Soup(r.text.encode("iso-8859-1").decode('gbk').encode('utf8'))
            else:
                r.encoding='utf-8'
                return Beautiful_Soup(r.text)
        else:
            print(url+'：请求失败！')
    except HTTPError:
        print(url+'：请求失败！')
    except Timeout:
        print(url+'：请求超时！')
    except ConnectionError:
        print(url + '：建立连接失败！')






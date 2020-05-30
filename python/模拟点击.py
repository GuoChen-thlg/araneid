# -*- coding: utf-8 -*-

# https://www.xn--frlovningsring-vpb.se/ringar
from selenium import webdriver
from pyquery import PyQuery as pq




browser = webdriver.Chrome()  # 打开浏览器
browser.get('https://www.xn--frlovningsring-vpb.se/ringar')  # 进入网站
html=browser.page_source # 获得源码

data=str(pq(html)) # 解析源码
i=0
while i<10:
    browser.find_element_by_class_name('view-more-button').click()
    i=i+1
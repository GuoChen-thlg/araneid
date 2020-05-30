# -*- coding: utf-8 -*-

# 分类链接抓取

# https://www.zales.com/

import requests
from lxml import etree
import re
from fake_useragent import UserAgent
import pandas as pd

url = 'https://www.zales.com'
menuUrl = 'https://www.zales.com/content/megamenu/desktop'
ua = UserAgent()
head = {'User-Agent': str(ua.random)}

res = requests.get(menuUrl, headers=head)

root = etree.HTML(res.text)
mainMenu = root.xpath('//div[@class="col-xs-12 btn-collection text-center"]/a/@href')
proInfoAll = pd.DataFrame()
for i in range(len(mainMenu)):
    inUrl = mainMenu[i]
    response = requests.get(inUrl, headers=head)
    ro = etree.HTML(response.text)
    num = ro.xpath('//span[@class="searchstring"]/span/strong/text()')
    name = ro.xpath('//span[@class="searchstring"]/span[0]/h1/strong/text()')

    print("=======================雅菲妮爬虫程序开始进行=============")
    print('分类页：' + str(name))
    print('应该抓取产品数：' + str(num))

    proUrlPat = '<a class="thumb main-thumb" href="(.*?)" title=".*?" itemprop="url">.*?<img itemprop="image".*?class="img-responsive js-lazyload"'
    proUrlList = re.findall(proUrlPat, response.text, re.S)

    x = 0
    for proUrl in proUrlList:
        proUrlList[x] = url + proUrl
        x += 1

    for j in range(len(proUrlList)):
        detailUrl = proUrlList[j]
        resp = requests.get(detailUrl, headers=head)
        print(resp)
        rhtml = etree.HTML(resp.text)
        imgPat = '<a href="#" class="item"> <img  loading="lazy" class="lazyOwl" src=".*?" data-src="(.*?)" alt=".*?"></a> '
        imgList = re.findall(imgPat, resp.text)
        y = 0
        for img in imgList:
            imgList[y] = url + img.replace('100', '600')
            y += 1
        title = rhtml.xpath('//h1[@class="name"]/text()')
        sku = rhtml.xpath('//span[@id="productCodeDetail"]/b/text()')
        origPat = '<div class="priceLabel 1">Orig&nbsp;(.*?)</div>'
        nowPat = '<span class="priceLabel price-red 2">Now&nbsp;(.*?)</span>'
        oriPrice = re.findall(origPat, resp.text)
        nowPrice = re.findall(nowPat, resp.text)
        descPat = '<div itemprop="description"><p class="description">(.*?)</p></div>'
        desc = re.findall(descPat, resp.text)

        pic1 = imgList[0].split(',')
        # pic2 = imgList[1].split(',')
        # pic3 = imgList[2].split(',')
        type = name
        productUrl = detailUrl.split(',')
        proInfo = pd.DataFrame([title, type, productUrl, oriPrice, nowPrice, desc, sku, pic1]).T
        proInfo.columns = ['title', 'type', 'productUrl', 'oriPrice', 'nowPrice', 'desc', 'sku', 'pic1']
        proInfoAll = pd.concat([proInfoAll, proInfo])

    print("=======================雅菲妮该分类页爬虫结束=============")

proInfoAll.to_csv('list.csv')

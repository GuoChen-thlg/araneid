# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
from utf8 import getUtf8


if __name__ == '__main__':

    book = []
    booktext=''
    ToClimbTheUrl = 'http://www.biqukan.com/1_1094'  # 待爬取网址

    request = requests.get(url=ToClimbTheUrl)

    html = getUtf8(request) 
    div = BeautifulSoup(html, features="lxml").find_all(
        'div', class_='listmain')
    a_list = BeautifulSoup(str(div[0]), features="lxml").find_all('a')
    i=0
    for aItem in a_list[13:]:
        # book.append({
        #     'name': aItem.string,
        #     'url': 'https://www.biqukan.com'+str(aItem.get('href'))
        # })
        i=i+1
        print('%.1f%%' % (i/len(a_list)*100))
        request1 = requests.get(
            url='https://www.biqukan.com' + str(aItem.get('href')))
        div1 = BeautifulSoup(getUtf8(request1), features="lxml", from_encoding="utf-8").find_all(
            'div', class_='showtxt')
        texts = str(div1).replace('<br/>', '').replace(' ', '')
        booktext = booktext+'***************  ******************'+str(texts)
        # if i == 5:
        #     break

# txt = open('C:\\Users\\Administrator\\Desktop\\Daily-project\\python\\txt.txt',
#            'w', encoding='utf-8')

# txt.write(str(booktext)+'\n')
# txt.close()

print('--------------------------------------结束---------------------------------------------')

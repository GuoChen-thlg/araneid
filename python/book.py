# -*- coding: utf-8 -*-
# 趣笔阁
# https://www.12zw.com/xiaoshuodaquan/

from spider_parts import requests_gethtml
import time
import random
file = None


def chapter(url, name):
    '''
    获得章节内容
    '''
    global file
    file.write('\n********************%s********************\n' % name)
    try:
        txt = requests_gethtml(url).find('div', id='content').get_text()
    except AttributeError:
        pass
    finally:
        pass
    file.write(txt)


def book(url, name):
    '''
    获得书籍内容

    url:url
    name:书籍名
    '''
    global file
    i = 0
    # 章节 列表
    chapters_list = requests_gethtml(url).find('div', id='list').find_all('a')
    file = open('python/xhxs/'+name+'.txt', 'w', encoding='utf-8')
    file.write('\n《《《《《《《《《《《《《《《%s》》》》》》》》》》》》》》》\n' % name)
    for chapter_item in chapters_list:
        print('%.2f%%' % (i/len(chapters_list)*100), end='\r')
        i = i+1
        time.sleep(random.random())
        chapter(url+chapter_item['href'], chapter_item.get_text())
    file.close()

def books():
    """
    获得书籍列表

    """
    div_llis = requests_gethtml(
        url='https://www.12zw.com/xiaoshuo1/').find('div', class_='llis')
    # 数组 书名及url
    books_list = div_llis.find_all('li')
    for book_item in books_list:
        book(book_item.a['href'], book_item.get_text().replace('/','_作者：'))




if __name__=='__main__':
    books()

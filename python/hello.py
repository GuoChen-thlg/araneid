# -*- coding:utf-8 -*-
# 打印 输出
# num = input("请输数字：")
# num=int(num)
# if num > 0:
#     print('num > 0')

# else:
#     print('num < 0')


# 编码转换

# print(ord('A'))

# print(chr(65))

# print('中文'.encode('utf-8'))

# print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8', errors='ignore'))

# 字符串和编码

# print('你好，%s ,现在 %d 点了 ，今天 %.2f 度' % ('小明',5,30.5))

# list tuple

# alist=['a','b','c','d']
# alist.append('e')  # 追加元素
# alist.insert(0,'f')# 指定位置插入元素
# print(len(alist))  # 查看 list 长度

# alist.pop()  # 删除末尾元素
# alist.pop(0)  # 删除指定位置元素
# alist[0]='z' # 替换指定位置元素
# print(alist)

# blist = ['1', '2', alist]
# print(blist)

# list 可变  相对不安全  tuple 不可变 安全
# list 声明 a=[]  tuple 声明 b=()

# atuple = (1,)
# print(atuple)

# if else
# age=int(input('请输入你的出生日期：'))
# if age>2000:
#     print('00后')
# else:
#    print('00前')


# 循环
# sun=0
# for item in range(101):
#     sun = sun+item

# print(sun)
# i = 100
# number = 0
# while i > 0:
#     number = number+i
#     i = i - 1

#     if i < 50:
#         break
# print(number)


# dict

# adict = {'a': 1, "b": 3}
# print(adict['b'])
# print('a' in adict)
# print('c'in adict)
# print(adict.get('a', 13))
# print(adict.get('d'))
# print(adict.get('d',13))


# s = set([ 2, 3,4,3,2,1])
# print(s)
# add 添加
# remove 删除

#
# a = 'abc'
# print(a.replace('a',"A"))


# 函数
# def pri(a,b,c,d):
#     return a,b,c,d


# q, w, e, r = pri(1, 2, 3, 4)
# print(q, w, e, r)

# import math

# print(math.sqrt(9))


#必选参数、默认参数、可变参数、命名关键字参数和关键字参数

# def wn(a,b='2',*c,d,**e):
#     print('a：',a,'b:',b,'c:',c,'d:',d,'e：',e)

# wn('1',c=[1,2,3,4],d='9999',e='op')


# txt = open('C:\\Users\\Administrator\\Desktop\\Daily-project\\python\\txt.txt',
#            'w', encoding='utf-8')

# txt.write('123fsdf65sfd \n')
# txt.close()

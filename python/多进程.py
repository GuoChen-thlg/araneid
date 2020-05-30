# -*- coding: utf-8 -*-

import time
import threading


def loop():
    # 开始 子线程
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

# 主线程
print('thread %s is running...' % threading.current_thread().name)
# 创造线程
t = threading.Thread(target=loop, name='LoopThread')
# 启动
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

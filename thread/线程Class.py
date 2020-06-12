# -*- coding: utf-8 -*-



import threading
import time

num=10

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开启线程： " + self.name)
        # 获取锁，用于线程同步
    #    threadLock.acquire()
        print_time(self.name, self.counter)
        # 释放锁，开启下一个线程
        # threadLock.release()


def print_time(threadName, delay):
    global num
    while num > 0:
        time.sleep(delay)
        print("%s: %s***%s" % (threadName, time.ctime(time.time()), num))
        threadLock.acquire()
        num-=1
        threadLock.release()

threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")

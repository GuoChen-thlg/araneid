# -*- coding: utf-8 -*-


import threading
import time

exitFlag = 0


class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print("退出线程：" + self.name)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s" % (threadName))
        counter -= 1
i=0
while i < 10:
    i+=1
    # 创建新线程
    thread1 = myThread(1, "Thread"+str(i), 1)
    # 开启新线程
    thread1.start()
    thread1.join()

print("退出主线程")

import _thread
import time

#创建一个线程函数
def print_time(threadName,delay):
    count = 0
    while count<5:
        time.sleep(delay)
        count+=1
        print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

#创建两个线程
try:
    _thread.start_new_thread(print_time,("thread1",2,))
    _thread.start_new_thread(print_time,("thread2",4,))
except:
    print("线程启动错误")

while 1:
    pass

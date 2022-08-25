"""
线程创建演示2
"""
from threading import Thread
from time import sleep


# 含有参数的线程函数
def fun(sec, name):
    print("含有参数的线程")
    sleep(sec)
    print("%s 线程执行完毕" % name)


# 创建多个线程
jobs = []
for i in range(5):
    t = Thread(target=fun, args=(2,), kwargs={"name": "T%d" % i})
    jobs.append(t)
    t.start()
# 回收线程
[x.join() for x in jobs]

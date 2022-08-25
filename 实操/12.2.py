"""
线程对象的属性
"""
from threading import Thread
from time import sleep


def fun():
    sleep(3)
    print("线程属性测试")


t = Thread(target=fun)
t.setDaemon(True)# start前设置，这个线程随主线程退出
t.start()

t.setName("tarena")
print("Name:", t.getName())
print("is alive:", t.is_alive())

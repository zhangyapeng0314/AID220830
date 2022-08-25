"""
线程Event
"""
from threading import Thread

import lock as lock

lock = lock
a = b = 0


def value():
    while True:
        lock.acquire()
        if a != b:
            print("a = %d,b = %d" % (a, b))
        lock.release()


t = Thread(target=value)
t.start()

while True:
    lock.acquire()
    a += 1
    b += 1
    lock.release()
# while True:
#     with lock:  # 上锁
#         a += 1
#         b += 1
#         # 语句块结束自动解锁
t.join()

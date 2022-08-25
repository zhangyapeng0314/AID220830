"""
线程实例
"""
from threading import Thread

from lock import lock

lock1 = lock()
lock2 = lock()


def print_num():
    # 每次循环打印两个数字
    for i in range(1, 53, 2):
        lock1.acquire()  # 上锁
        print(i)
        print(i + 1)
        lock2.release()  # 解锁


def print_char():
    for i in range(65, 91):
        lock2.acquire()  # 上锁
        print(chr(i))
        lock1.release()  # 解锁


t1 = Thread(target=print_num)
t2 = Thread(target=print_char)

lock.acquire()  # 让数字先执行


t1.start()
t2.start()
t1.join()
t2.join()

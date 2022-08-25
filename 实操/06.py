"""
进程相关函数
创建多个子进程
"""
import os
import sys
from multiprocessing import Process
from time import sleep


def th1():
    sleep(3)
    print("吃饭")
    print(os.getppid(), '---', os.getpid())


def th2():
    sleep(2)
    sys.exit("不睡觉了")
    print("睡觉")
    print(os.getppid(), '---', os.getpid())


def th3():
    sleep(5)
    print("打豆豆")
    print(os.getppid(), '---', os.getpid())


things = [th1, th2, th3]
jobs = []  # 用于存储启动的进程对象
if __name__ == '__main__':
    # 创建循环进程
    for th in things:
        p = Process(target=th)
        jobs.append(p)
        p.start()
    # 统一回收
    for i in jobs:
        i.join()

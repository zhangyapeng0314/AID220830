"""
练习1：模拟售票系统
现有500张票，记为T1--T500，放在一个列表里面
有10个窗口，记为w1--w10，每张票卖出需要0.1秒
创建10个线程，模拟10个窗口，票的出票顺序必须是1--500
每张票卖出时 打印 w2-----T203

编程创建10，线程模拟这个过程
"""
from threading import Thread
from time import sleep

# 存储票
ticket = ["T%d" % i for i in range(1, 501)]
# print(ticket)


# 模拟每个窗口的卖票情况,W窗口编号
def sell(w):
    while ticket:
        print("%s---%s" % (w, ticket.pop(0)))  # pop（0）弹出第一个，pop（）弹出最后一个
        sleep(0.1)


jobs = []
for i in range(1, 11):
    t = Thread(target=sell, args=("w%d" % i,))
    jobs.append(t)
    t.start()

[i.join() for i in jobs]

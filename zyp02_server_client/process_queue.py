"""
进程通信
"""
from multiprocessing import Queue, Process

# 创建消息队列,必须在父进程里面
q = Queue(maxsize=2)


def request():
    name = "zyp"
    passwd = "123"
    # 存入消息队列
    q.put(name)
    q.put(passwd)


def handle():
    name = q.get()
    passwd = q.get()
    print("用户名：", name)
    print("密码：", passwd)


if __name__ == '__main__':

    p1 = Process(target=request)
    p2 = Process(target=handle)
    p1.start()
    p2.start()
    p1.join()
    p2.join()



"""
进程池
注意：父进程退出，进程池自动销毁
   事件函数的声明要在创建进程池之前
"""
from multiprocessing import Pool
from time import sleep, ctime


# 进程池执行事件
def worker(msg, sec):
    print(ctime(), "----", msg)
    sleep(sec)


if __name__ == '__main__':

    # 创建进程池
    pool = Pool(10)
    # 向进程池中加入事件
    for i in range(100):
        msg = "Tedu-%d" % i
        pool.apply_async(func=worker, args=(msg, 4))  # 事件开始执行
    pool.close()  # 关闭进程池，不能添加新的事件
    pool.join()  # 等事件都执行完，回收进程池

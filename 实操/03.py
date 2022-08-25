"""
【1】 将需要新进程执行的事件封装为函数
【2】 通过模块的Process类创建进程对象，关联函数
【3】 通过进程对象调用start启动进程
【4】 通过进程对象调用join回收进程资源
"""
import multiprocessing
from time import sleep


# 进程执行函数
def fun():
    print("开始执行进程函数......")
    sleep(2)
    print("进程函数执行完了.")

if __name__ == '__main__':

    # 创建进程对象
    P = multiprocessing.Process(target=fun)
    # 启动进程，进程诞生，执行fun函数内容
    P.start()
    fun()
    # 等待执行完成后回收
    P.join()


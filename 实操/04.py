"""
【1】 将需要新进程执行的事件封装为函数
【2】 通过模块的Process类创建进程对象，关联函数
【3】 通过进程对象调用start启动进程
【4】 通过进程对象调用join回收进程资源
"""
from multiprocessing import Process
from time import sleep


# 带参数的进程函数
def worker(sec, name):
    for i in range(3):
        sleep(sec)
        print("I'm%s" % name)
        print("I'm working...")



# 位置传参
# P = Process(target=worker, args=(2,"Levi"))
#关键字传参
p=Process(target=worker,args=(2,),kwargs={"name":"Baron"})
if __name__ == '__main__':
    p.start()
    p.join(3)
    print("=======")

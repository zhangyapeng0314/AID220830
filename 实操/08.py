"""
练习1：编写一个程序
* 使用单进程求100000以内质数之和，记录所用时间
* 使用4个进程，将100000拆分成4份，分别求每部分中质数之和，记录所用时间
* 使用10个进程，将100000拆分成10份，分别求每部分中质数之和，记录所用时间
"""
import time
from multiprocessing import Process


# 求函数运行时间(装饰器)
def timeis(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = f(*args, **kwargs)
        end_time = time.time()
        print("运行时间：", end_time - start_time)
        return res

    return wrapper


# 判断一个数是不是质数
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# 单一进程
# @timeis
# def no_process():
#     prime = []
#     for i in range(1, 10001):
#         if isPrime(i):
#             prime.append(i)  # 将质数加入列表
#     print(sum(prime))
#
#
# no_process()  # 运行时间： 0.4328935146331787
class Prime(Process):
    def __init__(self, begin, end):
        """
        :param begin:开始值
        :param end: 结尾值
        """
        self.begin = begin
        self.end = end
        super().__init__()

    def run(self) -> None:
        prime = []
        for i in range(self.begin, self.end):
            if isPrime(i):
                prime.append(i)
        print(sum(prime))



if __name__ == '__main__':
    @timeis
    def process_4():
        jobs = []
        for i in range(1, 100001, 25000):
            p = Prime(i, i + 25000)
            jobs.append(p)
            p.start()
        for i in jobs:
            i.join()


# 运行时间： 15.319210529327393

    process_4()

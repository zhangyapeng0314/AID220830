"""
 自定义进程类
"""
from multiprocessing import Process


# 自定义类
class MyProcess(Process):
    def __init__(self, val):
        self.val = val
        super().__init__()  # 加载父类属性

    def fun1(self):
        print("步骤1：假设很复杂", self.val)

    def fun2(self):
        print("步骤2：假设也很复杂", self.val)

    # 重新run,将其作为一个新进程的执行内容
    def run(self) -> None:
        self.fun1()
        self.fun2()

if __name__ == '__main__':

    process = MyProcess(2)
    process.start()  # 启动进程，执行run
    process.join()

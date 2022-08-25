"""
练习：拷贝一个目录
编写程序完成，将一个文件夹拷贝一份
1.假设文件夹只有普通文件
2.将每个文件的拷贝作为一个拷贝事件
3.使用进程池完成事件
提示：os.mkdir('name')
"""
import os
import sys
from multiprocessing import Pool, Queue

q = Queue()  # 创建消息队列


# 进程池执行事件,拷贝文件，子进程
def copy(file, old_folder, new_folder):
    fr = open(old_folder + '/' + file, 'rb')  # 打开旧文件
    fw = open(new_folder + '/' + file, 'wb')  # 打开新文件
    while True:  # 边读边写
        data = fr.read(1024*10)
        if not data:  # 读到空了
            break
        n = fw.write(data)  # 写入多少就是拷贝多少
        q.put(n)  # 放入消息队列
    fr.close()  # 关闭旧文件
    fw.close()  # 关闭新文件


# 获取文件夹的大小
def get_size(dir):
    total_size = 0
    for file in os.listdir(dir):
        total_size += os.path.getsize(dir + "/" + file)
    return total_size


# 使用进程池，父进程
def main():
    old_folder = input("请输入你要拷贝的目录:")
    # 文件夹大小
    total_size = get_size(old_folder)
    new_folder = old_folder + "-备份"
    try:
        os.mkdir(new_folder)
    except:
        sys.exit("该目录已经存在")

    # 创建进程池
    pool = Pool()
    # 向进程池中加入事件,遍历目录，确定要拷贝的文件
    for file in os.listdir(old_folder):
        pool.apply_async(func=copy, args=(file, old_folder, new_folder))

    copy_size = 0
    while copy_size <= total_size:
        copy_size += q.get()  # 从消息队列获取数值累加
        print("拷贝了 %.2f%%" % (copy_size / total_size * 100))
    pool.close()  # 关闭进程池，不能添加新的事件
    pool.join()  # 等事件都执行完，回收进程池


if __name__ == '__main__':
    main()

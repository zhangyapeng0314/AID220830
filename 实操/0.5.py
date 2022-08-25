"""
练习：大文件拆分
将一个大文件拆分为两个部分，每个部分分别是文件的一半，
即原文件的上下部分，分别拆分到一个新的文件里面
要求使用两个进程同时进行
提示：按照文件的字节数计算文件大小
    os.path.getsize()
思路；获取文件的大小，上下两个部分的拆分分别封装为函数
"""
import os
from multiprocessing import Process

size = os.path.getsize("E:/Pycharm/project/zyp02_server_client/zly.jpeg")  # 获取文件大小


# 复制上半部分
def top():
    fr = open("E:/Pycharm/project/zyp02_server_client/zly.jpeg", 'rb')
    fw = open("top.jpg", 'wb')
    n = size // 2  # 要拷贝n个字节
    while n >= 1024:
        fw.write(fr.read(1024))
        n -= 1024
    else:
        fw.write(fr.read(n))
    fr.close()
    fw.close()


# 复制下半部分
def bot():
    fr = open("E:/Pycharm/project/zyp02_server_client/zly.jpeg", 'rb')
    fw = open("bot.jpg", 'wb')
    fr.seek(size // 2, 0)
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()



if __name__ == '__main__':
    p = Process(target=top)
    p.start()
    bot()
    p.join()

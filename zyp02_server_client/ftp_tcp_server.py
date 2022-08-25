"""
ftp文件服务 服务端
多线程并发模型
"""
import os
import time
from socket import *
from threading import Thread

# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)  # 服务器地址
# 文件库
FTP = "E:/FTP/"


# 处理客户端请求
class FTPServer(Thread):
    def __init__(self, connfd):
        super().__init__()
        self.connfd = connfd

    def do_list(self) -> object:
        # 判断文件库是否为空
        file_list = os.listdir(FTP)
        if not file_list:
            self.connfd.send(b"Fail")  # 列表为空
            return
        else:
            self.connfd.send(b"OK")
            time.sleep(0.1)
            data = "\n".join(file_list)
            self.connfd.send(data.encode())

    # 处理下载
    def do_get(self, filename):
        try:
            f = open(FTP + filename, "rb")
        except:
            # 文件不存在报异常
            self.connfd.send(b"Fail")
            return
        else:
            # 文件打开成功
            self.connfd.send(b"OK")
            time.sleep(5)
            # 发送文件
            while True:
                data = f.read(1024)
                if not data:
                    time.sleep(5)
                    self.connfd.send(b"##")  # 文件发送完毕
                    break
                self.connfd.send(data)
                print(data.decode())
            f.close()

    # 处理上传
    def do_put(self, filename):
        if os.path.exists(FTP + filename):
            self.connfd.send(b"Fail")
            return
        else:
            self.connfd.send(b"OK")
            # 接受文件
            f = open(FTP + filename, 'wb')
            while True:
                data = self.connfd.recv(1024)
                # print(data.decode(("utf8","ignore"))
                if data == b"##":
                    break
                f.write(data)
            f.close()

    # 作为一个线程内容处理某个客户端的请求
    def run(self):
        # 总分模式
        while True:
            # 某个client所有的请求
            data = self.connfd.recv(1024).decode()
            # 根据不同的请求做不同处理
            if not data or data == "exit":
                self.connfd.close()  # 某个客户端退出对应的套接字就关闭
                return
            elif data == "LIST":
                self.do_list()
            elif data[:4] == "RETR":
                filename = data.split(" ")[-1]
                self.do_get(filename)
            elif data[:4] == "STOR":
                filename = data.split(" ")[-1]
                self.do_put(filename)


def main():
    # tcp套接字创建
    sock = socket()
    sock.bind(ADDR)
    sock.listen(5)
    print("Listen the port %s" % PORT)

    # 循环连接
    while True:
        try:
            connfd, addr = sock.accept()
            print("Connfd from", addr)
        except KeyboardInterrupt:
            sock.close()
            return

        # 为连接进来的客户端创建单独的线程
        t = FTPServer(connfd)
        t.daemon = True  # 父进程退出,子进程终止服务
        t.start()


if __name__ == '__main__':
    main()

"""
ftp文件服务 客户端
"""
# 服务器地址
import sys
import time
from socket import socket

ADDR = ("127.0.0.1", 8888)


# 实现具体的请求功能
class FTPClient():
    def __init__(self, sock):
        self.sock = sock

    def do_list(self):
        self.sock.send(b"LIST")  # 发送请求
        result = self.sock.recv(1024).decode()  # 回复 字符串
        print(result)
        # 根据回复分情况讨论
        if result == "OK":
            # 接受文件列表
            file = self.sock.recv(1024 * 1024).decode()
            print(file)

        else:
            print("文件库为空")
            return

    # 下载文件
    def do_get(self, filename):
        data = "RETR " + filename
        self.sock.send(data.encode())  # 发送请求
        # 等待反馈
        result = self.sock.recv(1024).decode()
        print(result)
        if result == "OK":
            # 接受文件
            f = open(filename, 'wb')
            while True:
                data = self.sock.recv(1024)
                print(data.decode())
                if data == b"##":
                    break
                f.write(data)
            f.close()
        else:
            print("文件不存在")

    # 上传文件
    def do_put(self, filename):
        # 本地判断，防止文件路径写错
        try:
            f = open(filename, "rb")
        except:
            print("该文件不存在")
            return
        # 上传put后可能是路径，提取真正的文件名
        filename = filename.split('/')[-1]
        data = "STOR " + filename
        self.sock.send(data.encode())  # 发送请求
        # 等待反馈
        result = self.sock.recv(1024).decode()
        print(result)
        if result == "OK":
            # 发送文件
            while True:
                data = f.read(1024)
                if not data:
                    time.sleep(5)
                    self.sock.send(b"##")  # 文件发送完毕
                    break
                self.sock.send(data)
                # print(data.decode(("utf8","ignore"))
            f.close()
        else:
            print("文件已经存在")

    # 退出
    def do_exit(self):
        self.sock.send(b"exit")
        self.sock.close()
        sys.exit("谢谢使用")


def main():
    # 创建tcp套接字
    sock = socket()
    sock.connect(ADDR)
    # 实例化功能类对象
    ftp = FTPClient(sock)

    while True:
        print("=========命令选项==========")
        print("***         list      ***")
        print("***      get file     ***")
        print("***      put file     ***")
        print("***         exit     ***")
        print("========================")

        cmd = input("请输入命令：")
        if cmd == "list":
            ftp.do_list()
        elif cmd[:3] == "get":
            filename = cmd.split(" ")[-1]  # 提取文件名
            ftp.do_get(filename)
        elif cmd[:3] == "put":
            filename = cmd.split(" ")[-1]  # 提取文件名
            ftp.do_put(filename)
        elif cmd == "exit":
            ftp.do_exit()
        sock.send(cmd.encode())


if __name__ == '__main__':
    main()

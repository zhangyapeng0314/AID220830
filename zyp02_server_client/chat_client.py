"""
chat client
发送请求，得到结果
"""
import sys
from multiprocessing import Process
from socket import *

# 服务器的地址
ADDR = ("127.0.0.1", 8001)


# 请求进入聊天室
def login(sock):
    while True:
        name = input("请输入你的姓名：")
        msg = "L " + name  # 根据通信协议整理发送信息
        sock.sendto(msg.encode(), ADDR)
        result, addr = sock.recvfrom(1024)
        if result.decode() == "OK":
            print("您已进入聊天室")
            return name
        else:
            print("你的名字太受欢迎了，换一个吧")


# 接受消息
def recv_msg(sock):
    while True:
        data, ADDR = sock.recvfrom(2048)
        print("\n" + data.decode() + "\n我：", end="")


# 发送消息
def send_msg(sock, name):
    while True:
        try:
            msg = input("我：")
        except KeyboardInterrupt:
            msg = "exit"

        if msg == "exit":
            data = "E " + name
            sock.sendto(data.encode(), ADDR)
            sys.exit("您已经退出聊天室")
        data = "C %s %s" % (name, msg)
        sock.sendto(data.encode(), ADDR)


def main():
    sock = socket(AF_INET, SOCK_DGRAM)  # 创建UDP套接字
    # sock.bind('0.0.0.0',5555)
    name = login(sock)  # 进入聊天室
    # 为聊天创建一个子进程
    p = Process(target=recv_msg, args=(sock,))
    p.daemon = True  # 父进程退出子进程也退出
    p.start()
    send_msg(sock, name)
    p.close()


if __name__ == '__main__':
    main()

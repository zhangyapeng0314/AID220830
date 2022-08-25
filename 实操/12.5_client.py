"""
聊天室客户端
"""
import sys
from multiprocessing import Process
from socket import *

# 服务器地址
ADDR = ("127.0.0.1", 5550)


def login(sock):
    while True:
        name = input("Name:")
        msg = "L " + name
        sock.sendto(msg.encode(), ADDR)
        result, addr = sock.recvfrom(1024)
        if result.decode() == 'OK':
            print("您已经进入聊天室")
            return name
        else:
            print("您的名字太受欢迎了，请换一个")


def recv_msg(sock):
    while True:
        data, addr = sock.recvfrom(2048)
        print("\n", data.decode() + "\n我：", end="")


def send_msg(sock, name):
    while True:
        try:
            msg = input("我：")
        except KeyboardInterrupt:
            msg = 'exit'
        if msg == 'exit':
            data = 'E ' + name
            sock.sendto(data.encode(), ADDR)
            sys.exit("您已经退出了")
        data = "C %s %s" % (name, msg)
        sock.sendto(data.encode(), ADDR)


def main():
    sock = socket(AF_INET, SOCK_DGRAM)
    name = login(sock)
    p = Process(target=recv_msg, args=(sock,))
    p.daemon = True
    p.start()
    send_msg(sock, name)


if __name__ == '__main__':
    main()

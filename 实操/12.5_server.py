"""
聊天室服务端
"""

from socket import *

# 服务器使用地址
HOST = "0.0.0.0"
PORT = 5550
ADDR = (HOST, PORT)

# 存储用户信息
user = {}


def do_login(sock, name, address):
    if name in user or "管理" in name:
        sock.sendto(b"Fail", address)
        return
    else:
        sock.sendto(b"OK", address)
        msg = "欢迎%s进入聊天室" % name
        for i in user:
            sock.sendto(msg.encode(), user[i])
        user[name] = address
        print(user)


def do_chat(sock, name, content):
    msg = "%s:%s" % (name, content)
    for i in user:
        if i != name:
            sock.sendto(msg.encode(), user[i])


def do_exit(sock, name):
    del user[name]
    msg = "%s退出聊天室" % name
    for i in user:
        sock.sendto(msg.encode(), user[i])


def main():
    sock = socket(AF_INET, SOCK_DGRAM)
    global ADDR
    sock.bind(ADDR)
    while True:
        data, addr = sock.recvfrom(1024)
        tmp = data.decode().split(' ', 2)
        # print(data.decode())
        # print(tmp)

        # 根据请求调用不同的函数
        if tmp[0] == 'L':
            do_login(sock, tmp[1], addr)
        elif tmp[0] == 'C':
            do_chat(sock, tmp[1], tmp[2])
        elif tmp[0] == 'E':
            do_exit(sock, tmp[1])




if __name__ == '__main__':
    main()

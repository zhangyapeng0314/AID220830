"""
author:zyp
email:1729486966@qq.com
time:2022-7-28
env:python3
socket and Process exercise
"""
from multiprocessing import Process
from socket import *

# 服务器使用地址
HOST = "0.0.0.0"
PORT = 8001
ADDR = (HOST, PORT)
# 存储用户{name:address.....}
user = {}


# 处理进入聊天室
def do_login(sock, name, address):
    if name in user or "管理" in name:
        sock.sendto(b"FAIL", address)
        return
    else:
        sock.sendto(b"OK", address)
        # 通知其他人
        msg = "欢迎%s进入聊天室" % name
        for i in user:
            sock.sendto(msg.encode(), user[i])
        # 存储用户
        user[name] = address
        print(user)


# 处理聊天
def do_chat(sock, name, content):
    msg = "%s:%s" % (name, content)
    for i in user:
        # 刨除本人
        if i != name:
            sock.sendto(msg.encode(), user[i])


# 退出
def do_exit(sock, name):
    del user[name]  # 移除这个人
    # 通知其他人
    msg = "%s退出聊天室" % name
    for i in user:
        sock.sendto(msg.encode(), user[i])


# 子进程执行
def handle(sock):
    # 循环接受客户端请求
    while True:
        # 接受请求(所有用户的所有请求)
        data, addr = sock.recvfrom(1024)
        temp = data.decode().split(' ', 2)  # 对请求内容进行解析
        # 根据请求调用不同函数处理
        if temp[0] == 'L':
            # temp ==>[L,name]
            do_login(sock, temp[1], addr)  # 调用方法处理具体事件
        elif temp[0] == "C":
            # temp==>[C,name,xxxxxxx]
            do_chat(sock, temp[1], temp[2])
        elif temp[0] == "E":
            # temp==>[E,name]
            do_exit(sock, temp[1])


# 启动函数
def main():
    sock = socket(AF_INET, SOCK_DGRAM)  # 创建UDP套接字
    global ADDR
    sock.bind(ADDR)

    # # 创建一个新的进程，用于分担功能
    # p = Process(target=handle, args=(sock,))
    # p.daemon = True
    # p.start()
    # # 父进程发送管理员消息
    # # while True:
    # #     content = input("管理员消息：")
    # #     # 服务端整个退出
    # #     if content == "quit":
    # #         break
    # #     data = "C 管理员消息" + content
    # #     sock.sendto(data.encode(),ad)
    # p.close()


if __name__ == '__main__':
      main()

"""
基于select的 IO多路复用并发模型
重点代码
"""
from select import select
from socket import *
from time import sleep


# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)  # 服务器地址
# 创建三个对象，帮助监控
tcp_sock = socket()
tcp_sock.bind(ADDR)
tcp_sock.listen(5)
print(tcp_sock)
# 设置为非阻塞,防止网络卡顿
tcp_sock.setblocking(False)
# IO对象监控列表
rlist = [tcp_sock]  # 初始监听对象
wlist = []
xlist = []
# 循环监听
while True:
    # 对关注的IO循环监控
    rs, ws, xs = select(rlist, wlist, xlist)
    # 对返回值rs分情况讨论 监听套接字 客户端连接套接字
    for r in rs:
        if r is tcp_sock:
            # 处理客户端连接
            connfd, addr = r.accept()
            print("Connect from", addr)
            connfd.setblocking(False)  # 设置非阻塞
            rlist.append(connfd)
        else:
            # 收消息
            data = r.recv(1024)
            if not data:
                # 客户端退出
                rlist.remove(r)
                r.close()
                continue
            print(data.decode())
            # r.send(b"OK")
            wlist.append(r)  # 放入写列表
    for w in ws:  # (一般很少用到写操作)
        w.send(b"OK")  # 发送消息
        wlist.remove(w)  # 如果不移除会不断地写

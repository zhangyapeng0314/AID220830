"""
基于poll方法实现IO多路复用
"""
from select import *
from socket import *

# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)  # 服务器地址

# 创建套接字
tcp_sock = socket()
tcp_sock.bind(ADDR)
tcp_sock.listen(5)

# 设置为非阻塞,防止网络卡顿
tcp_sock.setblocking(False)

# IO对象监控列表
p = poll()  # 建立poll对象

p.register(tcp_sock, POLLIN)  # 初始监听对象
# 准备工作,建立文件描述符 和 IO对象对应的字典,时刻与register的IO一致
map = {tcp_sock.fileno(): tcp_sock}

# 循环监听
while True:
    # 对关注的IO循环监控
    events = p.poll()
    # events-->[(fileno,event),()......]
    for fd, event in events:
        # 分情况讨论
        if fd == tcp_sock.fileno():
            # 处理客户端连接
            connfd, addr = map[fd].accept()
            print("Connect from", addr)
            connfd.setblocking(False)  # 设置非阻塞
            p.register(connfd, POLLIN)  # 添加到监控
            map[connfd.fileno()] = connfd  # 同时维护字典
        else:
            # 收消息
            data = map[fd].recv(1024)
            if not data:
                # 客户端退出
                p.unregister(fd)  # 移除关注
                map[fd].close()
                del map[fd]  # 从字典也移除

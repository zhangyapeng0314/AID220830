"""
tcp 客户端演示
"""
from socket import *


# 发送消息
while True:
    msg = input("我：")
    if not msg:
        break
    # 创建套接字
    tcp_socket = socket()
    # 发起连接,连接服务端
    tcp_socket.connect(("127.0.0.1", 8899))
    tcp_socket.send(msg.encode())  # 发送字节串
    data = tcp_socket.recv(1024)
    print(data)
    print("小美:", data.decode())  # 转换字符串
    # 关闭
    tcp_socket.close()

"""
udp_server.py udp服务端简单实例
"""
from socket import *

# 创建udp的套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)
# 绑定地址
udp_socket.bind(("0.0.0.0", 8888))
# 接受一个消息
while True:
    data, addr = udp_socket.recvfrom(5)
    print(addr, "收到：", data.decode())  # bytes->str
    udp_socket.sendto(b"Thanks", addr)
# 关闭套接字
udp_socket.close()

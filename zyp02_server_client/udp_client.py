"""
udp_client.py 客户端
"""
from socket import *

# 确定服务端地址
ADDR = ("127.0.0.1", 8888)
# 创建套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 循环收发内容
while True:
    msg = input(">>")
    if not msg:
        break  # 输入为空退出
    udp_socket.sendto(msg.encode(), ADDR)
    data, addr = udp_socket.recvfrom(1024)
    print("从服务端收到:", data.decode())
# 关闭
udp_socket.close()

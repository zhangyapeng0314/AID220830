"""
udp_client.py 客户端
"""
from socket import *

# 确定服务端地址
ADDR = ("127.0.0.1", 11111)
# 创建套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 循环收发内容
while True:
    word = input(">>")
    if not word:
        break  # 输入为空退出
    # 发送单词
    udp_socket.sendto(word.encode(), ADDR)
    data, addr = udp_socket.recvfrom(1024)
    print("%s:%s" % (word, data.decode()))
print("退出程序")
# 关闭
udp_socket.close()

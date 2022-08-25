"""
select io 多路复用
"""
from select import select
from socket import *

# 创建两个对象，帮助监控
tcp_sock = socket()
tcp_sock.bind(("0.0.0.0", 8887))
tcp_sock.listen(5)

udp_sock = socket(AF_INET, SOCK_DGRAM)
udp_sock.bind(("0.0.0.0", 8865))

f = open("log.txt", "rb")
# 开始监控io
print("监控IO发生")
rs, ws, xs = select([udp_sock, tcp_sock], [], [])
print("rs：", rs)
print("ws：", ws)
print("xs：", xs)

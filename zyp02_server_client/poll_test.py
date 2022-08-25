"""
poll io 多路复用
"""
from select import *
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
p = poll()
# 关注
p.register(tcp_sock, POLLIN)
p.register(f, POLLOUT)
p.register(udp_sock, POLLOUT)
print("tcp_sock", tcp_sock.fileno())
print("udp_sock", udp_sock.fileno())
print("file", f.fileno())
# 准备工作
map = {tcp_sock.fileno(): tcp_sock,
       udp_sock.fileno(): udp_sock,
       f.fileno(): f
       }

events = p.poll()  # 进行监控
print(events)
p.unregister(f)  # 取消关注

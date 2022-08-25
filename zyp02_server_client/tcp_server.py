"""
tcp 服务端实例
"""
from socket import *

# 创建tcp套接字
tcp_socket = socket(AF_INET, SOCK_STREAM)
# 绑定地址
tcp_socket.bind(("0.0.0.0", 8888))
# 设置监听
tcp_socket.listen(5)
# 等待客户端连接
while True:
    print("Waiting for connect...")
    conndf, addr = tcp_socket.accept()
    print("connect from,", addr)  # 打印客户端地址

    # 等待接收
    while True:
        data = conndf.recv(1024)
        # 另外一端不存在了,recv会返回空字节
        if not data:
            break
        print("Recv:", data.decode())
        conndf.send(b"Thanks#")
    conndf.close()  # 某个客户端退出对应的套接字就关闭
# 都要关闭

tcp_socket.close()

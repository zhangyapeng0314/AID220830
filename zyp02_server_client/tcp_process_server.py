"""
基于多进程的TCP网络并发模型
重点代码
"""
from multiprocessing import Process
from signal import *
from socket import *

# 全局变量
HOST = '0.0.0.0'
PORT = 8889
ADDR = (HOST, PORT)  # 服务器地址


# 处理客户端请求
def handle(connfd):
    # 等待接收
    while True:
        data = connfd.recv(1024)
        # 另外一端不存在了,recv会返回空字节
        if not data:
            break
        print("Recv:", data.decode())
        connfd.send(b"Thanks#")
    connfd.close()  # 某个客户端退出对应的套接字就关闭


def main():
    # tcp套接字创建
    sock = socket()
    sock.bind(ADDR)
    sock.listen(5)
    print("Listen the port %s" % PORT)
    signal(SIGILL, SIG_IGN)  # 处理僵尸进程
    # 循环连接
    while True:
        try:
            connfd, addr = sock.accept()
            print("Connfd from", addr)
        except KeyboardInterrupt:
            sock.close()
            return

            # 为连接进来的客户端创建单独的子进程
        p = Process(target=handle, args=(connfd,))
        p.daemon = True  # 父进程退出,子进程终止服务
        p.start()


if __name__ == '__main__':
    main()

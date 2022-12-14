"""
web 服务程序
假定：用户有一组网页，希望使用我们提供的类快速搭建一个服务，实现自己网页的展示浏览
IO 多路复用和 http训练
"""
import re
from select import select
from socket import *


class WebServer:
    def __init__(self, host="0.0.0.0", port=80, html=None):
        self.host = host
        self.port = port
        self.html = html
        # 做IO多路复用并发模型准备
        self.__rlist = []
        self.__wlist = []
        self.__xlist = []
        self.create_socket()
        self.bind()

    # 创建套接字
    def create_socket(self):
        self.sock = socket()
        self.sock.setblocking(False)

    def bind(self):
        self.address = (self.host, self.port)
        self.sock.bind(self.address)

    # 启动服务
    def start(self):
        self.sock.listen(5)
        print("Listen the port %d" % self.port)
        # IO多路复用并发模型
        self.__rlist.append(self.sock)
        while True:
            # 循环监听IO
            rs, ws, xs = select(self.__rlist, self.__wlist, self.__xlist)
            for r in rs:
                # 分类讨论
                if r is self.sock:
                    # 有浏览器连接
                    connfd, addr = self.sock.accept()
                    connfd.setblocking(False)# 非阻塞
                    self.__rlist.append(connfd)
                else:  # 有客户端发起请求
                    # data = r.recv(4096)
                    # print(data.decode())
                    try:
                        self.handle(r)
                    except:
                        self.__rlist.remove(r)
                        r.close()

    # 处理客户端请求
    def handle(self, connfd):
        # 浏览器发送了HTTP请求
        request = connfd.recv(1024 * 10).decode()
        # print(request)
        # 使用正则提取内容
        pattern = "[A-Z]+\s+(?P<info>/\S*)"
        result = re.match(pattern, request)  # match对象/None,match只匹配目标字符串开始的位置
        if result:
            info = result.group("info")  # 提取请求内容
            print("请求内容:", info)
            # 发送响应内容
            self.send_response(connfd, info)
        else:
            # 没有获取请求断开客户端
            self.__rlist.remove(connfd)
            connfd.close()

    # 根据请求组织响应内容，发送给浏览器
    def send_response(self, connfd, info):
        if info == "/":
            filename = self.html + "/index.html"
        else:
            filename = self.html + info
        try:
            fd = open(filename, "rb")  # 有可能有文本还有图片
        except:
            # 请求的文件不存在
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += "<h1>Sorry....</h1>"
            response = response.encode()# 转换成字节串
        else:
            # 请求的文件存在
            data = fd.read()
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "Content-Length:%d\r\n" % len(data)  # 发送图片
            response += "\r\n"
            response = response.encode() + fd.read()  # 转化成字节串拼接
        finally:
            # 给客户端发送响应
            connfd.send(response.encode())


if __name__ == '__main__':
    """
    思考问题：1.使用流程
            2.哪些需要用户决定，怎么传入
                哪组网页？
                服务器地址？
    """
    httpd = WebServer(host="0.0.0.0", port=8000, html="E:/Pycharm/project/zyp02_server_client/static")  # 实例化对象
    httpd.start()

"""
练习：index.html 这个网页内容显示在浏览器上
要求：浏览器可以多次访问
"""
from socket import *

# 创建tcp套接字
s = socket()
s.bind(("0.0.0.0", 8889))
s.listen(5)
while True:
    c, addr = s.accept()
    print("connect from", addr)  # 浏览器连接
    data = c.recv(4096)  # 接收的是http请求
    print(data.decode().split('\n')[0])  # 请求行

    # 响应格式
    f = open("E:/Pycharm/project/zyp02_server_client/index.html")
    html = "HTTP/1.1 200 Ok\r\n"
    html += "Content-Type:text/html\r\n"
    html += "\r\n"
    html += f.read()  # 响应体
    c.send(html.encode())  # 发送响应给客户端
    f.close()
    c.close()
s.close()

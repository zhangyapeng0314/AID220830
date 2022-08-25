"""
http 请求响应演示
"""
from socket import *

# 创建tcp套接字
s = socket()
s.bind(("0.0.0.0", 8889))
s.listen(5)

c, addr = s.accept()
print("connect from", addr)# 浏览器连接
data = c.recv(4096)# 接收的是http请求
print(data.decode())

# 响应格式
html = """HTTP/1.1 200 Ok
Content-Type:text/html

hello word
"""
c.send(html.encode())# 发送响应给客户端



c.close()
s.close()

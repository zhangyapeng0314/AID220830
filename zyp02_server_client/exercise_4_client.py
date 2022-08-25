"""
客户端上传头像
思路：建立网络连接，发送图片
1.创建套接字
2.连接服务端
3.读取图片内容
4.发送图片内容
5.发送完成关闭
"""
from socket import *

# 创建套接字
sock = socket()
# 发起连接,连接服务端
sock.connect(("127.0.0.1", 8898))
# 读取图片内容
f = open("zly.jpeg", "rb")
while True:# 边读边发
    data = f.read(1024)  # 字节串
    # 读到文件结尾
    if not data:
        break
    # 发送图片内容
    sock.send(data)
# 关闭
f.close()
sock.close()

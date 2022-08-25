"""
上传头像
思路：建立网络，收取图片
1.建立套接字
2.等待客户端连接
3.接受图片
4.存储图片，以日期命名
5.关闭
"""

import time
from socket import *

# 1.建立tcp套接字
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(("0.0.0.0", 8898))
sock.listen(5)
# 2.等待客户端连接
while True:  # 等待多个客户端连接
    connfd, addr = sock.accept()
    print("Connect from", addr)
    # 3.接受图片
    filename = "%d-%d-%d.jpg" % time.localtime()[:3]
    f = open(filename, "wb")
    while True:  # 边收边保存
        data = connfd.recv(1024 * 1024)
        if not data:
            break
        f.write(data)
    # 关闭
    f.close()
    connfd.close()
sock.close()

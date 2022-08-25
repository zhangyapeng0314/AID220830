"""
tcp 服务端实例 从客户端不断的发送问题，小美会将回答发送回答打印，如果你的问题他听不懂则回复“人家还小不太明白”
"""
from socket import *

chat = {"你好": "你好",
        "叫什么": "我叫小美",
        "几岁": "我2岁了",
        "男生女生": "我是机器人"}

# 创建tcp套接字
tcp_socket = socket(AF_INET, SOCK_STREAM)
# 绑定地址
tcp_socket.bind(("0.0.0.0", 8899))
# 设置监听
tcp_socket.listen(5)
# 等待客户端连接
print("处理客户端消息")
while True:
    connfd, addr = tcp_socket.accept()
    print("connect from,", addr)  # 打印客户端地址
    # 等待接收
    data = connfd.recv(1024)
#    print(data.decode())
    # 另外一端不存在了,recv会返回空字节
    if not data:
        break
    # 遍历字典
    for i in chat:
        # 找到对应的键返回对应的值
        "----"
        print(i)
        if i in data.decode():
            connfd.send(chat[i].encode())
            "--------"
            print(chat[i])
            break
        else:
            # 没有找到键
            connfd.send("人家还小不太明白")
    connfd.close()  # 某个客户端退出对应的套接字就关闭
# 都要关闭

tcp_socket.close()

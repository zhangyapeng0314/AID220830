"""
单词通过数据表words查询
思路：客户端输入一个单词，发送一次，然后等接收，打印；
    服务端，接受单词，查询单词，讲解释发送给客户端
"""

from socket import *

import pymysql

# 确定服务器的地址
ADDR = ("0.0.0.0", 11111)


# 连接数据库-》创建游标-》执行sql-》查询结果
class Database:
    def __init__(self):
        self.db = pymysql.connect(user="root",
                                  password="969390",
                                  database="dict",
                                  charset="utf8")
        self.cur = self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()

    # 查询单词
    def find_words(self, word):
        """
        :param word:要查询的单词
        :return:str 查询到的解释 or Not Found
        """
        sql = "select mean from words where word=%s;"
        self.cur.execute(sql, [word])
        result = self.cur.fetchone()  # (mean,)None
        if result:
            return result[0]  # 返回解释
        else:
            return "Not Found"


# 单词的接受和解释发送
def main():
    # 创建udp的套接字
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    # 绑定地址
    udp_socket.bind(ADDR)
    db = Database()  # 生成数据库对象
    while True:
        # 接受客户端消息
        word, addr = udp_socket.recvfrom(1024)
        # 与客户端约定一个特殊的退出指令,服务端程序一般不退出
        # if word == b'##':
        #     break
        # 查询单词
        result = db.find_words(word.decode())
        udp_socket.sendto(result.encode(), addr)  # 给对应的客户端返回消息
    # db.close()
    # udp_socket.close()


if __name__ == '__main__':
    main()  # 启动

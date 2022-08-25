"""
练习题
"""

# import time
# 
# f = open('my.log', 'a+', encoding='UTF-8', buffering=1)
# n = 1
# f.seek(0, 0)
# for i in f:
#     n += 1
# 
# while True:
#     time.sleep(2)  # 时间间隔2秒
#     msg = '%d. %s\n' % (n, time.ctime())
#     f.write(msg)
#     n += 1
# 
# f.colse()
import re


def get_info():
    f = open("inet.log", encoding="UTF_8")

    while True:
        info = ""
        for line in f:
            if line == "\n":
                break
            info += line
        if not info:
            break
        yield info
    f.close()
    return


def get_address(port):
    for data in get_info():

        obj = re.match(r"\S+", data)
        if port == obj.group():
            pattern = r"[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}"
            result = re.search(pattern, data)
            if result:
                return result.group()
            else:
                return "Unknown"
    return "port error"


print(get_address(input("请输入你要输入的端口号：")))

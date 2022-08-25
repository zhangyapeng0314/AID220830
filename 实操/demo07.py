"""
登录及日志
"""
import time


def show_info():
    print('输入提示数字，执行相应的操作：0.退出 1.查看登录日志')


# 记录日志
def write_logininfo(username):
    with open('log.txt', 'a') as file:
        s = f'用户名{username},登陆时间:{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))}'
        file.write(s)
        file.write('\n')


# 读取日志
def read_logininfo():
    with open('log.txt', 'r') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            else:
                print(line,end='')


if __name__ == '__main__':
    username = input('请输入用户名:')
    paw = input('请输入密码:')
    if username == 'admin' and paw == 'admin':
        print('登陆成功')
        write_logininfo(username)  # 记录日志
        show_info()  # 提示用户进行什么操作
        num = int(input('请输入操作数字：'))
        while True:
            if num == 0:
                print('退出成功')
                break
            elif num == 1:
                print('查看登录日志')
                read_logininfo()  # 读取日志
                num = int(input('请输入操作数字：'))
            else:
                print('您输入的数字有误！！！')
                show_info()
                num = int(input('请输入操作数字：'))
    else:
        print('对不起，用户名或密码不正确')

    """
    print(time.time())#秒
    print(time.localtime(time.time()))#转换年月日，时分秒
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))#转换成自己的格式
    """

"""
火车信息
"""


def get_count(s,ch):
    count = 0
    for item in s:
        if ch.upper() == item or ch.lower() == item:
            count += 1
    return count


if __name__ == '__main__':
    s = 'hellopython,Hello_java,Hello_go'
    ch = input('请输入你要搜索的字符:')
    count = get_count(s, ch)
    print(f'{ch}在{s}中出现的次数为{count}')

"""
淘宝客服回复
"""


def find_answer(question):
    with open('reply.txt', 'r', encoding='UTF-8') as file:
        while True:
            line = file.readline()
            if not line:  # 到文件末尾退出
                break
            # 字符串分割
            keyword = line.split('|')[0]
            reply = line.split('|')[1]
            if keyword in question:
                return reply
    return False


if __name__ == '__main__':
    question = input("hi,您好，请输入您的问题")
    while True:
        if question == 'bye':
            break
        reply = find_answer(question)
        if not reply:
            question = input('您输入的问题不存在')
            break

        else:
            print(reply)
            question = input('还有什么其他问题？退出请输入bye')
    print('再见')

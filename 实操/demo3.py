"""
判断随机数
"""
import random


def guess(num, guess_num):
    if num == guess_num:
        return 0
    elif guess_num > num:
        return 1
    else:
        return -1


num = random.randint(1, 100)
for i in range(10):
    guess_num = int(input('我心里有个[1-100]的整数请你猜一猜:'))
    result = guess(num, guess_num)
    if result == 0:
        print('猜对了')
        break
    elif result == 1:
        print('大了')
    else:
        print('小了')
else:
    print('真笨，10次都没猜中')

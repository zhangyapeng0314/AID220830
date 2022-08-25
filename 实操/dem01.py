"""
操作练习
"""
'一.使用print方式进行输出（输出的目的地是文件）'
fp = open('E:/Pycharm/project/实操/test.txt', 'w')
print('奋斗成就更好的你', file=fp)
fp.close()
"""
以文件方式打开
"""
# 打开文件，写方式打开
# f = open("file.txt", "r",encoding='UTF-8')
# while True:
#     data = f.read(1024*10)
#     if not data:
#         break
#     print(data,end="")
# f.close()
# word = input('请输入你要查询的单词:')
# f = open("dict.txt", "r", encoding='UTF-8')
#
# for line in f:
#     word_list = line.split(' ')
#  #   print(word_list)
#     if word_list[0] > word:
#         print('没有该单词')
#         break
#     elif word == word_list[0]:
#         print(word_list[-1].split())
#         break
# else:
#     print("没有找到该单词")
# f.close()

for item in range(1, 100):
    ge = item % 10
    shi = item // 10 % 10
    bai = item // 100
    print(bai, shi, ge)

for item in range(100, 1000):
    ge = item % 10
    shi = item // 10 % 10
    bai = item // 100
    # print(ge, shi, bai)
    if ge**3+shi**3+bai**3==item:
        print(item)
for item in range(1, 51):
    if item % 5 != 0:
        continue
    print(item)

for item in range(3):
    pwd = input('请输入密码:')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
else:
    print('对不齐，三次密码均输入错误')

for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t')
    print()
lst = [10, 20, 30, 40, 50, 60]
print(id(lst))
list02 = ['hell', 'word']
lst[1:] = list02
print(lst, id(lst))


# number=ob10
# number02=ob10
# number02=ob10
# number03=ob10
# number01=15e-1

print(0.000000001)
date = '10'
data = 10
usd = input("请输入美元：")
usd = input("请输入美元：")
usd = input("请输入美元：")
usd = input("请输入美元：")
usd = input("请输入美元：")
usd = input("请输入美元：")
usd = input("请输入美元：")
""""
结果=数据类型（待转换数据）
"""
str_age = "18"
int_age = int

number01 = int("18")
float01 = float(18)
floato2 = float("1.5")
number01 = 10
number01 + 5
print(number01)
number01 = 10
number01 += 5
print(number01)
unit_price = float(input("请输入单价："))
amount = int(input("请输入数量："))
money = float(input("请输入金额："))
result = money - unit_price * amount
print("应该找回" + str(result))
number_of_people = float(input("请输入确诊人数："))
number_of_peopleo1 = float(input("请输入治愈人数;"))
Cure_ratio = number_of_peopleo1 / number_of_people * 100
print("治愈比例：" + str(Cure_ratio) + "%")
some = float(input("请输入两："))
jin = some // 16
some01 = some % 16
print(str(jin) + "斤" + str(some01) + "两")
data01 = 100
data02 = 200
data03 = data01 + data02
data01 = 200
print(data03)  # ?
father = float(input("获取父亲的身高："))
mother = int(input("获取母亲的身高："))
print("显示儿子的身高：" + str((father + mother) * 0.54))
print(int(input("请输入整数")) > 0)
print(1 <= int(input("请输入月份")) <= 12)
number = int(input("请输入数字:"))
if number > 0:
    print("正数")
elif number < 0:
    print("负数")
else:  # 是把健康
    print("零")
sex = input("请输入性别:")
if sex == "男":
    print("您好先生")
elif sex == "女":
    print("您好女士")
else:
    print("性别未知")
state = int(input("请输入整数:"))
if number % 2 != 0:
    print(str(state) + "奇数")
else:
    print(str(state) + "偶数")
state = "偶数" if int(input("请输入一个整数:")) % 2 == 0 else "奇数"
speed = float(input("虫子吃苹果的速度(小时/个):"))
print(state)
total_count = int(input("请输入苹果的数量:"))
duration = float(input("请输入经过多少小时:"))
remain_count = int(total_count - duration / speed)
if remain_count > 0:
    print("没有被虫子吃的苹果树:" + str(remain_count))
else:
    print("没有苹果啦")
while True:
    state = "奇数" if int(input("请输入一个整数:")) % 2 != 0 else "偶数"
    print(state)
    if input("请输入y继续") != "y":
        break
count = 0
while count < 5:
    print("写一次")
    count += 1

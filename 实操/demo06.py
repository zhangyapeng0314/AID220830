"""
推算日期
"""
import datetime  # 导入时间模块


def inputdate():  # 输入日期函数
    indate = input('请输入开始日期：（20220419）后按回车：')
    indate = indate.strip()  # 去掉空格
    datestr = indate[0:4] + '-' + indate[4:6] + '-' + indate[6:]  # 分割字符串，切片
    return datetime.datetime.strptime(datestr, '%Y-%m-%d')  # 返回字符串转换成时间


if __name__ == '__main__':
    print('---------------推算几天后的日期---------------------')
    sdate = inputdate()  # 调用当前的时间函数
    in_num = int(input('请输入你的间隔天数'))
    fdate = sdate + datetime.timedelta(days=in_num)  # 过程
    print('您推算的日期是：' + str(fdate))

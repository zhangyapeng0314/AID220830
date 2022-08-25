"""
学生信息管理系统
"""
import os.path

filename = 'student.txt'


def main():
    while True:
        menm()
        choice = int(input('请选择:'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('您确定要退出系统吗？y/n:')
                if answer == 'y' or answer == 'Y':
                    print('谢谢您的使用！！！')
                    break
                else:
                    continue
            elif choice == 1:
                insert()  # 录入学生信息
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()


def menm():
    print('=====================学生信息管理系统===========')
    print('----------------------功能菜单-----------------')
    print('\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t\t0.退出系统')
    print('----------------------------------------------')


def insert():
    student_list = []
    while True:
        id = input('请输入ID(如1001)')
        if not id:
            break
        name = input('请输入姓名：')
        if not name:
            break
        try:
            english = int(input('请输入英语成绩:'))
            python = int(input('请输入Python成绩:'))
            java = int(input('请输入Java成绩:'))
        except:
            print('输入无效,不是整数类型,请重新输入:')
            continue
        # 将录入的学生保存在字典中
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        # 将学生信息添加到列表当中
        student_list.append(student)
        answer = input('是否继续添加？y/n\n')
        if answer == 'y':
            continue
        else:
            break

    # 调用save()函数
    save(student_list)
    print('学生信息录入完毕！')


def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def search():
    student_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):  # 如果文件存在
            mode = input('按ID查找请输入1，按姓名查找请输入2：')
            if mode == '1':
                id = input('请输入学生ID：')
            elif mode == '2':
                name = input('请输入学生姓名：')
            else:
                print('您的输入有误，请重新输入')
                search()
            with open(filename, 'r', encoding='utf-8') as rfile:  # 表示有内容以读写的方式打开文件,没有文件创造文件
                student = rfile.readlines()  # 读取所有的学生信息放在列表中
                for item in student:  # 遍历读出来的学生信息
                    d = dict(eval(item))  # 读出来的是字符串,将字符串转换成字典
                    if id != '':
                        if d['id'] == id:
                            student_query.append(d)  # 将查询到的学生添加到student_query列表中
                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)  # 将查询到的学生添加到student_query列表中
            # 显示查询结果
            show_student(student_query)
            # 清空列表
            student_query.clear()
            answer = input('是否继续查询？y/n\n')
            if answer == 'y':
                continue
            else:
                break
        else:  # 如果文件不存在
            print('暂未保存学员信息')
            return


def show_student(lst):
    if len(lst) == 0:  # 列表的长度为0
        print('没有查到学生信息，无数据显示！！')
        return
    # 定义标题显示格式
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}\t'
    print(format_title.format('ID', '姓名', '英语成绩', 'python成绩', 'java成绩', '总成绩'))
    # 定义内容的显示格式
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item.get('english')) + int(item.get('python')) + int(item.get('java'))
                                 ))


def delete():
    while True:
        student_id = input('请输入要删除的学生的ID:')
        if student_id != '':
            if os.path.exists(filename):  # 判断文件是否存在
                with open(filename, 'r', encoding='utf-8') as file:  # 存在的情况下打开文件
                    student_old = file.readlines()  # 读取所有的学生信息放在列表中
            else:  # 文件不存在的情况下
                student_old = []  # 定义一个列表
            flag = False  # 标记是否删除
            if student_old:  # 判断列表，空列表的Boolean为false，如果列表的内容为ture,表示有内容以读写的方式打开文件
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}  # 空字典将删除后的字典写入磁盘文件中
                    for item in student_old:  # 遍历列表
                        d = dict(eval(item))  # 读出来的是字符串,将字符串转换成字典
                        if d['id'] != student_id:  # 判断列表中的ID与学生列表中的ID不相等
                            wfile.write(str(d) + '\n')  # 讲一条学生信息写入文件
                        else:
                            flag = True  # 标记已删除
                    if flag:
                        print(f'id为{student_id}的学生信息已经删除')
                    else:
                        print(f'没有找到id为{student_id}的学生信息')
            else:
                print('无学生信息')
                break
            show()  # 删除之后重现显示所有的学生信息
            answer = input('是否继续删除？y/n\n')
            if answer == 'y':
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(filename):  # 判断文件是否存在
        with open(filename, 'r', encoding='utf-8') as file:  # 存在的情况下打开文件
            student_old = file.readlines()  # 读取所有的学生信息放在列表中
    else:
        return
    student_id = input('请输入要修改的学员的ID:')
    with open(filename, 'w', encoding='utf-8') as wfile:  # 表示有内容以读写的方式打开文件
        for item in student_old:  # 遍历读出来的学生信息
            d = dict(eval(item))  # 读出来的是字符串,将字符串转换成字典
            if d['id'] == student_id:  # 输入的学生ID等于字典里的ID，键相等
                print('找到学生信息,可以修改他的相关信息了！')
                while True:
                    try:
                        d['name'] = input('请输入姓名：')  # 根据键获取值
                        d['english'] = input('请输入英语成绩：')
                        d['python'] = input('请输Python成绩：')
                        d['java'] = input('请输入Java成绩：')
                    except:  # 抛异常
                        print('您输入的有误，请重新输入')
                    else:  # 阻止不断循环
                        break
                wfile.write(str(d) + '\n')  # 修改的没有问题，需要写入，字典转成str类型
                print('修改成功！！！')
            else:
                wfile.write(str(d) + '\n')  # 如果ID不相等，就写入文件
        answer = input('是否继续修改其他学生信息？y/n\n')
        if answer == 'y':
            modify()


def sort():
    show()
    if os.path.exists(filename):  # 判断文件是否存在
        with open(filename, 'r', encoding='utf-8') as rfile:  # 表示有内容以读写的方式打开文件
            students_list = rfile.readlines()  # 读取所有的学生信息放在列表中
        student_new = []  #
        for item in students_list:  # 遍历读出来的学生列表
            d = dict(eval(item))  # 读出来的是字符串,将字符串转换成字典
            student_new.append(d)  # 将字典添加到学生列表中
    else:  # 如果文件不存在
        return

    asc_or_desc = input('请选择(0.升序 1.降序):')
    if asc_or_desc == '0':
        asc_or_desc_bool = False
    elif asc_or_desc == '1':
        asc_or_desc_bool = True
    else:
        print('您的输入有误，请重新输入')
        sort()
    mode = input('请选择排序方式(1.按英语成绩排序 2.按Python成绩排序 3.按java成绩排序 0.按总成绩排序): ')
    if mode == '1':
        student_new.sort(key=lambda x: int(x['english']), reverse=asc_or_desc_bool)
    elif mode == '2':
        student_new.sort(key=lambda x: int(x['python']), reverse=asc_or_desc_bool)
    elif mode == '3':
        student_new.sort(key=lambda x: int(x['java']), reverse=asc_or_desc_bool)
    elif mode == '0':
        student_new.sort(key=lambda x: int(x['english']) + int(x['python']) + int(x['java']), reverse=asc_or_desc_bool)
    else:
        print('您的输入有误，请重新输入')
        sort()
    show_student(student_new)


def total():
    if os.path.exists(filename):  # 判断文件是否存在
        with open(filename, 'r', encoding='utf-8') as rfile:  # 存在的情况下打开文件
            student = rfile.readlines()
            if student:  # 如果学生列表不为空
                print(f'一共有{len(student)}名学生')
            else:
                print('还没有录入学生信息')
    else:
        print('暂未保存数据！')


def show():
    student_lst = []  # 存储学生信息
    if os.path.exists(filename):  # 判断文件是否存在
        with open(filename, 'r', encoding='utf-8') as rfile:  # 存在的情况下打开文件
            students = rfile.readlines()  # 读取所有的学生信息放在列表中
            for item in students:  # 遍历列表
                student_lst.append(eval(item))  # 读出来的是字符串,将字符串转换成字典,然后添加到student_lst列表中
            if student_lst:  # 如果列表不为空，列表对象的Boolean（布尔值）为ture
                show_student(student_lst)  # 调用show函数展示学生信息
    else:
        print('暂未保存过数据！')


if __name__ == '__main__':
    main()

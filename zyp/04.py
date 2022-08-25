"""
练习
"""


lst = [20, 40, 10, 98, 54]
print('排序前的列表', lst, id(lst))
# “ 开始排序，调用列表的surt方法，升序排列”
lst.sort()
print('排序后的列表', lst, id(lst))

lst = [i for i in range(1, 10)]
print(lst)
lst01 = [i*2 for i in range(1, 10)]
print(lst01)

score = {'张三': '10', '李四': '30'}
for item in score:
    print(item, score[item], score.get(item))
    print()


class Student:
    native_pace = '山西'  # 直接写在类里面的变量，称为类属性

    def __init__(self, name, age):
        self.name = name  # 实例属性，进行了一个赋值的操作，将局部变量的name的值赋值给实例属性
        self.age = age

    # 实例方法
    def eat(self):
        print('学生在吃饭')
    # 静态方法


    @staticmethod
    def method():
        print('我使用了staticmethod方法，所以我是静态方法')


    # 类方法
    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用classmethod方法进行修饰')


# 在类之外定义的成为函数，在类之内定义的成为方法
def drink():
    print('喝水')


#创建Student类的对象
stu1 = Student('张三', 30)
print(id(stu1))
print(type(stu1))
print(stu1)
print('-----------------------------')
print(id(Student))
print(type(Student))
print(Student)
stu1.eat()
print(stu1.name)
print(stu1.age)
print('-----------------------------')
Student.eat(stu1)#65行与61行代码功能相同,都是调用Student中的eat方法
                #类名.方法名（类的对象）---->实际上就是方法定义处的self
'''
继承
'''


class Person(object):
    def __init__(self, name='', age=''):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)
        self.stu_no = stu_no

    def info(self):
        super().info()
        print(self.stu_no)


class Teacher(Person):
    def __init__(self, name, age, teachofyear):
        super().__init__(name, age)
        self.teachofyear = teachofyear

    def info(self):
        super().info()
        print(self.teachofyear)


stu = Student('张三', 20, 1001)
teacher = Teacher('李四', 30, 10)

stu.info()
teacher.info()

class Student:
    pass


stu = Student()
print(dir(stu))
print(stu)


class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self, name, age):
        self.name = name
        self.age = age
class D(A):
    pass
# 创建C类的对象
X=C('张亚鹏',26)
print(X.__dict__) #实例对象的属性字典
print(C.__dict__)
print(X.__class__)#输出对象所属的类
print(C.__bases__)#c类的父类型的元素
print(C.__base__)#类的基类
print(C.__mro__)#类的层次结构
print(A.__subclasses__())#子类的列表
"""
特殊方法
"""


class Student:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.name + other.name


stu1 = Student('张亚鹏')
stu2 = Student('汪云飘')
S = stu1 + stu2
print(S)
"""
类的赋值和浅拷贝
"""

#列出指定目录下的所有的py文件
import os #导入系统模块
path = os.getcwd()#获取当前目录
lst02 = os.listdir(path)#获取路径下的所有文件，放在一个列表中
for filename in lst02:#遍历列表
    if filename.endswith(".py"):
        print(filename)
#mport os #导入系统模块
# path = os.getcwd()#获取当前目录
lst03 = os.walk(path)#获取路径下的所有文件子文件，放在一个列表中
print(lst03)#迭代器对象
print("------------------------------------")
for dirpath,dirname,filename in lst03:#遍历迭代器对象，返回的是一个元组，元组当中包含目录下的所有文件夹和所有文件（类型是元组返回多个类型）
 #遍历当前目录下的文件，还可以把当前目录下的子文件遍历下来
    # print(dirpath)
    # print(dirname)
    # print(filename)
    # print("XXXXXXXXXXXXXXXXXX")
    for dir in dirname:
        print(os.path.join(dirpath,dir))#在当前目录下有多少个子目录

    for file in filename:#文件名
        print(os.path.join(dirpath,file))#连接路径和文件名







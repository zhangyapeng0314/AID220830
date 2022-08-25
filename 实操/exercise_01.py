"""
练习
create table words (id int primary key auto_increment,word char(30),mean varchar(256));
"""
import re
import pymysql

#打开单词本
f=open("dict.txt")

#装单词[(word,mean),(),()]-> executeany
args_list = []
for line in f:
    #result -->[(word,mean)]
    result=re.findall(r"(\w+)\s+(.*)",line)
    #print(result)
    args_list.append(result[0])
f.close()

# 连接数据库
db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="969390",
                     database="dict",
                     charset="utf8"
                     )
# 创建游标
cur = db.cursor()

# 对数据库操作（增删改查）




try:
    sql = "insert into words (word,mean) values (%s,%s);"
    # for i in l:
    #     cur.execute(sql.i)
    cur.executemany(sql,args_list)
    db.commit()
except Exception as e:
    print(e)
    # 注意：数据库的引擎
    db.rollback()  # 没有提交到数据库的内容，全部失效

# 获取一条记录
# row = cur.fetchone()
# print(row)


# 关闭游标和数据库
cur.close()
db.close()


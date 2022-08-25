"""
mysql
"""
import pymysql

# 连接数据库
db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="969390",
                     database="stu",
                     charset="utf8"
                     )
# 创建游标
cur = db.cursor()

# 对数据库操作（增删改查）

# 插入多条数据
l = [
    # (1, '老舍', '男', '骆驼祥子'),
    (2, '鲁迅', '男', '阿Q正传'),
    (3, '王八蛋', '女', '傻逼'),
    (4, '李白', '男', '将进酒')
]
# 查询数据库
# sql="select * from 作家;"
# cur.execute(sql)
# 插入表中的内容:
try:
    sql = "insert into 作家 (id,name,sex,remark) values (%s,%s,%s,%s);"
    # for i in l:
    #     cur.execute(sql.i)
    cur.executemany(sql,l)
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

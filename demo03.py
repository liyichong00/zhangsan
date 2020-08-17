import time #时间
import random #生成随机数
import pymysql #数据库

# for i in range(10):
#     time.sleep(1) #停顿1秒
#     print(i)

# a = random.randint(100,1000)

db = pymysql.connect(host="127.0.0.1",user="root",password="123456",db="testdb")
cur = db.cursor()
try:
    cur.execute("select * from t_class;")
    res = cur.fetchall()
    print(res)
except:
    print("sql语句错误")

"""
练习:
定义一个方法,用来判断用户输入的账号密码是否符合规范
"""
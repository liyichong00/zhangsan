import time #时间
import random #生成随机数
import pymysql #数据库

# for i in range(10):
#     time.sleep(1) #停顿1秒
#     print(i)

# a = random.randint(100,1000)

# db = pymysql.connect(host="127.0.0.1",user="root",password="123456",db="testdb")
# cur = db.cursor()
# try:
#     cur.execute("select * from t_class;")
#     res = cur.fetchall()
#     print(res)
# except:
#     print("sql语句错误")

"""
练习:
定义一个方法,用来判断用户输入的账号密码是否符合规范
"""
# def checkname(username,password): #def方法声明,checkname方法名称,username方法参数
#     """
#     自动判断账号长度是否为5-7位,并且必须小写字母开头
#     """
#     if len(username)>=5 and len(username)<=8:
#         if username[0] in "qwertyuiopasdfghjklzxcvbnm":
#             if len(password) >= 8 and len(password) <= 12:
#                 return True
#                 userlist = {"username":username,"passwrod":password}
#             else:
#                 return "密码必须8-12位"
#         else:
#             return "账号首字母必须为小写字母"    
#     else:
#         return "账号长度不符合规范,请输入5-8位的账号"

#类
"""
class 声明类的名字
然后类的名字首字母必须大写
面向对象编程
类里面所有的方法,都必须要传一个参数:self
"""

class GirlFriend():
    """
    女朋友
    """
    def __init__(self,sex,high,weight,hair,age): #初始化
        self.sex = sex
        self.high = high
        self.weight = weight
        self.hair = hair
        self.age = age

    def talent(self,num):
        """
        才艺
        """
        print("性别"+self.sex+"身高"+self.high+"体重"+self.weight+"发型"+self.hair+"年龄"+self.age)
        if num == 1:
            print("胸口碎大石")
        elif num ==2:
            print("唱跳RAP篮球")
        else:
            print("单手开瓶盖")

    def cooking(self):
        """
        厨艺
        """
        print("精通八大菜系")
    
    def work(self):
        """
        工作
        """
        print("开挖掘机")

#类的实例化
# zhangsan = GirlFriend()
# zhangsan.talent(1)
# zhangsan.work()
# print(zhangsan.high)

# class Car():
#     def __init__(self,brand,color,decorate,type):
#         self.brand = brand
#         self.color = color
#         self.decorate = decorate
#         self.type = type
#     def transform(self):
#         print("汽车变形金刚")
#     def fly(self):
#         print("车子开始起飞")

# zhangsan = Car("五菱宏光","灰色","豪华","面包车")
# zhangsan.transform()

class Nvpengyou(GirlFriend):
    def work(self):
        print("修电脑")

zhangsan = Nvpengyou("女","170","100","短发","24")
zhangsan.work()

#GirlFriend:父类
#Nvpengyou:子类
#Object:祖类
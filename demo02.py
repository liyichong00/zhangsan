#判断
# a = 1
# b = 2
# if a>b:
#     print("a比b大") #四格缩进代表代码块
# else:
#     print("b比a大")

# age = int(input("请输入你的年龄:"))
# if age>60:
#     print("你应该退休了")
# elif age>30:
#     print("家庭的责任很重吧")
# elif age>20:
#     print("一定要好好规划你的未来")
# else:
#     print("读书的时候要认真")

# a = "你好"
# if a in "你好,今天你吃了吗?":
#     print("ok")
# else:
#     print("no")

# a = input("请输入:")
# print(type(a))
# if a=="":
#     print("不能为空")
# if a in "0123456789":#此行代码有bug
#     a = int(a)
# else:
#     print("请输入正确的年龄")
#     exit()
# if a>5:
#     print("大")
# else:
#     print("小")

# a = 10
# if type(a) is int:
#     print("是数字")
# elif type(a) is str:
#     print("是字符串")
# else:
#     print("其他")

#循环
# a = 1
# while a<10:
#     print("哈哈")
#     a = a+1

"""
练习:现在有10个学生的成绩需要录入到系统中
这10个人为:张三,李四,王五,赵六,周七,刘八,钱九,孙十
并且名字和成绩需要对应上,而且大于60的与小于60的需要分开存放
"""
# num = 0 #初始化
# studentlist = []
# yespass = {} #定义一个空字典,用来存储及格的信息
# nopass = {} #定义一个空字典,用来存储不及格的信息
# while num<3:
#     name = input("请输入姓名:")
#     studentlist.append(name)
#     grde = int(input("请输入成绩:"))
#     #studentlist = {"name":name,"grde":grde}
#     #studentlist.update(name=name,grde=grde)
#     if grde>=60:
#         yespass[studentlist[num]] = grde
#     else:
#         nopass[studentlist[num]] = grde
#     #print(studentlist)
#     num = num + 1 #控制循环次数
# print("及格的:",yespass)
# print("不及格的:",nopass)

#遍历
# a = [1,2,3,4,5,6,7,8,9]
# for i in a:
#     print(i)

# for i in range(0,100,2):#range()生成数列
#     print(i)

"""
练习:
打印九九乘法表
"""
#嵌套循环
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,"X",i,"=",i*j,end="  ") #end控制不换行
#     print()

"""
练习:
1.通过print打印，模拟一个红绿灯的功能,注意:红灯30次,绿灯35次,黄灯3次
2.使用代码实现一个注册的功能,用户输入账号和密码,要求账号长度是5-8位,密码6-12位,并且账号必须小写字母开头,
  储存到字典中,{username:passwrod}
"""

#第一题 
# while Ture: #死循环
#     for i in range(0,30):
#         print("红灯还有",int(30-i),"秒结束")
#     for j in range(0,35):
#         print("绿灯还有",int(35-j),"秒结束")
#     for k in range(0,3):
#         print("黄灯还有",int(3-k),"秒结束")

# light = {"红灯":30,"绿灯":35,"黄灯":3}
# while True:
#     for i in light:
#         for j in range(light[i]):
#             print(i,"倒计时还有",light[i]-j,"秒")

#第二题
# username = input("账号:")
# if username == "":
#     print("账号不能为空")
# elif username not in "abcdefghijklmnopqrstuvwxyz": #有bug
#     print("账号开头必须为小写字母,请重新输入!")
# elif len(username)<5:
#     print("账号过短")
# elif len(username)>8:
#     print("账号过长")
# else:
#     password = input("密码:")
#     if password =="":
#         print("密码不能为空")
#     elif len(password)<6:
#         print("密码过短")
#     elif len(password)>12:
#         print("密码过长")
#     else:
#         print("注册成功")
#         userlist = {"username":username,"passwrod":password}
# print(userlist)

# username = input("请输入账号:")
# password = input("请输入密码:")
# if len(username)>=5 and len(username)<=8:
#     if username[0] in "qwertyuiopasdfghjklzxcvbnm":
#         if len(password) >= 8 and len(password) <= 12:
#             print("注册成功")
#             userlist = {"username":username,"passwrod":password}
#         else:
#             print("密码必须8-12位")
#     else:
#         print("账号首字母必须为小写字母")    
# else:
#     print("账号长度不符合规范,请输入5-8位的账号")

# for i in range(10):
#     if i == 4:
#         continue #略过当前循环
#         #break #跳出循环
#     print(i)

#函数/方法

# def checkname(username): #def方法声明,checkname方法名称,username方法参数
#     """
#     自动判断账号长度是否为5-7位,并且必须小写字母开头
#     """
#     if len(username)>=5 and len(username)<=8:
#         if username[0] in "qwertyuiopasdfghjklzxcvbnm":
#             return True
#         else:
#             return "账号首字母必须为小写字母"    
#     else:
#         return "账号长度不符合规范,请输入5-8位的账号"

# username = input("请输入账号:")
# password = input("请输入密码:")
# if checkname(username) ==True:
#     if len(password) >= 8 and len(password) <= 12:
#         print("注册成功")
#         userlist = {"username":username,"passwrod":password}
#     else:
#         print("密码必须8-12位")
# else:
#     print(checkname(username))


# def addition(a,b):
#     """
#     实现两个数字相加
#     """
#     if type(a) is int and type(b) is int:
#         return a+b
#     else:
#         return "输入的数据类型不正确"

# a = []
# print(a.append("哈哈")) #none
# print(a.count("哈哈")) #1
# print(addition(1,1)) #2,none

"""
返回值返回后我们可以对这个值做其他的操作
而print不能
"""
# a = [1,2,1,1,3]
# x = a.index[2]
# print(a[x])

#异常捕获

# try:
#     print("a"+1)
# except:
#     print("上面的代码写错了")

#代码单位:包->模块->类->方法->变量

#异常类
try:
    print("a"+1)
except Exception as e:
    print("上面的代码写错了",e)

a = input("请输入你的名字:")
b = input("请输入你的年龄:")
try：
    if int(b)>18:
        print(a,"成年了")
    else:
        print(a,"未成年")
except:
    print("请输入正确的年龄")
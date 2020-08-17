#print()打印
"""
print ("hello world!")#字符串
print(233)#整数
print(2.33)#小数
print(True)#布尔值 Ture False
print(())#元组
print([])#数组
print({})#字典

# 锄禾日当午
# 汗滴禾下土

print("哈哈",233,2.33)
print("哈哈"+"嘻嘻")#字符串的拼接
print("哈哈"*100)
print(((1+2)*100-9.9)/2)
print(2>3)

name = "张三"#把张三这个值赋值给了名字叫name的这个变量
print(name)
"""

#input()输入

#a = input("请输入: ")
#print("input获取的内容: ",a)

#数据格式转换

# print(type("哈哈"))
# print(type(233))
# print(type(2.33))
# print(type(True))
# print(type(()))
# print(type([]))
# print(type({}))

# a = float(input("请输入:"))
# b = float(input("请输入:"))
# print("input获取的内容:",a+b)

#练习:通过代码获取两段内容,并且计算他们的长度的和。

# a = input("请输入:")
# b = input("请输入:")

# print("长度和为:",len(a)+len(b))

#元组,下标,从0开始编号

# a = (1,2,3,4,"哈哈","哈哈","嘻嘻",True,False)
# print(a[4])
# print(a[-2])

# print(a.index("嘻嘻"))
# print(a.count("哈哈"))

#切片
# print(a[:4]) #左闭右开
# print(a[4:6])
# print(a[6:])

#二维元组

# b = (a,"哈哈","嘻嘻")
# print(b[0][3])

#数组

# a = [1,2,3,4,"哈哈","哈哈","嘻嘻",True,False]
# print(a[4])

#区别:元组在写好后不可修改,而数组可以修改

# a.append("呵呵") #增加
# a.append("嘿嘿")
# print(a)
# a.index()
# a.count()
# a.insert(7,"嗯嗯") #插入
# print(a)
# b = a.pop(0) #剪切
# c = a.pop(0)
# print(a)
# print(b+c)

#a.clear() #清空
# xx = ["你好","不好"]
# a.extend(xx) #合并数组,也可以直接使用a+xx 
# print(a)

#下标不要超出范围,即"越界"

"""
python语法
所有的方法都是小括号结尾,如print(),input(),len()
元组,数组,字典的取值,都是中括号,如a[0]
元组,数组,字典的定义,分别为(),[],{}
"""

"""
字典的特点
1.字典中的值没有顺序
2.字典的结构必须是键值对 即key:value
3.字典的取值是通过key去取value
"""
# a = {"name":"张三","age":25,0:"哈哈"}
#取值
# print(a["name"])
#新增
# a["high"] = "183cm"
# print(a)
#修改
# a["name"] = "李四"
# print(a)

# b = a.get("name")
# print(b)
# b = a.pop("name")
# print(b)
# print(a)
# a.update(name=111) #name不用"
# print(a)

#数组和字典的删除
# del a["name"]
# print(a)
# del a[0]

"""
练习:获取用户输入的个人信息,并且储存到字典中
个人信息包括了:name,age,sex
"""
name = input("请输入姓名:")
age = input("请输入年龄:")
sex = input("请输入性别:")
userinfo = {"name":name,"age":age,"sex":sex}
#userinfo.update(name=name,age=age,sex=sex)
print(userinfo)
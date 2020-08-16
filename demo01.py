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

a = input("请输入:")
b = input("请输入:")

print("长度和为:",len(a)+len(b))
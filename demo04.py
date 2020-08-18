import time

#写日记
now = time.strftime("%y-%m-%d %H:%M:%S")
text = input("请输入今天的心情:")
with open("C:\workhome\github\zhangsan\日记.txt","a",encoding="utf8") as f:
    f.write(now+"\n")
    f.write(text+"\n")
    f.write("-------------------------------\n")
#\t:制表符
#\n:换行

with open("C:\workhome\github\zhangsan\日记.txt","r",encoding="utf8") as f:
    text = f.readlines()
#    print(text)
for i in text:
    print(i)
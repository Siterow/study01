""" 
练习：
获取用户输入的个人信息并放入一个字典中
个人信息应该包括 name,age,sex
 """
 #我写的
a = {}
a["name"] = input("请输入姓名:")
a["age"] = input("请输入年龄:")
a["sex"] = input("请输入性别:")
print("用户的信息为")
print(a)

# 老师写的
name = input("请输入姓名:")
age = input("请输入年龄:")
sex =input("请输入性别:")
userinfo = {}
userinfo.update(name=name, sex=sex, age=age)
print(userinfo)

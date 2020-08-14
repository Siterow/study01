
""" 
练习1：
通过print打印实现一个模拟红绿灯的功能，红灯30次，绿灯35次，黄灯3次
（输出红灯30次→输出绿灯35次→输出黄灯3次依次循环）
练习2：
实现一个注册功能，用户输入账号和密码，账号长度5-8位，密码6-12位，并且账号必须小写字母开头
储存到字典中 {username:password}
 """
""" 
# 练习一
for i in range(1, 30):
    print("距离红灯结束还有", 30 - i, "秒")

for i in range(1, 35):
    print("距离绿灯结束还有", 35 - i, "秒")

for i in range(1, 3):
    print("距离黄灯结束还有", 3 - i, "秒")

# 练习2
user = {}
username = input("请输入账号")
if len(username) < 5 or len(username) > 8:
    print("账号长度应为5-8位")
    username = input("请重新输入账号")
password = input("请输入密码")
if len(password) < 6 or len(password) > 12:
    print("密码6-12位")
    password = input("请重新输入密码")
user = {username: password}
print(user)
 """
""" 
   # 老师答案
   # 练习1
   light = {"红灯": 30, "绿灯": 35, "黄灯": 3}
   for i in light:
       for j in range(light[i]):
           print(i, "倒计时还有", light[i]-j, "秒")
    """
# 练习2
username = input("请输入账号")
password = input("请输入密码")
if len(username) >= 5 and len(username) <= 8:
    if username[0] > "a" and username[0] < "z":
        if len(password) >= 6 and len(password) <= 12:
            print("注册成功", {username: password})
        else:
            print("密码必须6-12位")
    else:
        print("账号必须以小写字母开头")
else:
    print("账号必须5-8位")

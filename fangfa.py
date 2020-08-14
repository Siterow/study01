# 8.12方法的定义和异常的捕获

def checkname(username):
    """ 
    自动判断账号是否符合规范  
     """
    if len(username) >= 5 and len(username) <= 8:
        if username[0] > "a" and username[0] < "z":
            print("ok")
        else:
            print("账号必须以小写字母开头")
    else:
        print("账号必须5-8位")

# checkname("s12346")
# def 方法的申明
# checkname 方法的名字
# username 方法的参数
# """ 方法的说明 """


def jiafa(a, b):
    """ 加法 """
    if type(a) is int and type(b) is int:
        return a + b
    else:
        return "请输入数字"
# jiafa(23, 3)
# jiafa("23", "3")


a = []
print(a.append("哈哈"))
print(a)
print(a.count("哈哈"))
print(jiafa(1, 1))

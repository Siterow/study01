# 判断
"""
a = 1
b = 2
if a == b:
    print("这两个数一样大")
if a > b:
    print("a大")
else:
    print("b大")

age = int(input("输入年龄"))
if age > 60:
    print(1)
elif age > 30:
    print(2)
elif age > 20:
    print(3)
else:
    print(4)
 """


# in的使用
"""
a = "你好"
if a in "你好吗":
    print("ok")
else:
    print("不ok")  # 也可以使用在字典、数组等
 """
"""
a = input("请输入")
if a == "":
    print("a不能为空")
    exit()
if a in "0123456789":
    a = int(a)
else:
    print("请输入数字")
    exit()
 """

"""
#  8.12循环 while & for
a = 1
while a < 10:
    print("这是第", a, "次循环")
    a = a+1
 """

"""
练习：
现在有10个学生的成绩需要录入系统中
名字分别为：a1,b2,c3,d4,e5,f6,g7,h8,i9,k10
并且名字和成绩需要对应上，并且成绩大于60的和小于60的需要分开存放
 """
"""
   studentlist = ["a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8", "i9", "k10"]
   highchengji = {}
   lowchengji = {}
   a = 0
   while a < len(studentlist):
       chengji = int(input("请输入" + studentlist[a] + "的成绩"))
       if chengji >= 60:
           highchengji[studentlist[a]] = chengji
       else:
           lowchengji[studentlist[a]] = chengji
       a = a + 1
   print("成绩60以上的", highchengji)
   print("成绩60以下的", lowchengji)
    """
"""
#  for循环的使用 遍历
a = ["a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8", "i9", "k10"]
for i in a:
    print(i)  # 遍历一遍a，依次输出

b = list(range(0, 100, 2))  # range(开始值，小于结束值，步进)
print(b)
 """
""" 
studentlist = ["a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8", "i9", "k10"]
highchengji = {}
lowchengji = {}
for i in studentlist:
    chengji = int(input("请输入" + i + "的成绩")) #for循环会自动遍历该字典中的每一个元素
    if chengji >= 60:
        highchengji[i] = chengji
    else:
        lowchengji[i] = chengji  
print("成绩60以上的", highchengji)
print("成绩60以下的", lowchengji)
 """

""" 
练习：
打印9*9乘法表
 """
for i in range(1, 10):  # 相当于java中for(i=1;i<10;i++);
    for j in range(1, i+1):
        k = i * j
        print(i, "x", j, "=", k, end="  ")  # end的用途是每一个输出最后加一个end值
    print()  # 换行

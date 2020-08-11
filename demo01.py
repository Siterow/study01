""" 
print("hello world")
print(233333)
print(True)
print(())
8.10 print
"""

""" 
a=int(input())
b=int(input())
print(a+b,a-b,a*b,a/b)
print(type(a))
print(type(b))
8.10 input
"""

""" 
# 元祖练习8.11
a=(1,2,3,4,"嘻嘻嘻嘻",True,False,3,3,3)
print(a)
print(a[3],a[5])
print(a.index(2)) #index输出下标,只能输入一个值
print(a.count(3)) #统计值的数量

# 二维元祖
b=(a,5,5,5,6,6,23,100,"呜呜呜呜","嘿诶嘿嘿")
print(b[1])
print(b[0][3])
print(b[0][5])
print(b.count(4))
print(b.index("呜呜呜呜"))

#切片
print(a[0:4])
print(a[:4])
print(a[6:])
 """

""" 
 #数组的学习
a = [1,2,3,4,"嘻嘻嘻嘻",True,False,3,3,3]
print(a[3])   #元祖不可以后期修改，数组可以后期修改
a.append("增加数组元素1")
a.append("增加数组元素2") #只能插入在最后
print("第1次修改后",a)
a.insert(0,"插入元素0") #在指定位置插入元素
a.insert(4,5)
print("第2次修改后",a)
a.pop(4) #剪切指定下标元素
print("第3次修改后",a)
b=a.pop(0)
print(b)
xx=[20,21]
a.extend(xx) #合并两个数组
print(a)
print(a+xx)
a.remove(21) #删除指定值
print(a)
 """

""" 
python中所有的方法都是（）结尾，
元组、字典的取值都使用[]
元组、数组、字典的定义分别为()、[]、{}
 """

# 字典的学习

""" 
 字典的特点：
 1、字典中的值没有顺序。
 2、字典的接口必须是 键值对的结构。key=value  
 例如 
 a={"name":"张三"，
    0："哈哈",
    "age":13} 我觉得看起来很像sql里的字段名和对应的值
 """

a = {"name": "张三", "状态": "哈哈", "age": 13}
# 取值
print(a)
# 新增
a["sex"] = "女"  # a[key]=new value
print(a)
# 修改
a["name"] = "张三换个名字吧"  # 直接改
print(a)
# 字典里的常用方法 get pop update
b = a.get("name")
print(b)

c = a.pop("name")
print(a)
print(c)

a.update(id=000)
print(a)

# 数组和字典的删除使用del方法
del a["sex"]
print(a)

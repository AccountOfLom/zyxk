


# def 是关键字，表示要定义一个函数了，后面跟函数名
# 参数名其实就是定义一个去接收数据的变量，变量名可以随意编写，符合规范即可
# def out(name):
#     print(name + "out了")
#
# xingming = "小孩哥"
# out(xingming)



# def demo(name, age):
#     print("我是用来调试关键字参数的函数:" + name + "；年龄：" + age)
# 关键字参数
# demo(name = "佩奇", age = "18")
# demo(age = "18", name = "佩奇")


# 在函数定义中，如果给参数设定了一个值，这个值就是默认值，但是会被所传的值覆盖
# 有默认值的参数可以不传
def demo(age = "99", name = "佩奇"):
    print("我是用来调试关键字参数的函数:" + name + "；年龄：" + age)

demo("98", "阿海")



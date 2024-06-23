


# js 以及很多的编程语言，都是通过  function 关键字来定义函数的
# function myFunc()
# {}

# python 是通过 def 来定义的


def out():
    print("你out了")
    print("不，我很fashion")


# 函数可以有一个或多个参数，参数可以是任意数据类型
def whoOld(personOne, personTwo):
    if personOne['age'] > personTwo['age']:
        print(personOne['name'] + "年纪更大")
    else:
        print(personTwo['name'] + "年纪更大")


xiaoHong = {
    "name":"小红",
    "age":18
}
xiaoHai = {
    "name":"小孩哥",
    "age":9
}

whoOld(xiaoHong, xiaoHai)


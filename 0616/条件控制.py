
# 条件控制
account = "18513145200"
password = "123456"

if account == "正确的账号" and password == "正确的密码":
    print("登录成功，并且跳转到主页")
else:
    print("登录失败，留在登录页面")

# 注意父子级的关系，子级相对父级要缩进4个空格
# if account == "正确的账号":
#     if account == "正确的账号" and password == "正确的密码":
#         print("登录成功，并且跳转到主页")
#     else:
#         print("登录失败，留在登录页面")
# else:
#     print("去注册")
#     # if....  判断账号是否存在
#





age = int(input("请输入你家狗狗的年龄: "))
print("")

# 开始匹配
match age:
    case 5:  # 条件判断
        print("和大人一桌")
    case 6:
        print("和小孩一桌")
    case 7:
        print("和小猫一桌")
    case _:
        print("年龄不在范围")


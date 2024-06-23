

# 不定长参数的定义，需在参数名前加 * 号
def students(*names):
    # print(names)
    for name in names:
        print(name)

students("大海，你全是水", "朱朱", "清清")
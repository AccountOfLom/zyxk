
# 这是一个操作mysql的包
# pip3 install pymysql
import pymysql
from datetime import datetime

# 数据库对象 db （database）
class db:
    # 连接
    query = None

    # 构造方法，在对象被实例化时会自动执行
    def __init__(self):
        self.query = pymysql.connect(
            host = 'localhost',     # 数据库地址， localhost（等同于127.0.0.1） 是本机的意思
            port = 8001,            # 端口，MySQL默认3306（如果没有去修改的话）
            user = 'bor_m',          # 数据库的账号
            password = 'bor_m',      # 数据库密码
            db ='bor_m',             # 库名
            charset = 'utf8mb4'     # 字符集
        )

    # 获取格式化后的时间
    def now(self):
        # 获取当前时间
        now = datetime.now()
        # 将时间格式化为 Y-m-d H:i:s 格式
        return now.strftime('%Y-%m-%d %H:%M:%S')

    # 查询方法
    def __get(self, sql):
        # print("执行语句：" + sql)
        # 操作对象
        obj = self.query.cursor()
        # 执行查询
        obj.execute(sql)
        data = obj.fetchall()
        # 关闭连接
        obj.close()
        self.query.close()

        # obj.description 获取列名(字段名)
        # 通过 for in 将字段遍历给 columns
        columns = [column[0] for column in obj.description]
        # 将结果转换为字典列表
        rowsDict = []
        for row in data:
            field = dict(zip(columns, row)) # 构建字段映射
            rowsDict.append(field)          # 写入到 rowsDict 字典结果中
        return rowsDict

    # 读取符合条件的一条数据
    def getOne(self, sql):
        rowsDict = self.__get(sql)
        if len(rowsDict) == 0:
            print("查无数据")
            return None
        return rowsDict[0]  # 只获取第一个

    # 读取符合条件的所有数据
    def getAll(self, sql):
        rowsDict = self.__get(sql)
        return rowsDict  # 返回全部

    # 写入数据
    def add(self, table, keyValue):
        field = ""  # 所有字段
        value = ""  # 所有的值
        # 循环，组装 字符串
        for i in keyValue:
            field += ',' + i
            value += ", '{}'".format(keyValue[i])
        # 删除开头的 , 号
        field = field[1:]
        value = value[1:]

        sql = "insert {} ({}) values ({})".format(table, field, value)
        print(sql)
        # 执行sql
        # 操作对象
        obj = self.query.cursor()
        # # 执行
        obj.execute(sql)
        # 提交更改
        self.query.commit()
        # 关闭连接
        obj.close()
        self.query.close()


    # 更新数据
    def update(self, sql):
        # 数据库操作对象
        query = self.query.cursor()
        # 执行sql (mysql命令)
        query.execute(sql)
        # 提交更改，确认执行
        self.query.commit()
        # 关闭连接
        query.close()
        self.query.close()

    # 删除数据
    def delete(self, sql):
        # 数据库操作对象
        query = self.query.cursor()
        # 执行sql (mysql命令)
        query.execute(sql)
        # 提交更改，确认执行
        self.query.commit()
        # 关闭连接
        query.close()
        self.query.close()

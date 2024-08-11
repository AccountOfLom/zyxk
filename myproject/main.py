from flask import Flask, request
import db
import json
import dateTimeEncoder
from flask_cors import CORS
import datetime

app = Flask(__name__)
# 允许跨域请求
CORS(app)

# route 表示定义一个接口，接口地址中，只有一个 “/”，表示根目录
@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"


# 几乎所有应用，代码执行的核心，都是对数据的增、删、改、查

# 登录接口
@app.route("/login")
def login():
    return "账号<input><br>密码<input><br><button>登录</button>"


# 人物列表
@app.get("/member")
def member():
    query = db.db()
    data = query.getAll("select * from bother_sisters") # 这个方法得到的是一个字典
    # python后端接口，返回数据给客户端页面，需要用到一个数据格式，json

    # [{'id': 1, 'name': 'naonao', 'created_at': datetime.datetime(2024, 7, 28, 11, 50)}, {'id': 2, 'name': '团团', 'created_at': datetime.datetime(2024, 7, 28, 11, 50, 14)}]
    print(data)
    # data 转为 json格式时，可以通过 cls关键字来声明数据的处理
    json_data = json.dumps(data, cls=dateTimeEncoder.DateTimeEncoder)
    return json_data


# 电脑列表查询
@app.get("/computer")
def computer():
    query = db.db()
    data = query.getAll("select * from computers")
    json_data = json.dumps(data, cls=dateTimeEncoder.DateTimeEncoder)
    return json_data


# 添加电脑的接口，在这个接口，需要接收客户端提交的参数(电脑信息)，而后写入到数据库
@app.post("/computer") # 此接口只接受 post 请求
def computerAdd():
    # 获取参数
    sysVersion = request.form.get('system_version')
    notes = request.form.get('notes')
    # print("系统版本" + sysVersion + "；备注：" + notes)
    # 组装需要写入到数据库的数据
    data = {
        "system_version":sysVersion,
        "notes":notes,
        "created_at":datetime.datetime.now()
    }
    # 获取 db 数据库执行对象
    query = db.db()
    # 写入数据
    query.add("computers", data)
    # 跳转回列表页
    return "<script>alert('操作成功');window.history.back();</script>"


# 编辑接口
@app.put("/computer") # 此接口只接受 put 请求
def computerEdit():
    # 获取参数
    id = request.form.get('id') # 所编辑的电脑的ID
    sv = request.form.get('sv') # 系统版本
    notes = request.form.get('notes') # 备注信息

    # 1、检查数据库字段值，排查显示问题
    # 2、后端取值有没有问题
    # 3、前端传值有没有问题

    # 获取 db 数据库执行对象
    # 组装字符串sql， sql 就是操作数据库的命令
    sql = f"update computers set system_version = '{sv}',notes = '{notes}'  where id = {id}"
    query = db.db()
    query.update(sql)
    # 返回了一个 json 数据（这里的json，是一个约定的数据格式），通知客户端处理结果
    json_data = json.dumps({"status":1, "msg":"操作成功"})
    return json_data


# 添加人员的接口，在这个接口，需要接收客户端提交的参数(人员信息)，而后写入到数据库
@app.post("/member") # 此接口只接受 post 请求
def memberAdd():
    # 获取参数
    name = request.form.get('name')
    # 组装需要写入到数据库的数据
    data = {
        "name":name,
        "created_at": datetime.datetime.now()
    }
    # 获取 db 数据库执行对象
    query = db.db()
    # 写入数据
    query.add("bother_sisters", data)
    # 跳转回列表页
    return "<script>alert('操作成功');window.history.back();</script>"


# 编辑接口
@app.put("/member") # 此接口只接受 put 请求
def memberEdit():
    # 获取参数
    id = request.form.get('id') # 所编辑的用户的ID
    name = request.form.get('name') # 修改的数据
    # 获取 db 数据库执行对象
    # 组装字符串
    sql = f"update bother_sisters set name = '{name}' where id = {id}"
    query = db.db()
    query.update(sql)
    # 返回了一个 json 数据（这里的json，是一个约定的数据格式），通知客户端处理结果
    json_data = json.dumps({"status":1, "msg":"操作成功"})
    return json_data


# 编辑接口
@app.delete("/member") # 此接口只接受 delete 请求
def memberDel():
    # 获取参数
    id = request.form.get('id') # 所编辑的用户的ID
    # 获取 db 数据库执行对象
    # 组装字符串
    sql = f"delete from bother_sisters where id = {id}"  # f"字符内容"，这是python组装字符串的一个方式
    query = db.db()
    query.delete(sql)
    # 返回了一个 json 数据（这里的json，是一个约定的数据格式），通知客户端处理结果
    json_data = json.dumps({"status":1, "msg":"操作成功"})
    return json_data


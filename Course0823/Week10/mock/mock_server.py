#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @File    : mock_server.py
# @Author  : Baoshun.Chin
# @Email   : baoshunchin@qq.com
# @Time    : 2020-11-08 10:08
# @Site    : 
# @version : V1.0

from flask import Flask,Response,json,request,jsonify
from Week10.mock.through import passThrough,passThroughRe

app = Flask(__name__)
app.config['JSON_AS_ASCII']=False
#编写mock路由，说明这个接口是当前系统需要被mock的一个接口
@app.route('/login',methods=["POST"])
def login():
    # 1.接收入参
    # url = 'login'
    data = json.loads(request.get_data(as_text=True))
    name = data['name']
    pwd = data['password']
    # 2.实现多种异常返回
    if name =='被锁定':
        return jsonify({'code':402,'name':'被锁定','res':'用户被锁定'})
    elif name =='黑名单':
        return jsonify({'code': 445, 'name': '黑名单', 'res': '您已进入我司很名单，请联系我们的售后专员'})
    elif name =='今日密码错误次数超过限制':
        return jsonify({'code': 201, 'name': '今日密码错误次数超过限制', 'res': '您今日密码错误次数超过限制，请联系我们的售后专员进行解锁'})
    elif name == '本日幸运用户':
        return jsonify({'code': 201, 'name': '本日幸运用户', 'res': '恭喜您称为本日第一个登陆系统的用户，后台将发送给您100元代金券一张'})
    elif name == '账单逾期':
        return jsonify({'code': 201, 'name': '账单逾期', 'res': '您的账号已经预期，请尽快处理'})
    # elif name == '注册为优质客户':
    #     需要实现在数据库搭上“优质”标签的sql
    #     然后再返回相应信息

    # 这里产生了一个问题，真实服务和mock服务是两个服务。怎么让我们的被测系统调用到“mock服务”呢？
    # 例如：
    #     我希望调用mock服务也能进行真正的“登录”，这里就需要实现一个“透传”
    else:
        #如果我们接受到的数据，没有进入任何一个“后门”，那么我们就调用透传，来使用“真实”服务
        url = 'login'
        resp = passThrough(url,data)
        return resp

# 问题2：
# 在真实的项目配置里，我们的配置一般到“系统”一级。一个系统下辖了若干接口，这就会导致mock里边出现了
# “需要被mock的接口”和“不需要被mock的接口”
# 这就产生了“针对接口”mock的需求
# 使用flask的动态路由功能
@app.route('/<func>',methods = ['POST'])
def through(func):
    print(f'当前的{func}接口没有实现过mock功能，所以直接进入透传调用真实服务')
    data = request.get_json()
    resp = passThroughRe(url=func,data=data)
    return resp


if __name__ == '__main__':
    app.run(port=5001)
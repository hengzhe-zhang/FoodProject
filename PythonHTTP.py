#Flask服务器模块
from flask import Flask,request,session
from MainModel import User,Order,Food,Order_Food
from PlayHouse.shortcuts import dict_to_model,model_to_dict
import json
app=Flask(__name__)
app.secret_key='Food'
# app.debug=True
#登录模块
@app.route('/login/<user_id>+<password>',methods=['post','get'])
def user_login(user_id,password):
    print(request.form)
    # user_id=request.form['']
    try:
        user=User.get((User.user_id==user_id)&(User.password==password))
        return json.dumps(model_to_dict(user))
    except:
        return '登陆失败'
#获取余菜数量
@app.route('/get_food_num/<food_id>', methods=['post', 'get'])
def get_food_num(food_id):
    food=Food.get(Food.food_id==food_id)
    food_str={'name':food.name,'num':food.num}
    return json.dumps(food_str)
#获取餐饮记录模块
@app.route('/get_food_history/<user_id>+<password>',methods=['post','get'])
def get_food_history(user_id,password):
    try:
        user=User.get((User.user_id==user_id)&(User.password==password))
        order=Order.select().where(Order.user_id == user.user_id)[-1]
        print(order.id)
        #食物订单和ID列表
        order_food_list=Order_Food.select().where(Order_Food.id==order.id)
        print(len(order_food_list))
        food_list=[]
        for order_food in order_food_list:
            food_list.append(model_to_dict(Food.get(id=order_food.food_id)))
        #食物ID映射
        for food in food_list:
            if food['name']=='煎蛋':
                food['id']=1
            if food['name']=='二两米饭':
                food['id']=2
            if food['name']=='炒空心菜':
                food['id']=3
            food['num']=order_food_list[food_list.index(food)].food_num
            food['time']=order.date
        return json.dumps(food_list)
    except:
        return '密码错误'
app.run(host='0.0.0.0')
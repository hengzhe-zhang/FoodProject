#TCP监听服务器（客户）
import socket,threading,datetime
from  SendInformation import senddata
from MainModel import Order,Order_Food,Food,User
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('0.0.0.0',9998))
s.listen(5)
print('服务器用户端口成功启动')
#从数据库中读取用户信息
def GetPersonFromDB(id):
    user_list=User.select()
    for user in user_list:
        if str(user.user_id).__contains__(id[0:4]):
            return user
#删除食品
def DelFood(food_id):
    food=Food.get(Food.id==food_id)
    food.num=food.num.__int__()-1
    food.save()
#存储订单
def InsertOreder(person):
    num=len(Order.select())
    print('创建订单开始')
    new_order=Order().create(id=num+1,user_id=person.user_id,date=datetime.datetime.now())
    print('创建订单成功')
    return num+1
#存储订单食物关系表
def SaveOrderFood(order_id, food_id_list):
    for food_id in food_id_list:
        print(food_id)
        DelFood(food_id)
        try:
            order_food=Order_Food().create(id=order_id,food_id=food_id,food_num=1)
            print('创建订单详细信息成功')
        except:
            order_food=Order_Food.get(id=order_id,food_id=food_id)
            print(order_food.food_num)
            order_food.food_num=order_food.food_num+1
            order_food.save()
            print('创建订单详细信息失败')
#TCP处理函数
def tcplink(sock,addr):
    while True:
        data=sock.recv(1024)
        if not data:
            break
        data=data.decode('ascii')
        if len(data)<5:
            break
        with open('data.txt','r') as d:
            food_data=d.readlines()
            buy_food_list=str(food_data).split(' ')
            print(buy_food_list)
            #购买食品对应ID列表
            buy_food_id_list=[]
            food_list=Food.select()
            print('食品信息表{}'.format(food_list))
            #从数据库中查找食物对应的ID
            for new_food in buy_food_list:
                for food in food_list:
                    if new_food.__contains__(food.name):
                        buy_food_id_list.append(food.id)
            #存储订单
            person=GetPersonFromDB(data)
            new_order_id=InsertOreder(person)
            #存储详细订单
            SaveOrderFood(new_order_id,buy_food_id_list)
            print('存储完成')
        #清空历史
        with open('data.txt','w') as d:
            d.write('')
        print('服务器成功接收到用户信息'+person.nickname)
        senddata(person.nickname)
while True:
    sock,addr=s.accept()
    t=threading.Thread(target=tcplink,args=(sock,addr))
    t.start()
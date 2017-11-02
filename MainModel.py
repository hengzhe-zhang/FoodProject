import peewee,json
import logging
database=peewee.MySQLDatabase(host='localhost',user='root',password='',port=3306,database='canteen')
logger=logging.getLogger('peewee')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())
class BaseModel(peewee.Model):
    class Meta:
        database=database
class Food(BaseModel):
    #食物芯片ID
    id=peewee.CharField()
    #食物ID
    food_id=peewee.IntegerField(primary_key=True)
    #食物名称
    name=peewee.CharField()
    #食物余量
    num=peewee.IntegerField()
class User(BaseModel):
    #用户ID
    user_id=peewee.CharField(primary_key=True)
    #密码
    password=peewee.CharField()
    #昵称
    nickname=peewee.CharField()
    #相片
    photo=peewee.CharField(null=True)
    #性别
    sex=peewee.CharField(null=True)
    #住址
    location=peewee.CharField(null=True)
    #身高
    height=peewee.FloatField(null=True)
    #体重
    weight=peewee.FloatField(null=True)
class Order(BaseModel):
    #订单ID
    id=peewee.IntegerField()
    #用户ID
    user_id=peewee.CharField()
    #日期
    date=peewee.CharField()
class Order_Food(BaseModel):
    # 订单ID
    id = peewee.IntegerField()
    #食物ID
    food_id=peewee.CharField()
    #食物数量
    food_num=peewee.IntegerField()
    class Meta:
        database=database
        primary_key= peewee.CompositeKey('id','food_id')
if __name__ == '__main__':
    database.connect()
    # Food.create_table()
    # User.create_table()
    # Order.create_table()
    # Order_Food.create_table()
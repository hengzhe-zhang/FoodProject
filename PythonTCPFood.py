#TCP监听服务器（食物）
import socket,threading
from  SendInformation import senddata
from flask import Flask
from MainModel import Food
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('0.0.0.0',9999))
s.listen(5)
print('服务器食物端口成功启动')
def tcplink(sock,addr):
    while True:
        data=sock.recv(1024)
        if not data:
            break
        foods = Food.select()
        content=data.decode('utf8')
        send_str = ''
        if 30 > len(content) > 10:
            for food in foods:
                if str(food.id).__contains__(content[2:7]):
                    print('接收到信息{}'.format(food.name))
                    send_str = send_str + str(food.name) + ' '
        else:
            for food in foods:
                if str(content).__contains__(food.id[2:7]):
                    print('接收到信息{}'.format(food.name))
                    send_str = send_str + str(food.name) + ' '
        with open('data.txt','a') as d:
            d.write(send_str)
        print('服务器成功接收到食物信息'+data.decode('utf8'))
        senddata(send_str)
while True:
    sock,addr=s.accept()
    t=threading.Thread(target=tcplink,args=(sock,addr))
    t.start()
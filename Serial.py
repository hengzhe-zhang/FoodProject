#串口通信模块
import socket
import time

import serial

from MainModel import *

com_num=input('请输入端口号')
s=serial.Serial('com{}'.format(com_num),115200)
ip_address=''
port=9999
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((ip_address,port))
while True:
    content=str(s.read_all())
    if not content=='b\'\'' :
        print(content)
        sock.send(content.encode('utf8'))
    time.sleep(0.03)
#TCP通信测试
import socket,time
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('ip',9999))
s.send(str(50).encode('utf8'))
time.sleep(0.2)
s.send(str(60).encode('utf8'))
time.sleep(0.2)
s.send(str(70).encode('utf8'))
time.sleep(0.2)
s.send(str(80).encode('utf8'))
time.sleep(0.2)
s.close()
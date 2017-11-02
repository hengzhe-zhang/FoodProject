### 基于OneNET云平台的膳食分析系统
#### 项目概述
![](http://on2oj7i3h.bkt.clouddn.com/17-11-2/16547938.jpg)
#### 配置方案
项目基于Mysql+serial+Flask+peewee  
* serial+Flask+peewee 可以使用PIP安装最新版本  
* Mysql 安装最新版本，执行项目根目录下的canteen,sql即可
### 项目结构  
模块名|功能  
---|---  
Serial.py|端口通信脚本
SendInformation.py|通过API向Onenet平台发送数据
PythonTCPFood.py|TCP通信脚本
PythonHTTP.py|HTTP服务器脚本
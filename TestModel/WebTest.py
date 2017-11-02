import requests,datetime
from bs4 import BeautifulSoup
#登录测试模块
def LoginTest():
    ip='http://ip:5000/get_food_num/8B95E1C4+123456'
    # login_data={'user_id':'8B95E1C4'}
    sess=requests.session()
    req=sess.post(ip)
    # req=sess.get('http://192.168.1.100:5000/get_food_history')
    soup=BeautifulSoup(req.text,'lxml')
    print(soup.text)
if __name__ == '__main__':
    LoginTest()
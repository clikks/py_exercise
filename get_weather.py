# _*_ coding:utf-8 _*_
__author__ = 'lux'

import requests



def weather_info(city = '北京'):

    url = 'http://wthrcdn.etouch.cn/weather_mini?city=%s' %city
    req = requests.get(url)
    req.encoding = 'utf-8'
    print(req.text)
    data = req.json()
    print(data)


city = input('*' * 30 + '\n\t' + "输入您要查询天气的城市:" \
             + '\n' + '*' * 30 + '\n')
if city == '':
    weather_info()
else:
    weather_info(city)
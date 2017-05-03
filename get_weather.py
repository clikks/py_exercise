# _*_ coding:utf-8 _*_
__author__ = 'lux'

import requests,re


def weather_info(city = '北京'):

    url = 'http://wthrcdn.etouch.cn/weather_mini?city=%s' %city
    req = requests.get(url)
    req.encoding = 'utf-8'
    data = req.json()

    print('城市:',req.json()['data']['city'])
    print('当前气候：',req.json()['data']['wendu'] + '℃',end=' ')
    print(req.json()['data']['forecast'][0]['type'])

    low = req.json()['data']['forecast'][0]['low']
    high = req.json()['data']['forecast'][0]['high']
    #提取当日高低气温值
    pattern = re.compile(r'\d+\W')
    x = pattern.findall(low)
    y = pattern.findall(high)
    print('今日气温：',x[0],'~',y[0] )
    #格式化输出当日气温

    print('风力风向：',req.json()['data']['forecast'][0]['fengli'],end=' ')
    print(req.json()['data']['forecast'][0]['fengxiang'])
    print('空气质量AQI：',req.json()['data']['aqi'])


city = input('*' * 30 + '\n\t' + "输入您要查询天气的城市:" \
             + '\n' + '*' * 30 + '\n')
if city == '':
    weather_info()
else:
    weather_info(city)

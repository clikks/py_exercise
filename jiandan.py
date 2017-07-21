#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
__author__ = 'lux'

import requests
import re
from bs4 import BeautifulSoup

class Beauty:
    def __init__(self, start=0, end=0):
        self.start = int(input("请输入起始页："))
        self.end = int(input("请输入终止页："))
        # self.url = 'http://jandan.net/ooxx/page-%d#comments'

    def pic_url(self):
        page = 'http://jandan.net/ooxx/page-%d#comments' %self.start
        Url = requests.get(page)
        # print(page)
        Html = BeautifulSoup(Url.text,'lxml')
        Img_url = Html.find_all('a',class_ = 'view_img_link')
        # print(Img_url)
        image = []
        for i in Img_url:
            i = str(i)
            result = re.findall(r'href="//(\w+\d.\w+.\w+/\w+/\w+\.(jpg|gif|png|bmp))',i)
            image.append(result[0][0])
            print(image)

    def download(self):

HtmlOpen = requests.get('http://jandan.net/ooxx')
# HtmlOpen.encoding = 'utf-8'
# with open('jiandan.html','w',encoding='utf-8') as f:
#     f.write(HtmlOpen.text)
# Soup = BeautifulSoup(open('jiandan.html',encoding='utf-8'),'lxml')
Soup = BeautifulSoup(HtmlOpen.text,'lxml')
tag = Soup.find_all('span',class_='current-comment-page')
page = str(tag[0].contents[0])
comment_page = int(re.findall(r'\w+',page)[0])
# print(comment_page)

C1 = Beauty()
C1.pic_url()




# top = tkinter.Tk()
# top.title('煎蛋妹子图下载器')
# top.geometry('400x200')
# def pageButton():
#     print('目录')
# button = tkinter.Button(top,text = '下载路径',command = pageButton).pack()
# top.mainloop()
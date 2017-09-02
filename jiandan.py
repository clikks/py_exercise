#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
__author__ = 'lux'

from bs4 import BeautifulSoup
import urllib.request
import re
import posixpath

class Beauty:
    def __init__(self, start=0, end=0,image=[]):
        self.start = int(input("请输入起始页："))
        self.end = int(input("请输入终止页："))
        self.image = image
        # self.url = 'http://jandan.net/ooxx/page-%d#comments'

    def pic_url(self):
        for input_pages in range(self.start,self.end+1):
            pages = 'http://jandan.net/ooxx/page-%d#comments' %input_pages
            Url = urllib.request.urlopen(pages)
            # print(page)
            Html = BeautifulSoup(Url.read(),'lxml')
            Img_url = Html.find_all('a',class_ = 'view_img_link')
            # print(Img_url)
            for i in Img_url:
                i = str(i)
                result = re.findall(r'href="//(\w+\d.\w+.\w+/\w+/\w+\.(jpg|gif|png|bmp))',i)
                self.image.append(result[0][0])
                # print(image)

    def download(self):
        # print(self.image)
        # pattern = r'\w+\.(jpg|gif|png|bmp)'
        for pic in self.image:
            print(type(pic))
            img_name = re.findall(r'(\w+\.(jpg|gif|png|bmp))',pic)[0][0]
            pic_url = "http://" + pic
            img_page = urllib.request.urlopen(pic_url,timeout=10).read()
            with open(img_name,'wb') as f:
                f.write(img_page)

HtmlOpen = urllib.request.urlopen('http://jandan.net/ooxx')
Soup = BeautifulSoup(HtmlOpen.read(),'lxml')
tag = Soup.find_all('span',class_='current-comment-page')
print(tag)
page = str(tag[0].contents[0])
comment_page = int(re.findall(r'\w+',page)[0])
print(comment_page)

C1 = Beauty()
C1.pic_url()
C1.download()



# top = tkinter.Tk()
# top.title('煎蛋妹子图下载器')
# top.geometry('400x200')
# def pageButton():
#     print('目录')
# button = tkinter.Button(top,text = '下载路径',command = pageButton).pack()
# top.mainloop()
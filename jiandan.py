#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
__author__ = 'lux'

import urllib.request
import urllib.parse
import tkinter as tk
# start = int(input("请输入起始页："))
# end = int(input("请输入终止页："))
# url = 'http://jandan.net/ooxx/page-%d#comments'
# print(url %start)

class Beauty:
    def __init__(self,start,end,url):
        self.start = int(input("请输入起始页："))
        self.end = end = int(input("请输入终止页："))
        self.url = 'http://jandan.net/ooxx/page-%d#comments'

    # def
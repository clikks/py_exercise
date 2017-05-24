#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
__author__ = 'clikks'

import os

print("=" * 24 + '\n' + " 奥运奖牌榜查询处理程序\n" + "=" * 24)

def value(num,chose):
    while True:
        try:
            chose = int(chose)
            while chose > num:
                chose = int(input("选项错误，请重新选择:\n" + ">>> "))
            break
        except ValueError:
            chose = input("请使用数字选择:\n" + ">>> ")

if os.path.exists('./medals_tally.db'):
    judge = True
    chose = input("请选择您需要的操作:\n"
                + "1) 查看奖牌榜\n"
                + "2) 查看金牌榜\n"
                + "3) 增加国家奖牌数量\n"
                + "4) 退出程序\n"
                + ">>> "
                  )
    value(4,chose)

else:
    judge = False
    chose = input("暂无奖牌榜数据，您可执行以下操作:\n"
          + "1) 增加国家奖牌数量\n"
          + "2) 退出程序\n"
          + ">>> "
          )
    value(2,chose)



class File_operate:
    def __init__(self,dir ='./new_tally.db' ):
        self.dir = dir

    def openfile(self):
        global new
        if chose == 1:
            self.dir = './medals_tally.db'

        with open(self.dir, 'r') as f:
            new = {}
            for line in f.readlines():
                line = line.strip()
                text = line.split(':')[1].split(",")
                text.pop()
                new[line.split(':')[0]] = text

    def writefile(self,dir = './new_tally.db'):
        self.dir = dir()
        with open(self.new_tally,'w+') as f:
            for i in new:
                f.write(i + ":")
                for s in new[i]:
                    f.write(s + ",")
                f.write('\r')

class Medal_tally:
    def __init__(self,name = 'china',gold=0,silver=0,copper=0):
        self.name = name
        self.gold = gold
        self.silver = silver
        self.copper = copper
    #定义Medal_tally的属性，国家名name，金牌glod，银牌silver，铜牌copper

    def new_tally(self):
        self.name = input("please enter country:")
        print(self.name)
        self.gold = input("请输入新增金牌数：")
        self.silver = input("请输入新增银牌数：")
        self.copper = input("请输入新增铜牌数：")
        if new.get(self.name) != None:
            del new[self.name]
            new[self.name] = [self.gold,self.silver,self.copper]

        else:
            new[self.name] = [self.gold,self.silver,self.copper]
        print(new)
    # 定义新增奖牌数方法,将新增奖牌的国家名和新增数写入new字典

    # def sum_tally(self):

C1 = File_operate()
C1.openfile()
C2 = Medal_tally()
C2.new_tally()
C1.writefile()

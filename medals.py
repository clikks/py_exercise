#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
__author__ = 'clikks'

import os

def value(num,chose):
    while True:
        try:
            chose = int(chose)
            while chose > num:
                chose = int(input("选项错误，请重新选择:\n" + ">>> "))
            break
        except ValueError:
            chose = input("请使用数字选择:\n" + ">>> ")
#判断选择操作有效性的函数，防止用户输入错误的类型

class File_operate:
    # def __init__(self,dir):
    #     self.dir = dir

    def openfile(self,dir):
        self.dir = dir
        global new
        with open(self.dir, 'w+') as f:
            new = {}
            for line in f.readlines():
                line = line.strip()
                text = line.split(':')[1].split(",")
                # text.pop()
                new[line.split(':')[0]] = text

    def writefile(self,dir,dict):
        self.dir = dir
        self.dict = dict
        # self.dict2 = dict2
        with open(self.dir,'w+') as f:
            for i in self.dict:
                f.write(i + ":")
                for s in self.dict[i][0:-1]:
                    f.write(str(s) + ",")
                s = self.dict[i][-1]
                f.write(str(s))
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

    def sum_new_tally(self):
        global all_tally
        if judge == False:
            File_operate().writefile('./medals_tally.db',new)
            File_operate().writefile('./new_tally.db',new)
        else:
            all_tally = {}
            with open('./medals_tally.db','r') as f:
                for data in f.readlines():
                    data = data.strip()
                    print(data)
                    doc = data.split(':')[1].split(",")
                    print(doc)
                    all_tally[data.split(':')[0]] = doc
                print(all_tally)
                for i in range(3):
                    all_tally[self.name][i] = int(all_tally[self.name][i])
                    new[self.name][i] = int(new[self.name][i])
                    all_tally[self.name][i] += new[self.name][i]
                # all_tally[self.name][1] += new[self.name][1
                    print(all_tally)


print("=" * 24 + '\n' + " 奥运奖牌榜查询处理程序\n" + "=" * 24)
#输出程序title

if os.path.exists('./medals_tally.db'):
    judge = True
    chose = input("请选择您需要的操作:\n"
                + "1) 查看奖牌榜\n"
                + "2) 查看金牌榜\n"
                + "3) 增加国家奖牌数量\n"
                + "4) 清除奖牌数据库\n"
                + "5) 退出程序\n"
                + ">>> "
                  )
    value(4,chose)
    if chose == 3:
        C1 = File_operate()
        C1.openfile('./new_tally.db')
    else:
        C1 = File_operate()
        C1.openfile('./medals_tally.db')
else:
    judge = False
    chose = input("暂无奖牌榜数据，您可执行以下操作:\n"
          + "1) 增加国家奖牌数量\n"
          + "2) 退出程序\n"
          + ">>> "
          )
    value(2,chose)
    C1 = File_operate()
    C1.openfile('./new_tally.db')
#判断总奖牌榜数据文件是否存在，存在则给出全部操作选项，否则只能新增奖牌

# C1 = File_operate()
# print(new)
C2 = Medal_tally()
C2.new_tally()
C2.sum_new_tally()
if judge:
    C1.writefile('./medals_tally.db',all_tally)

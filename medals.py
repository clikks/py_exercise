#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
__author__ = 'clikks'

import os,sys

def value(num,chose):
    while True:
        try:
            chose = int(chose)
            while chose > num:
                chose = int(input("选项错误，请重新选择:\n" + ">>> "))
            return chose
            break
        except ValueError:
            chose = input("请使用数字选择:\n" + ">>> ")
            return chose
#判断选择操作有效性的函数，防止用户输入错误的类型

class File_operate:
    def openfile(self,dir):
        self.dir = dir
        global new
        with open(self.dir,encoding='utf-8') as f:
            new = {}
            data = f.readlines()
            for line in data:
                line = line.strip()
                text = line.split(':')[1].split(',')
                for i in range(3):
                    text[i] = int(text[i])
                new[line.split(':')[0]] = text
    #提供文件路径，并打开文件写入new字典。

    def writefile(self,dir,dict):
        self.dir = dir
        self.dict = dict
        with open(self.dir,'w+',encoding='utf-8') as f:
            for i in self.dict:
                f.write(i + ":")
                for s in self.dict[i][0:-1]:
                    f.write(str(s) + ",")
                s = self.dict[i][-1]
                f.write(str(s))
                f.write('\r')
    # 提供文件路径和需要写入文件的字典，将字典写入文件中。

class Medal_tally:
    def __init__(self,name = 'china',gold=0,silver=0,copper=0):
        self.name = name
        self.gold = gold
        self.silver = silver
        self.copper = copper
    #定义Medal_tally的属性，国家名name，金牌glod，银牌silver，铜牌copper

    def new_tally(self):
        self.name = input("please enter country:")
        self.gold = input("请输入新增金牌数：")
        self.silver = input("请输入新增银牌数：")
        self.copper = input("请输入新增铜牌数：")
        if judge and self.name in new:
            del new[self.name]
            new[self.name] = [self.gold,self.silver,self.copper]
        else:
            new[self.name] = [self.gold,self.silver,self.copper]
    # 定义新增奖牌数方法,将新增奖牌的国家名和新增数写入new字典

    def sum_new_tally(self):
        global all_tally
        if judge == False:
            File_operate().writefile(path + 'medals_tally.db',new)
            File_operate().writefile(path + 'new_tally.db',new)
        else:
            all_tally = {}
            with open(path + 'medals_tally.db','r',encoding='utf-8') as f:
                for data in f.readlines():
                    data = data.strip()
                    doc = data.split(':')[1].split(",")
                    for i in range(3):
                        doc[i] = int(doc[i])
                    all_tally[data.split(':')[0]] = doc
                if self.name in all_tally:
                    for i in range(3):
                        new[self.name][i] = int(new[self.name][i])
                        all_tally[self.name][i] += new[self.name][i]
                else:
                    all_tally[self.name] = new[self.name]
    #定义总奖牌计数方法，将新增奖牌数量加到原有奖牌数上。

    def sorting(self):
        board = {}
        for i in new:
            result = new[i][0] + new[i][1] + new[i][2]
            board[i] = result
        print('名次\t国家\t金牌数\t银牌数\t铜牌数',end='')
        x = 1
        if int(chose) == 1:
            rank = sorted(board.items(), key=lambda d: d[1], reverse=True)
            print('\t奖牌总数')
            for s in rank:
                str = '%d\t%s\t%s\t%s\t%s\t%s'\
                      %(x,s[0],new[s[0]][0],new[s[0]][1],new[s[0]][2],s[1])
                x += 1
                print(str)
        if int(chose) == 2:
            rank = sorted(new.items(), key=lambda d: d[1][0], reverse=True)
            print('\n',end='')
            for s in rank:
                str = '%d\t%s\t%s\t%s\t%s'\
                      %(x,s[0],new[s[0]][0],new[s[0]][1],new[s[0]][2])
                x += 1
                print(str)
        input('\nPlease enter to exit query!')
    #定义奖牌榜级金牌榜排序的方法，并格式化输出奖牌榜及金牌榜。

    def clean_db(self):
        if os.path.exists(path + 'new_tally.db') and os.path.exists(path + 'medals_tally.db'):
            os.remove(path + 'new_tally.db')
            os.remove(path + 'medals_tally.db')
    #定义清除奖牌榜数据库的方法。
run = True
while run:
    print("=" * 24 + '\n' + " 奥运奖牌榜查询处理程序\n" + "=" * 24)
    global path
    path = os.getcwd() + '/'

    if os.path.exists(path + 'medals_tally.db'):
        judge = True
        chose = input("请选择您需要的操作:\n"
                    + "1) 查看奖牌榜\n"
                    + "2) 查看金牌榜\n"
                    + "3) 增加国家奖牌数量\n"
                    + "4) 清除奖牌数据库\n"
                    + "5) 退出程序\n"
                    + ">>> "
                      )
        chose = value(5,chose)

        if int(chose) == 3:
            C1 = File_operate()
            C1.openfile(path + 'new_tally.db')
            C2 = Medal_tally()
            C2.new_tally()
            C1.writefile(path + 'new_tally.db', new)
            C2.sum_new_tally()
            C1.writefile(path + 'medals_tally.db', all_tally)
        if int(chose) == 4:
            C2 = Medal_tally()
            C2.clean_db()
        if int(chose) == 5:
            run = False
            sys.exit()
        elif int(chose) == 1 or int(chose) == 2:
            C1 = File_operate()
            C1.openfile(path + 'medals_tally.db')
            C2 = Medal_tally()
            C2.sorting()
    elif os.path.exists(path + 'new_tally.db'):
        os.remove(path + 'new_tally.db')
    else:
        judge = False
        new = {}
        chose = input("暂无奖牌榜数据，您可执行以下操作:\n"
              + "1) 增加国家奖牌数量\n"
              + "2) 退出程序\n"
              + ">>> "
                      )
        chose = value(2,chose)
        if int(chose) == 1:
            C2 = Medal_tally()
            C2.new_tally()
            C2.sum_new_tally()
        else:
            run = False
            sys.exit()


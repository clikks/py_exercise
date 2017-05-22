#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
__author__ = 'lux'

new = {}
# country = input("please enter country:")


class Medal_tally:
    def __init__(self,name = 'china',gold=0,silver=0,copper=0):
        self.name = input("please enter country:")
        self.gold = gold
        self.silver = silver
        self.copper = copper

    def new_tally(self):
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

    def writefile(self,add_tally = './new_tally.db'):
        self.add_tally = add_tally
        with open(self.add_tally,'w+') as f:
        
            f.write(new)
        # with open(./new_tally.db,)
    # def
country1 = Medal_tally()
country1.new_tally()

country2 = Medal_tally()
country2.new_tally()
country2.writefile()
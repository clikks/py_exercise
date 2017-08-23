#!/usr/bin/python3
# _*_ coding:utf-8 _*_
__author__ = 'anyco'


class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, n):
        if n == 1:
            return 0
        elif n > 1 and n <= 3:
            return 1
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)

while True:
    try:
        num = int(input('please enter a number:' + '\n'))
        while num <= 0:
            num = int(input('please enter interger!' + '\n'))
        c1 = Solution()
        print(c1.fibonacci(num))
        break
    except ValueError:
        print('ERROR NUMBER!!!' + '\n')
        continue



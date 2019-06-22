# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        a = 1
        b = 1
        for i in range(number):
            a,b = b,a+b
        return a
    
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        while number < 3 :
            return number
        front = 1
        behind = 2
        if number > 2:
            for i in range(number -2):
                front, behind = behind, front + behind
            return behind
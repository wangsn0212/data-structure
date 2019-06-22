# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number < 1:
            return 0
        p = q = r =0
        for i in range(1,number+1):
            if i == 1:
                p = q = r =1
            elif i == 2:
                q = r = 2
            else:
                r = q + p
                p = q
                q = r
        return r
    
    
class Solution:
    def rectCover(self, number):
        # write code here
        if number ==0 :
            return 0
        a = 1
        b = 1
        for i in range(number):
            a, b = b, a+b
        return a
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        return sum([(n>>i & 1) for i in range(0,32)])
    
    


class Solution:
    def NumberOf1(self, n):
        # write code here
        '''
        f=1
        c = 0
        for _ in range(32):
            if f&n>=1:
                c+=1
            f = f<<1
        return c
        '''
        c = 0
        if n<0:
            n = n&0xffffffff
        while n:
            c += 1
            n &= n-1
        return c
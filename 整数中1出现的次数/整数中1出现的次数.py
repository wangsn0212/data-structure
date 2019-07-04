# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        res=0
        tmp=n
        base=1
        while tmp:
            last=tmp%10
            tmp=tmp/10
            res+=tmp*base
            if last==1:
                res+=n%base+1
            elif last>1:
                res+=base
            base*=10
        return res
    
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        flist = range(1,n+1)
        f = str(flist)
        count = 0
        for i in f:
            if i =='1' :
                count += 1
        return count
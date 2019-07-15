# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum < 3:
            return []
        small = 1  #窗口左指针
        big = 2  #窗口右指针
        middle = (tsum + 1)>>1  #目标和+1的中位数
        curSum = small + big
        output = []
        while small < middle:
            if curSum == tsum:
                output.append(range(small, big+1))
                big += 1
                curSum += big
            elif curSum > tsum:
                curSum -= small
                small += 1
            else:
                big += 1
                curSum += big
        return output
    
class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum < 3:
            return []
         
        res = []
        small = 1
        big = 2
        mid = (1 + tsum) / 2
        curSum = small + big
         
        while small < mid:
            if curSum == tsum:
                res.append(range(small, big + 1))
                curSum -= small
                small += 1
            elif curSum < tsum:
                big += 1
                curSum += big
            else:
                curSum -= small
                small += 1
         
        return res
    
class Solution:

    def FindContinuousSequence(self, tsum):
        # write code here
        rlist = []
        if tsum < 3:
            return []
        for i in range(1, tsum):
            n = (1 - 2*i + ((2*i -1)**2+8*tsum)**0.5)/2
            if n % 1 == 0 and 1< n <= tsum:
                curlist = range(i,i+int(n))
                rlist.append(curlist)

        return rlist
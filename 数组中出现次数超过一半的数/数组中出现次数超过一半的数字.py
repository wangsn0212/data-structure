# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import collections
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        tmp = collections.Counter(numbers)
        x = len(numbers)/2
        for k, v in tmp.items():
            if v > x:
                return k
        return 0
    
    
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        numberset = set(numbers)
        printdata = 0
        for data in numberset:
            count = 0
            for num in numbers:
                if data == num:
                    count = count + 1
            if count > len(numbers)/2:
                printdata = data
        return printdata
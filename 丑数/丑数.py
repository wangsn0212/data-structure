# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        if (index <= 0):
            return 0
        uglyList = [1]
        indexTwo = 0
        indexThree = 0
        indexFive = 0
        for i in range(index-1):
            newUgly = min(uglyList[indexTwo]*2, uglyList[indexThree]*3, uglyList[indexFive]*5)
            uglyList.append(newUgly)
            if (newUgly % 2 == 0):
                indexTwo += 1
            if (newUgly % 3 == 0):
                indexThree += 1
            if (newUgly % 5 == 0):
                indexFive += 1
        return uglyList[-1]
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding:utf-8 -*-
from collections import Counter
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        return list(self.dc(array, 0, len(array)-1))
         
    def dc(self, array, start, end):
        res = set()
        if start > end:
            return res
        if start == end:
            return set(array[start:end+1])
         
        spl = (start+end)/2
         
        s1 = self.dc(array, start, spl)
        s2 = self.dc(array, spl+1, end)
         
        return s1.union(s2).difference(s1.intersection(s2))
    
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        a=[]
        mydic = {}
        if not array:
            return array
        for data in array:
            mydic[data] = array.count(data)
        for key, val in mydic.items():
            if val is 1: 
                a.append(key)
        return a
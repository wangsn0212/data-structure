# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 21:26:19 2019

@author: PPLoveXueer
"""

# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        for i in s:
            c = s.count(i)
            if c == 1:
                return s.index(i)
        return -1

class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        ls=[0]*256
        #遍历字符串,下标为ASCII值,值为次数
        for i in s:
            ls[ord(i)]+=1
        #遍历列表,找到出现次数为1的字符并输出位置
        for j in s:
            if ls[ord(j)]==1:
                return s.index(j)
                break
        return -1
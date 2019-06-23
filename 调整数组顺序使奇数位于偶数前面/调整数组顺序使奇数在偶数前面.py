# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding:utf-8 -*-
from collections import deque
class Solution:
    def reOrderArray(self, array):
        # write code here
        odd = deque()
        x = len(array)
        for i in range(x):
            if array[x-i-1]%2 != 0:
                odd.appendleft(array[x-i-1])
            if array[i]%2 == 0:
                odd.append(array[i])
        return list(odd)
    
    
class Solution:
    def reOrderArray(self, array):
        # write code here
        
        odd = []
        even = []
        for data in array:
            if data % 2 == 0 :
                even.append(data)
            if data % 2 != 0:
                odd.append(data)
        odd.extend(even)
        return odd
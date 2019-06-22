# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        pre = -7e20
        for num in rotateArray:
            if num < pre :
                return num
            pre = num
             
        if len(rotateArray) == 0:
            return 0
        return rotateArray[0]
    
    
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        rotatelist = []
        for i in rotateArray:
            rotatelist.append(i)    #数组变为list()
        if len(rotatelist) == 0:
            return 0
        rotatelist.sort()          #sort()从小到大排列， sort(reverse = True) 从打到小排列
        return rotatelist[0]
    
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        contrast = rotateArray[0]
        for data in rotateArray:
            if data < contrast:
                contrast = data
            
        return contrast
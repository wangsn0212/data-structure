# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        max_sum, cur_sum = -0xffffff, 0
        for i in array:
            if cur_sum <= 0:  #此前为负值，则加上任何一数，都比当前值要小
                cur_sum = i
            else:
                cur_sum += i
            if cur_sum > max_sum:
                max_sum = cur_sum
        return max_sum
    
    
# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return None
        sumlist = []
        for i in range(len(array)):
            for j in range(i+1,len(array)+1):
                a = sum(array[i:j])
                sumlist.append(a)
        return max(sumlist)
    

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        n = len(array)
        dp = [ i for i in array]
        for i in range(1,n):
            dp[i] = max(dp[i-1]+array[i],array[i])
         
        return max(dp)

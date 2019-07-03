# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if tinput is None:
            return
        n = len(tinput)
        if n < k:
            return []
        tinput = sorted(tinput)
        return tinput[:k]
    
    
# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput:
            return []
        if k <= len(tinput):
            tinput.sort()
            return tinput[:k]
        else:
            return []
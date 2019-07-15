# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        l=s.split(' ')
        return ' '.join(l[::-1])
    
    # -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        res = s[::-1]
        ress = []
        word = res.split(' ')
        for data in word:
            ress.append(data[::-1])
        return ' '.join(ress)
    
    
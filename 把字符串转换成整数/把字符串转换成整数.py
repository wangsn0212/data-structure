# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        try:
            return int(s)
        except Exception as e:
            return 0
        
# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        es=[]
        # write code here
        org =['+','-','0','1','2','3','4','5','6','7','8','9']
        lg =len(s)
        if not s:
            return 0
        for i in range(lg):
            if s[i] not in org:
                return 0
            else:
                es.append(org.index(s[i])-2)
        sum = 0    
        
        if s[0] is '+':
            for i in range(1,lg):
                sum = sum + es[i]*(10**(lg-1-i))
            return sum
            
            
        if s[0] is '-':
            for i in range(1,lg):
                sum = sum - es[i]*(10**(lg-1-i))
            return sum
        for i in range(0,lg):
            sum = sum + es[i]*(10**(lg-i-1))
        return sum
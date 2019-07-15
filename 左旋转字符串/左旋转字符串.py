# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding:utf-8 -*-
class Solution:
 
    def reverse(self, s):
        if not s:
            return ""
 
        length = len(s)
        if length <= 0:
            return ""
 
        s = list(s)
        #print s
        start = 0
        end = length - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        #print 'after', s
        return ''.join(s)
     
 
    def LeftRotateString(self, s, n):
        # write code here
        if not s:
            return ""
        length = len(s)
        if length <= 0:
            return ""
        if n > length:
            n = n % length
 
        s = self.reverse(s)
 
        first = ""
        second = ""
        for i in range(length - n):
            first += s[i]
        first = self.reverse(first)
        for i in range(length - n, length, 1):
            second += s[i]
        second = self.reverse(second)
        return first + second
    
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
       
        return s[n:]+s[0:n]
    
    
    
        return (s[:n][::-1]+s[n::][::-1])[::-1]
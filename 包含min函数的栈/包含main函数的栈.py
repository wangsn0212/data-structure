# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []  #数据入栈
        self.min_stack = []    #最小辅助栈
        
    def push(self, node):     #压入
        # write code here
        self.stack.append(node)        #正常数据压入
        if not self.min_stack or node <= self.min_stack[-1]:      #如果最小辅助栈没有值，或压入值小于等于当前最小值
            self.min_stack.append(node)          #则最小辅助栈压入该值
            
    def pop(self):
        # write code here
        if self.stack[-1] == self.min_stack[-1]: #如果正常栈需要弹出的值等于最小栈的最新最小值，则最小值栈也弹出该值
            self.min_stack.pop()
        self.stack.pop()        #正常数据弹出
        
    def top(self):       #取出最新压入的值
        # write code here
        return self.stack[-1]
    
    def min(self):
        # write code here
        return self.min_stack[-1]     #最小辅助栈的最新值即为正常数栈的最小值
    
    
class Solution:
    def __init__(self):
        self.stack = []
        self.assist = []
         
    def push(self, node):
        min = self.min()
        if not min or node < min:
            self.assist.append(node)
        else:
            self.assist.append(min)
        self.stack.append(node)
         
    def pop(self):
        if self.stack:
            self.assist.pop()
            return self.stack.pop()
     
    def top(self):
        # write code here
        if self.stack:
            return self.stack[-1]
         
    def min(self):
        # write code here
        if self.assist:
            return self.assist[-1]
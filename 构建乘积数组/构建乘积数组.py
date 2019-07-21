# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        if not A:
            return []
        # 计算前面一部分
        num = len(A)
        B = [None] * num
        B[0] = 1
        for i in range(1, num):
            B[i] = B[i-1] * A[i-1]
        # 计算后面一部分
        # 自下而上
        # 保留上次的计算结果乘本轮新的数,因为只是后半部分进行累加，所以设置一个tmp,能够保留上次结果
        tmp = 1
        for i in range(num-2, -1, -1):
            tmp *= A[i+1]   
            B[i] *= tmp
        return B
    
# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        if A is None:
            return False
        B = []
        cum = 1
        j =0
        for i in range(len(A)):
            cum = 1
            j = 0
            while j < len(A):
                if j == i :
                    j += 1
                else:
                    cum = cum*A[j]
                    j += 1
            B.append(cum)
        return B
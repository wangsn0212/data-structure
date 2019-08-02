# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 17:23:07 2019

@author: PPLoveXueer
"""

def Cnm(a, b):
    ans =1
    for i in range(a+1, a + b +1):
        ans *=i
    for i in range(1, b +1):
        ans //=i
    return ans
 
n, m, k =map(int, input().strip().split())
if Cnm(n, m) < k:
    print(-1)
else:
    ans =""
    while n > 0 and m > 0:
        temp =Cnm(n -1, m)
        if temp <k:
            k-=temp
            ans +="z"
            m -=1
        else:
            ans +="a"
            n -=1
    ans +="a"*n
    ans +="z"*m
    print(ans)
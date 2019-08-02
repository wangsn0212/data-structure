# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 16:25:38 2019

@author: PPLoveXueer
"""

lis = list(map(int, input().split()))
a = max(lis)
lis.remove(a)
if lis[0] + lis[1] > lis[0]*lis[1]:
    print(a*(lis[0] + lis[1]))
else:
    print(a*(lis[0] * lis[1]))
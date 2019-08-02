# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 19:51:07 2019

@author: PPLoveXueer
"""


n = int(input())
ns = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))
 
for i in range(1, n):
    ns[i] += ns[i-1]

for i in q:
    l, r =0, n-1
    while l < r:
        mid = (l +r) >> 1
        if ns[mid] < i:
            l = mid + 1
        else:
            r = mid
    print(r + 1)
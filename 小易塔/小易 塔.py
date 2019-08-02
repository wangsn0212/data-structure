# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 16:44:54 2019

@author: PPLoveXueer
"""

n, k = map(int, input().split())
a = list(map(int, input().split()))
 
res_list = []
for i in range(k):
    max_index = a.index(max(a))
    min_index = a.index(min(a))

    res_list.append([max_index+1, min_index+1])

    a[max_index] -= 1
    a[min_index] += 1

    if max(a) - min(a) < 2:
        break

print("%d %d" % (max(a)-min(a), len(res_list)))

for i in range(len(res_list)):
    print("%d %d" % (res_list[i][0], res_list[i][1]))
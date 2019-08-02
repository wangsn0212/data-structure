# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
小易觉得高数课太无聊了，决定睡觉。不过他对课上的一些内容挺感兴趣，所以希望你在老师讲到有趣的部分的时候叫醒他一下。你知道了小易对一堂课每分钟知识点的感兴趣程度，并以分数量化，以及他在这堂课上每分钟是否会睡着，你可以叫醒他一次，这会使得他在接下来的k分钟内保持清醒。你需要选择一种方案最大化小易这堂课听到的知识点分值。
'''
n,k = [int(x) for x in input().strip().split()]
scores = [int(x) for x in input().strip().split()]
wakes = [int(x) for x in input().strip().split()]

if n <= k:
    print(sum(scores))
else:
    maxscore = 0
    sums = 0
    for i in range(n):
        if wakes[i] == 1:
            sums += scores[i]
            scores[i] = 0
    i = 0
    j = 0
    while j < k:
        if wakes[j] == 0:
            sums += scores[j]
        j += 1
    maxscore = max(maxscore,sums)
    for i in range(n-k):
        sums -= scores[i]
        sums += scores[j]
        j += 1
        maxscore = max(maxscore,sums)
    print(maxscore)

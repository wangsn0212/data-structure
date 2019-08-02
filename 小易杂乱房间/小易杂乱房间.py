# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 16:12:57 2019

@author: PPLoveXueer
"""

import sys
 
def rot90(a, b, x, y):
    return [y - b + x, a - x + y]
 
def dis(point1, point2):
    return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
 
def is_square(clutter, i, j, k, t):
    point1, point2, point3, point4 = clutter[0][i], clutter[1][j], clutter[2][k], clutter[3][t]
    q = [dis(point1, point2), dis(point1, point3), dis(point1, point4), dis(point2, point3), dis(point2, point4),
         dis(point3, point4)]
    q.sort()
    if q[0] > 0 and q[0] == q[1] == q[2] == q[3] == q[4] / 2 == q[5] / 2:
        return True
    return False
 
if __name__ == "__main__":
    # sys.stdin = open('input.txt', 'r')
    n = int(input().strip())
    for _ in range(n):
        clutter = []
        for _ in range(4):
            a, b, x, y = list(map(int, input().strip().split()))
            tmp = [[a, b]]
            for _ in range(3):
                tmp.append(rot90(tmp[-1][0], tmp[-1][1], x, y))
            clutter.append(tmp)
        ans = 100
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for t in range(4):
                        if is_square(clutter, i, j, k, t):
                            ans = min(ans, i + j + k + t)
        if ans > 3 * 4:
            ans = -1
        print(ans)
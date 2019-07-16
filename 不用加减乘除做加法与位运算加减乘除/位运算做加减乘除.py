# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 22:30:16 2019

@author: PPLoveXueer
"""

def add(a, b):  # 递归
    if b==0:
        return a
    sum = a ^ b  # 异或得到两数之和
    carry = (a & b) << 1  # 与得到进位，左移后与sum相加
    return add(sum, carry)

def add(a, b):  # 非递归
    sum = 0
    carry = 0
    while b:
        sum = a ^ b
        carry = (a & b) << 1
        a = sum
        b = carry
    return a


#减法
def sub(a, b):
    return add(a, add(~b,1))

#乘法
def mul(a, b):
    flag = True if (a^b)>=0 else False  # 同号时flag为True
    if a<0:
        a = add(~a, 1)
    if b<0:
        b = add(~b, 1)
    res = 0
    while b:
        if b&1: 
            res = add(res, a)
        a <<= 1
        b >>= 1
    return res if flag else add(~res,1)

#除法
def div(a, b):
    flag = True if (a^b)>=0 else False  # 同号时flag为True
    if a<0:
        a = add(~a, 1)
    if b<0:
        b = add(~b, 1)
    res = 0
    for i in range(31, -1, -1):
        if (a>>i)>=b:
            res = add(res, 1<<i)
            a = sub(a, b<<i)
    return res if flag else add(~res,1)

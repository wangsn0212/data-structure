# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        if len(ss) <=0:
            return []
        res = list()
        self.perm(ss,res,'')
        uniq = list(set(res))
        return sorted(uniq)
    def perm(self,ss,res,path):
        if ss=='':
            res.append(path)
        else:
            for i in range(len(ss)):
                self.perm(ss[:i]+ss[i+1:],res,path+ss[i])
                
                
# -*- coding:utf-8 -*-

class Solution:
    def Permutation(self, ss):
        res = []
        for i in ss:
            res.append(i)
        res.sort()
        list = []
        if len(res) <= 1:
            return res
        for i in range(len(res)):
            for j in map(lambda x: res[i]+x, self.Permutation(res[:i]+res[i+1:])):  #生成每个排好序的字符串（lambda补全每个循环中返回字符串的头部）
                if j not in list:   #这里的判断可以消除重复值的影响
                    list.append(j)
        return list
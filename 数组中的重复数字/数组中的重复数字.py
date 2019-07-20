# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding:utf-8 -*-
import collections
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        flag=False
        c=collections.Counter(numbers)
        for k,v in c.items():
            if v>1:
                duplication[0]=k
                flag=True
                break
        return flag
    
    
# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if numbers is None :
            return False
        condi = {}
        count = 0
        for data in numbers:
            condi[data] = numbers.count(data)
        for key, val in condi.items():
            if val > 1 :
                duplication[0] = key
                return True 
            else :
                count +=1
        if count == len(numbers):
            return False
        
radiansdict.clear()    #删除字典内所有元素
radiansdict.copy()    #返回一个字典的浅复制
radiansdict.fromkeys()    #创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
radiansdict.get(key, default=None)    #返回指定键的值，如果值不在字典中返回default值
radiansdict.has_key(key)    #如果键在字典dict里返回true，否则返回false
radiansdict.items()    #以列表返回可遍历的(键, 值) 元组数组
radiansdict.keys()    #以列表返回一个字典所有的键
radiansdict.setdefault(key, default=None)    #和get()类似, 但如果键不已经存在于字典中，将会添加键并将值设为default
radiansdict.update(dict2)    #把字典dict2的键/值对更新到dict里
radiansdict.values()    #以列表返回字典中的所有值
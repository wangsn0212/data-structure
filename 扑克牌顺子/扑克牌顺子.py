# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding:utf-8 -*-
import collections
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False
        c = collections.Counter(numbers)
        m = c[0]
        new_list = [i for i in numbers if i > 0]
        new_list.sort()
        n = 0
        for j in range(len(new_list)-1):
            if (new_list[j+1] - new_list[j]) > 0:
                n += (new_list[j+1] - new_list[j])
            else:
                return False
        if n <= 4:
            return True
        else:
            return False
        
        
        
# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        numbers.sort()
        zero = numbers.count(0)
        for data in numbers[:2]:
            if data == 0:
                numbers.remove(0)
        dif = []
        for i in range(len(numbers)-1):
            dif.append(numbers[i+1] - numbers[i])
        diff = set(dif)
        two = dif.count(2)
        if diff == {1}:
            return True
        if zero == 1 and diff == {1,2} and two == 1:
            return True
        if zero == 2 and (diff == {1,2} or diff == {2}):
            return True
        if zero == 3 and 1 < max(diff) < 5:
            return True
        if zero ==4:
            return True
        
        return False



def IsContinuous(self, numbers):
 
    if not numbers:return False
    numbers.sort()
    zeroNum = numbers.count(0)
    for i, v in enumerate(numbers[:-1]):
        if v != 0:
            if numbers[i+1]==v:return False
            zeroNum = zeroNum - (numbers[i + 1] - v) + 1
            if zeroNum < 0:
                return False
    return True            
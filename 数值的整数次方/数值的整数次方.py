# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        flag = 0
        if base == 0:
            return False
        if exponent == 0:
            return 1
        if exponent < 0:
            flag = 1
        result = 1
        for i in range(abs(exponent)):
            result *= base
        if flag == 1:
            result = 1 / result
        return result
    
class Solution:
    def Power(self, base, exponent):
        # write code here
        return pow(base, exponent)
    
# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0:
            return 0
        if exponent ==0:
            return 1
        result = 1
        if exponent < 0:
            for i in range(-exponent):
                result = result * (1/base)
            return result
        if exponent > 0:
            for i in range(exponent):
                result = result * base
            return result
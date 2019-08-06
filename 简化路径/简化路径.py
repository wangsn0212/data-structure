# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 10:15:45 2019

@author: PPLoveXueer
"""

# =============================================================================
# ## 任务 ##
# 以 Unix 风格给出一个文件的绝对路径，你需要简化它。或者换句话说，将其转换为规范路径。
# 
# 在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..） 表示将目录切换到上一级（指向父目录）；两者都可以是复杂相对路径的组成部分。更多信息请参阅：Linux / Unix中的绝对路径 vs 相对路径
# 
# 请注意，返回的规范路径必须始终以斜杠 / 开头，并且两个目录名之间必须只有一个斜杠 /。最后一个目录名（如果存在）不能以 / 结尾。此外，规范路径必须是表示绝对路径的最短字符串。
# 
#  
# 
#     示例 1：
#     
#     输入："/home/"
#     输出："/home"
#     解释：注意，最后一个目录名后面没有斜杠。
# 
# 
# ##关键思路 ##
# 
#     result =['','' ]存储结果，考虑最后可能没有路径，返回/，所以提前预设两个空值，保证 '/'.join(result) 起码返回一个 /  
#     路径按/分割 （split()） 
#     先判断元素是否为 .. ,是的话result.pop(), 如果pop()为'' ，则需要重新加回来，为起始就是..情况。
# 
# 
# ##关键函数 ##
# Python **replace()** 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。  
# 
# ！原字符串不修改，返回值为修改
# 
#     str.replace(old, new[, max])  
# 
# old -- 将被替换的子字符串。  
# new -- 新字符串，用于替换old子字符串。  
# max -- 可选字符串, 替换不超过 max 次  
# 
# **实例**
# 
#  
#     str = "this is string example....wow!!! this is really string";
#     print str.replace("is", "was");
#     print str.replace("is", "was", 3);
#     以上实例输出结果如下：
#     
#     thwas was string example....wow!!! thwas was really string
#     thwas was string example....wow!!! thwas is really string
# =============================================================================

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        pathli = path.split('/')  #路径以反斜杠分割，重复的/变为一个，会返回空值
        result =['','']
        for pathstr in pathli :
            if pathstr == '..':
                a = result.pop()
                if a == '':               #针对初始..情况
                    result.append(a)      #保证result 至少有2个值，可以凭借
                continue         #不跳出，会继续执行把..添加到结果
             
            if pathstr != '' and pathstr != '.':
                result.append(pathstr)
        
        re = '/'.join(result)
        while re.count('//')!=0:
            re = re.replace('//','/')
        return re
                

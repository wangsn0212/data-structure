# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 14:34:12 2019

@author: PPLoveXueer
"""
# =============================================================================
# 
# ## 任务 ##
# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
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
# **思路一**:   
# 用 O(m+n)额外空间
# 
# 两遍扫matrix,第一遍用集合记录哪些行,哪些列有0;第二遍置0
# 
# **思路二**:   
# 用O(1)空间
# 
# 关键思想: 用matrix第一行和第一列记录该行该列是否有0,作为标志位
# 
# 但是对于第一行,和第一列要设置一个标志位,为了防止自己这一行(一列)也有0的情况.注释写在代码里,直接看代码很好理解!
# 
# 
# 
# 
# ##关键函数 ##
# **原地算法：**  
# 原地算法不依赖额外的资源或者依赖少数的额外资源，仅依靠输出来覆盖输入的一种算法操作。  
# 原地算法包含使用O(1)空间复杂度的所有算法。
# 
# 如： 原地反转，不借助另外list填充  
# 
#     def reverse(a):
#     """
#     	:param a: list
#     	:return: list
#     	"""
#     	n = len(a)-1
#     	tmp = list()
#     	for i in range(int(n/2)):
#     	tmp = a[i]
#     	a[i] = a[n-i]
#     	a[n-i] = tmp
#     	print(a)
#    		return a
# =============================================================================

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        row0_flag = False
        col0_flag = False
        # 找第一行是否有0
        for j in range(col):
            if matrix[0][j] == 0:
                row0_flag = True
                break
        # 第一列是否有0
        for i in range(row):
            if matrix[i][0] == 0:
                col0_flag = True
                break

        # 把第一行或者第一列作为 标志位
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        #print(matrix)
        # 置0
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row0_flag:
            for j in range(col):
                matrix[0][j] = 0
        if col0_flag:
            for i in range(row):
                matrix[i][0] = 0


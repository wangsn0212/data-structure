# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding:utf-8 -*-
# =============================================================================
#         :param matrix:字符矩阵
#         :param rows:矩阵的行数
#         :param cols:矩阵的列数
#         :param path:需要寻找的路径
# =============================================================================
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        for i in range(rows):
            for j in range(cols):
                if matrix[i*cols+j] == path[0]:
                    if self.find(list(matrix),rows,cols,path[1:],i,j):
                        return True
        return False
    def find(self,matrix,rows,cols,path,i,j):
        if not path:
            return True
        matrix[i*cols+j]='0'
        if j+1<cols and matrix[i*cols+j+1]==path[0]:
            return self.find(matrix,rows,cols,path[1:],i,j+1)
        elif j-1>=0 and matrix[i*cols+j-1]==path[0]:
            return self.find(matrix,rows,cols,path[1:],i,j-1)
        elif i+1<rows and matrix[(i+1)*cols+j]==path[0]:
            return self.find(matrix,rows,cols,path[1:],i+1,j)
        elif i-1>=0 and matrix[(i-1)*cols+j]==path[0]:
            return self.find(matrix,rows,cols,path[1:],i-1,j)
        else:
            return False  
        



# -*- coding:utf-8 -*-
#回溯法
#遍历矩阵中的每一个位置
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix:
            return False
        if not path:
            return True
        x = [list(matrix[cols*i:cols*i+cols]) for i in range(rows)]
        for i in range(rows):
            for j in range(cols):       #路径第一个值的遍历
                if self.exist_helper(x, i, j, path):   
                    return True
        return False
    def exist_helper(self, matrix, i, j, p):
        if matrix[i][j] == p[0]:
            if not p[1:]:
                return True
            matrix[i][j] = '' #不可重叠
            if i > 0 and self.exist_helper(matrix, i-1, j, p[1:]):
                return True
            if i < len(matrix)-1 and self.exist_helper(matrix, i+1, j ,p[1:]):
                return True
            if j > 0 and self.exist_helper(matrix, i, j-1, p[1:]):
                return True
            if j < len(matrix[0])-1 and self.exist_helper(matrix, i, j+1, p[1:]):
                return True
            matrix[i][j] = p[0] ##都不符合的话说明选错了起始点要变回
            return False
        else:
            return False

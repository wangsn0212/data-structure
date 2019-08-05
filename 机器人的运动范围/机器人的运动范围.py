# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
"""
# -*- coding:utf-8 -*-
class Solution:

#数字转化为list  map(int,list(str(data)))
# 0 矩阵： [[0 for _ in range(cols)] for _ in range(rows)]


    def movingCount(self, threshold, rows, cols):
        # write code here
        board=[[0 for i in range(cols)]for j in range(rows)]    #全0矩阵
        global acc
        acc=0  #计数
        def jurge(r,c):    #判断是否满足条件
            s=sum(map(int,str(r)+str(c)))
            return s>threshold
         #不满足，返回True  (1)  ,满足返回 False  (0)
            
        def traverse(r,c):
            global acc
            if not (0<=r<rows and 0<=c<cols):     # 越界 无返回
                return
            if board[r][c]!=0:                    # 已标记过 无返回
                return
            if board[r][c]==-1 or jurge(r,c):     # 不满足，对应值记为-1 无返回
                board[r][c]=-1     
                return
            board[r][c]=1                         #满足的点记录1
            acc+=1                                #并计数加一
            traverse(r+1,c)
            traverse(r-1,c)
            traverse(r,c+1)
            traverse(r,c-1)
             
        traverse(0,0)
        return acc
    
class Solution:

    
    def movingCount(self, threshold, rows, cols):
        # write code here
        if rows == 0 or cols == 0:
            return None
        maxti = [[0 for m in range(cols)] for n in range(rows)]
        count = 0
        for i in range(rows):
            for j in range(cols):
                maxti[i][j] = self.juge(threshold, i,j)
        for i in range(rows):
            for j in range(cols):
                if maxti[i][j] == 1 :
                    if (excit(i-1,j,maxti) ==1) or (excit(i+1,j,maxti) ==1) or (excit(i,j+1,maxti) ==1) or (excit(i,j-1,maxti) ==1):
                        count = count +1
        return count
    
    def juge(self, threshold, rows, cols):
        sum = sum(map(int,str(rows) + str(cols)))
        if sum > threshold:
            return 0
        else:
            return 1
        
    def excit(self, rows, cols, maxti):
        try:
            maxti[rows][cols]
            return maxti[rows][cols]
        except:
            return 0
      
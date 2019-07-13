# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot == None:
            return True
        if abs(self.TreeDepth(pRoot.left)-self.TreeDepth(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
       
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot == None:
            return 0
        nLeft = self.TreeDepth(pRoot.left)
        nRight = self.TreeDepth(pRoot.right)
        return max(nLeft+1,nRight+1)#(nLeft+1 if nLeft > nRight else nRight +1)
    
    
    
自下向上

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, p):
        return self.dfs(p) != -1       # 存有不满足情况
    def dfs(self, p):
        if p is None:
            return 0
        left = self.dfs(p.left)
        if left == -1:   #左右子树有一个不满足，直接返回不满足
            return -1
        right = self.dfs(p.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1   #左右子树差距>1，不满足要求
        return max(left, right) + 1   #左右子树都满足
    '''下往上，dfs(None) = 0,
    dfs(None的上一层)=1；dfs(None的上二层)=2；以此类推，直到左右节点值相差大于1，变成-1，输出False
    '''
自上向下


class Solution:
    def IsBalanced_Solution(self, p):
        if p is None:
            return True
        left = self.depth(p.left)
        right = self.depth(p.right)
        return abs(left - right) <=1 and self.IsBalanced_Solution(p.left) and self.IsBalanced_Solution(p.right)
    def depth(self, p):
        if p is None:
            return 0
        return 1 + max(self.depth(p.left), self.depth(p.right))
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if sequence==None or len(sequence)==0:
            return False
        length=len(sequence)
        root=sequence[length-1]
        # 在二叉搜索 树中 左子树节点小于根节点
        for i in range(length):
            if sequence[i]>root:
                break
        # 二叉搜索树中右子树的节点都大于根节点
        for j  in range(i,length):
            if sequence[j]<root:
                return False
        # 判断左子树是否为二叉树
        left = True      #左树可以为空树
        if  i>0:
            left = self.VerifySquenceOfBST(sequence[0:i])
        # 判断 右子树是否为二叉树
        right = True         #右树可以为空树
        if i < length-1:
            right = self.VerifySquenceOfBST(sequence[i:-1])
        return left and right
    
  
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        node = sequence[-1]              #找根节点
        for i in range(len(sequence)):   #找左树右树分割点[0,i],[i,-1]
            if sequence[i] > node:
                break
        for data in sequence[i:-1]:
            if data < node:
                return False
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[0:i])
        right = True
        if i < len(sequence)-1:
            right = self.VerifySquenceOfBST(sequence[i:-1])
        return left and right
        

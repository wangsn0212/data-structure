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
    def PrintFromTopToBottom(self, root):
        if  not root:
            return []
        # write code here
        ls=[root]
        result=[]
        while len(ls)>0:
            node=ls.pop(0)
            result.append(node.val)
            if node.left!=None:
                ls.append(node.left)
            if node.right!=None:
                ls.append(node.right)
        return result
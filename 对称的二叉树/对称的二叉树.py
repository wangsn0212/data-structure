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
    def isSymmetrical(self, pRoot):
        # write code here
        def is_same(p1,p2):
            if not p1 and not p2:
                return True
            if (p1 and p2) and p1.val==p2.val:
                return is_same(p1.left,p2.right) and is_same(p1.right,p2.left)
            return False
        if not pRoot:
            return True
        if pRoot.left and not pRoot.right:
            return False
        if not pRoot.left and pRoot.right:
            return False
        return is_same(pRoot.left,pRoot.right)
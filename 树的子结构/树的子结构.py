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
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        return self.is_subtree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
     
    def is_subtree(self, A, B):
        if not B:
            return True
        if not A or A.val != B.val:
            return False
        return self.is_subtree(A.left,B.left) and self.is_subtree(A.right, B.right)
    
    


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):               #确定主树A里是否有B的相同点
        # write code here
        result = False
        if  pRoot1 and  pRoot2:
            if pRoot1.val==pRoot2.val:      #相同点在根节点
                result = self.DoesTree1HaveTree2(pRoot1,pRoot2)
            if not result:     #相同点在左支
                result = self.HasSubtree(pRoot1.left,pRoot2)
            if not result:     #相同点在右支，如果在左支，not result 为假，不触发，直接return
                result = self.HasSubtree(pRoot1.right,pRoot2)
        return result
     
    def DoesTree1HaveTree2(self,pRoot_A,pRoot_B):      #判断是否具有相同的结构
        if not pRoot_B:                              #考虑到递归时，子树长度可以小于主树
            return True
        if not pRoot_A:                             #考虑到递归时，主树长度肯定要大于等于子树长度
            return False
        if pRoot_A.val != pRoot_B.val:                   #考虑递归时节点值不同，结果不符
            return False
         
        return self.DoesTree1HaveTree2(pRoot_A.left,pRoot_B.left) and self.DoesTree1HaveTree2(pRoot_A.right,pRoot_B.right)
    #递归判断左右节点值是否相等
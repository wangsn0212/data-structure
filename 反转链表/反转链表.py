# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
         
 
        # write code here
        if not pHead or not pHead.next:
            return pHead
          
        last = None
          
        while pHead:
            tmp = pHead.next
            pHead.next = last
            last = pHead
            pHead = tmp
        return last
    
    
    
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        l = []
        if not pHead or not pHead.next:
            return pHead
        else:
            while pHead!= None:
                l.insert(0,pHead.val)
                pHead = pHead.next
            dhead = ListNode(l[0])
            p = dhead
            for i in range(len(l)-1):
                p.next = ListNode(l[i+1])
                p = p.next
            return dhead
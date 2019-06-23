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
            tmp = pHead.next   #指向原序的反转点 phead 的下一点（next）,即反转后的上一点
            pHead.next = last  # 进行反转点 phead 的next 重赋值，即赋值为原序列的上一点
            last = pHead       #反转完成， last 指针移动，从原序列的上一点，转移至当前点
            pHead = tmp        #反转完成， 当前点 指针移动，从原序列的当前点，转移至下一点
        return last            #last 从none开始指
    
    
    
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

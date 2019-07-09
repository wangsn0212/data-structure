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
    def FindFirstCommonNode(self, head1, head2):
        # write code here
        list1 = []
        list2 = []
        node1 = head1
        node2 = head2
        while node1:
            list1.append(node1.val)
            node1 = node1.next
        while node2:
            if node2.val in list1:
                return node2
            else:
                node2 = node2.next
                
                


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return None
         
        stack1 = []
        stack2 = []
         
        while pHead1:
            stack1.append(pHead1)
            pHead1 = pHead1.next
             
        while pHead2:
            stack2.append(pHead2)
            pHead2 = pHead2.next
             
        first = None
        while stack1 and stack2:
            top1 = stack1.pop()
            top2 = stack2.pop()
            if top1 is top2:
                first = top1
            else:
                break
        return first
    


class Solution:
    def FindFirstCommonNode(self, head1, head2):
        if not head1 or not head2:
            return None
 
        p1, p2= head1, head2
        length1 = length2 = 0
 
        while p1:
            length1 += 1
            p1 = p1.next
        while p2:
            length2 += 1
            p2 = p2.next
 
        if length1 > length2:
            while length1 - length2:
                head1 = head1.next
                length1 -= 1
        else:
            while length2 - length1:
                head2 = head2.next
                length2 -= 1
 
        while head1 and head2:
            if head1 is head2:
                return head1
            head1 = head1.next
            head2 = head2.next
 
        return None
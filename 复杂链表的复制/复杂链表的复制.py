# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
         
        head = pHead
        p_head = None
        new_head = None
         
        random_dic = {}
        old_new_dic = {}
         
        while head:
            node = RandomListNode(head.label)
            node.random = head.random  #复制头结点
            old_new_dic[id(head)] = id(node)           #id() 函数用于获取对象的内存地址。
            random_dic[id(node)] = node
            head = head.next
             
            if new_head:
                new_head.next = node
                new_head = new_head.next
            else:
                new_head = node
                p_head = node
                 
        new_head = p_head
        while new_head:
            if new_head.random != None:
                new_head.random = random_dic[old_new_dic[id(new_head.random)]]
            new_head = new_head.next
        return p_head
    
    

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return None
         
        dummy = pHead
         
        # first step, N' to N next
        while dummy:
            dummynext = dummy.next
            copynode = RandomListNode(dummy.label)
            copynode.next = dummynext
            dummy.next = copynode
            dummy = dummynext
         
        dummy = pHead
         
        # second step, random' to random'
        while dummy:
            dummyrandom = dummy.random
            copynode = dummy.next
            if dummyrandom:
                copynode.random = dummyrandom.next
            dummy = copynode.next
         
        # third step, split linked list
        dummy = pHead
        copyHead = pHead.next
        while dummy:
            copyNode = dummy.next
            dummynext = copyNode.next
            dummy.next = dummynext
            if dummynext:
                copyNode.next = dummynext.next
            else:
                copyNode.next = None
            dummy = dummynext
 
        return copyHead
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:14:17 2019

@author: PPLoveXueer
"""

def ysf(m,l):
    global nlist,k,plist
    if nlist == []:　　　　# 全部出列退出递归
        return 0

    if l>=m:　　　　# 将出列人员按顺序编入plist
        plist.append(nlist[m-1])
        ysf(m+k,l)
    else:　　　　# 循环回列表，并将出列人编号移出nlist
        for i in range(len(plist)):
            if plist[i] in nlist:
                nlist.remove(plist[i])
        m = m-l
        ysf(m,len(nlist))

def main(n):
    global nlist,plist,k
    nlist = list(range(n))
    plist = []
    k = int(input())
    ysf(k,len(nlist))
    print(plist)

main(int(input()))


#————————————————————————————————————————————————

class Node():             #使用链表法
	def __init__(self,value,next=None):
		self.value=value
		self.next=next
 
def createLink(n):            #建立循环链表
	if n<=0:
		return False
	if n==1:
		return Node(1)
	else:
		root=Node(1)
		tmp=root
		for i in range(2,n+1):
			tmp.next=Node(i)
			tmp=tmp.next
		tmp.next=root
		return root
 
def showLink(root):
	tmp=root
	while True:
		print(tmp.value)
		tmp=tmp.next
		if tmp==None or tmp==root:
			break
 
def josephus(n,k):
	if k==1:
		print('survive:',n)
		return
	root=createLink(n)
	tmp=root
	while True:
		for i in range(k-2):  #在k值得前1位停止
			tmp=tmp.next
		print('kill:',tmp.next.value)   
		tmp.next=tmp.next.next       #遗弃该k结点
		tmp=tmp.next          #重定指针位置
		if tmp.next==tmp:     #当只有一个结点时，输出幸存节点
			break
	print('survive:',tmp.value)
 
if __name__=='__main__':
	josephus(10,4)
	print('-----------------')
	josephus(10,2)
	print('-----------------')
	josephus(10,1)
	print('-----------------')

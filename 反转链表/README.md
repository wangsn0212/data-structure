## 任务 ##
输入一个链表，反转链表后，输出新链表的表头。
## 关键思路 ##
思路1
>pHead始终指向要反转的结点  
>last 指向反转后的首结点  
>每反转一个结点，把pHead结点的下一个结点指向last, last指向pHead成为反转后首结点, 再把pHead向前移动一个结点直至None结束

思路2 
>所有元素存到list中，再重新赋值

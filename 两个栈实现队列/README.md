## 任务 ##
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。


## 关键思路 ##

> ***栈：*** 后进先出  ，执行  压入弹出端，称为栈顶， 另一端称为栈底。  
>     对于顺序表， 后端插入和删除是O(1)操作，此端为栈顶  
>     对于链接表， 前端插入和删除是o(1)操作，此端为栈顶
>     
        push()  将元素stack加入栈，也常称为  压入  
        pop()   删除最后压入的元素，也称  弹出  
        top()   取得栈里最后压入的元素，  不删除

## 基本操作：  
    class Stack(object):   
      def __init__(self):  
        self.stack=[]   #初始化，映射为list操作
      def isEmpty(self):  
        return self.stack==[]  
      def push(self,item):    #压入
        self.stack.append(item)  
      def pop(self):  #弹出
        if self.isEmpty():  
          raise IndexError,'pop from empty stack'    
        return self.stack.pop()   #返回弹出值
      def peek(self):  
        return self.stack[-1]  
      def size(self):  
        return len(self.stack) 
> ***队列***：先进先出  

        Queue(self)  创建空队列
        enqueue()  将元素stack加入队列，也常称为  入队  
        dequeue()   删除最早加入的元素，也称  出队  
        peek()   查看最早进入的元素，  不删除

## 下列对象的布尔值都是False： ##

NONE;

False(布尔类型)

所有的值为零的数

       0（整型）

       0.0（浮点型）

       0L(长整型)

       0.0+0.0j(复数)

""(空字符串)

[](空列表)

()(空元组)

{}(空字典)

raise 语句 抛出指定异常

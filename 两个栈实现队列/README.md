## 任务 ##
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。


## 关键词 ##

> ## 栈：  
> 后进先出  ，执行  压入弹出端，称为栈顶， 另一端称为栈底。  
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
> ## 队列 ：  
> 先进先出  

        Queue(self)  创建空队列
        enqueue()  将元素stack加入队列，也常称为  入队  
        dequeue()   删除最早加入的元素，也称  出队  
        peek()   查看最早进入的元素，  不删除
## 基本操作 ##


class Squeue():

    def __init__(self, init_len = 8):
        self._len = init_len  #存储区长度
        self._elems = [0]*init_len  #元素存储
        self._head = 0  #表头元素下标
        self._num = 0  #元素个数
    
    def is_empty(self):
        return self._num == 0
    
    def peek(self):
        if self._num  == 0:
            raise QueueUnderflow
        return self._elems[self._head]    #抛出指定异常
    
    def dequeue(self):
        if self._num == 0:
            raise QueueUnderflow
        e = self._elems[self._head]
        self._head = (self._head+1) % self._len
        self._num -= 1
        return e
    
    def enqueue(self, e):
        if self._num == self._len:
            self.__extend()
        self._elems[(self._head + self._num) % self._len] = e
        self._num += 1
        
    def __extend(self):
        old_len = self._len
        self._len *= 2
        new_elems = [0]*self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head+i)%old_len]
        self._elems, self._lead = new_elems, 0


## 关键思路 ##
栈A用来作入队列  

栈B用来出队列，当栈B为空时，栈A全部出栈到栈B,栈B再出栈（即出队列）  

     A.append(node) 压入元素
     A ：1 → 6  
     B ：6 → 1
     弹出 B.pop()即可实现先进先出

pop()默认返回最后值， append（）默认加到最后位
>## 下列对象的布尔值都是False： ##
NONE;  
False(布尔类型)：所有的值为零的数  
       0（整型）

       0.0（浮点型）

       0L(长整型)

       0.0+0.0j(复数)
>""(空字符串)  
>[](空列表)

>()(空元组)

>{}(空字典)

>raise 语句 抛出指定异常

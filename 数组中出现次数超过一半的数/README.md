## 任务 ##
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

## 关键思路 ##
1. set()函数找到元素，一一相比，计数增加，没有则返回 0 
2.  使用库函数计数 collections.Counter, 返回字典

## 关键函数 ##
**set()**
> set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
> 
    >>>x = set('runoob')
    >>> y = set('google')
    >>> x, y
    >(set(['b', 'r', 'u', 'o', 'n']), set(['e', 'o', 'g', 'l']))   # 重复的被删除
    >>> x & y         # 交集
    set(['o'])
    >>> x | y         # 并集
    set(['b', 'e', 'g', 'l', 'o', 'n', 'r', 'u'])
    >>> x - y         # 差集
    set(['r', 'b', 'u', 'n'])

**collections.Counter**

    >import collections
    >colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
    >c = collections.Counter(colors)
    >c
    Counter({'blue': 3, 'green': 1, 'red': 2})  #为字典

**字典(Dictionary) items()方法**  
dict.items()  

     >dict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}  
     >print "字典值 : %s" %  dict.items()
     字典值 : [('Google', 'www.google.com'), ('taobao', 'www.taobao.com'), ('Runoob', 'www.runoob.com')]

     >for key,values in  dict.items():
    		print key,values
     Google www.google.com
     taobao www.taobao.com
     Runoob www.runoob.com


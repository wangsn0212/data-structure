## 任务 ##
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。


##关键词##
**字典（key,val）**  
定义：mydic = {}  
添加元素： mydict['data'] = 1  

           > mydict{data:1}

输出键为2的值 ：print mydict[2]  
输出所有键： print mydict.keys()  
输出所有值：print mydict.values()  
输出值为2的键：

     for key, val in mydict.items():
    	if val == 2:
        	print(key)

del mydict['a'] #删除key为a的键值对   
mydict.clear #清除字典c中所有的键值对

字典内置函数和方法
函数或方法	作用
cmp(dict1, dict2)	比较两个字典元素  
len(dict)	字典长度  
str(dict)	输出字典可打印的字符串表示  
type(variable)	输出变量的类型  
dict.clear()	删除字典内所有元素  
dict.copy()	返回字典的一个复制  
dict.fromkeys(seq[, val])	创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值  
dict.get(key, default=None)	返回指定键的值，如果值不在字典中返回default值  
dict.has_key(key)	如果键在字典dict里返回true，否则返回false  
dict.items()	以列表返回可遍历的(键, 值) 元组数组  
dict.keys()	以列表返回一个字典所有的键  
dict.setdefault(key, default=None)	和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default  
dict.update(dict2)	把字典dict2的键/值对更新到dict里  
dict.values()	以列表返回字典中的所有值  
pop(key[,default])	删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。  
popitem()	随机返回并删除字典中的一对键和值。  

**ASCII码**

字符转ASCII 码为：ord(c)
ASCII码转字符 chr(数字)

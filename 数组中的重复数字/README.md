## 任务 ##
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。

##关键思路##
radiansdict.clear()    #删除字典内所有元素  
radiansdict.copy()    #返回一个字典的浅复制  
radiansdict.fromkeys()    #创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值  
radiansdict.get(key, default=None)    #返回指定键的值，如果值不在字典中返回default值  
radiansdict.has_key(key)    #如果键在字典dict里返回true，否则返回false  
radiansdict.items()    #以列表返回可遍历的(键, 值) 元组数组  
radiansdict.keys()    #以列表返回一个字典所有的键  
radiansdict.setdefault(key, default=None)    #和get()类似, 但如果键不已经存在于字典中，将会添加键并将值设为default  
radiansdict.update(dict2)    #把字典dict2的键/值对更新到dict里  
radiansdict.values()    #以列表返回字典中的所有值  

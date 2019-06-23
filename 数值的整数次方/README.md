## 任务 ##
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
## 关键思路 ##
1. base = 0 时，返回 0
2. exponent = 0 时，返回 1
3. 累乘： 
>exponent > 0 返回 result  
         exponent < 0 返回 1/result

## 关键函数 ##

    pow() 方法返回（x的y次方） 的值。 
1、内置的 pow() 方法 
>    pow(x, y[, z]) ,函数是计算x的y次方，  
>    如果z在存在，则再对结果进行取模（余），其结果等效于pow(x,y) %z

2、x**y

3、 abs(x) x的绝对值




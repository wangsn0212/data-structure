## 任务 ##
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

##关键思路##
**1 逻辑与**   

相加为  逻辑或 |   3|4 = 7  




 
**2 逻辑运算符**    
a  and  b，a为False，返回a，a为True，就返回b


    class Solution:
       def Sum_Solution(self, n):
    # write code here
           ans=n
           temp=ans and self.Sum_Solution(n-1)  #正常希望n+(n-1)...叠加，但当n=0时，迭代停止，+0没影响
           ans=ans+temp
           return ans
    

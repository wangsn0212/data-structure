## 任务 ##
输入一棵二叉树，判断该二叉树是否是平衡二叉树。

## 关键思路 ##

1.从下到上  
>     class Solution:  
>     def IsBalanced_Solution(self, p):  
>         return self.dfs(p) != -1       # 存有不满足情况
>     def dfs(self, p):
>         if p is None:
>             return 0
>         left = self.dfs(p.left)
>         if left == -1:   #左右子树有一个不满足，直接返回不满足
>             return -1
>         right = self.dfs(p.right)
>         if right == -1:
>             return -1
>         if abs(left - right) 1:
>             return -1   #左右子树差距>1，不满足要求
>         return max(left, right) + 1   #左右子树都满足
从下往上，dfs(None) = 0,  
 dfs(None的上一层)=1；  dfs(None的上二层)=2；  
以此类推，直到左右节点值相差大于1，变成-1，输出False

             1           则dfs为         -1
            / \                         / \
           2   4                       3   1
          /\                          /\
         5  6                        2  1   
        /                           /
       7                           1                      
    
    

方法2：自顶向下,对于每个节点，都计算一下左子树以及右子树的差的绝对值，即每个节点都判断一下。
算法复杂度为O（N*2）
##关键词##
**平衡树**  
**平衡二叉搜索树**（Self-balancing binary search tree）又被称为AVL树（有别于AVL算法），且具有以下性质：它是一棵**空树**或**它的左右两个子树的高度差的绝对值不超过1**，并且左右两个子树都是一棵平衡二叉树。平衡二叉树的常用实现方法有红黑树、AVL、替罪羊树、Treap、伸展树等。 最小二叉平衡树的节点总数的公式如下 F(n)=F(n-1)+F(n-2)+1 这个类似于一个递归的数列，可以参考Fibonacci(斐波那契)数列，1是根节点，F(n-1)是左子树的节点数量，F(n-2)是右子树的节点数量。

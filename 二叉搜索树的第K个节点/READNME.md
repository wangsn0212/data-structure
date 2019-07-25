## 任务 ##
给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。

## 关键思路 ##
**二叉搜索树**  
二叉查找树，（二叉搜索树，二叉排序树）它或者是一棵空树，或者是具有下列性质的二叉树：   
若它的**左子树不空**，则左子树上所有结点的值均**小于它的根结点的值**；
若它的**右子树不空**，则右子树上所有结点的值**均大于它的根结点的值**；  
它的**左、右子树也分别为二叉排序树。**

故求最小第k节点，进行左中右的遍历即可。  
递归调用  
    
    def middle(self,proot):
        result = []
        if proot == None:
            return None
        if proot.left:
            result.extend( self.middle(proot.left))
        result.append(proot)
        if proot.right:
            result.extend( self.middle(proot.right))
        return result

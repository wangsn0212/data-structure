## 任务 ##
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度

## 关键思路 ##
求树的深度，可以从层次遍历出发考虑  
层次遍历可以使用队列完成，也可以使用递归完成，所以有两种方法




    class Solution:  
    # 层次遍历  
      def levelOrder(self, root):  
>         # write your code here  
>         # 存储最后层次遍历的结果  
>         res = []  
>         # 层数  
>         count = 0  
>         # 如果根节点为空，则返回空列表  
>         if root is None:  
>             return count  
>         # 模拟一个队列储存节点  
>         q = []  
>         # 首先将根节点入队  
>         q.append(root)  
>         # 列表为空时，循环终止  
>         while len(q) != 0:
>             # 使用列表存储同层节点
>             tmp = []
>             # 记录同层节点的个数
>             length = len(q)
>             for i in range(length):
>                 # 将同层节点依次出队
>                 r = q.pop(0)
>                 if r.left is not None:
>                     # 非空左孩子入队
>                     q.append(r.left)
>                 if r.right is not None:
>                     # 非空右孩子入队
>                     q.append(r.right)
>                 tmp.append(r.val)
>             if tmp:
>                 count += 1  # 统计层数
>             res.append(tmp)
>         return count
>  
>     def TreeDepth(self, pRoot):
>         # write code here
>         # 使用层次遍历
>         # 当树为空直接返回0
>         if pRoot is None:
>             return 0
>         count = self.levelOrder(pRoot)
>         return count
 
方法二：使用递归方法
    
    class Solution:  
	    def TreeDepth(self, pRoot):  
        # write code here  
        # 使用层次遍历  
        # 当树为空直接返回0  
        	if pRoot is None:  
            	return 0  
        # 方法2：使用递归  
        # 如果该树只有一个结点，它的深度为1.如果根节点只有左子树没有右子树，  
        # 那么树的深度为左子树的深度加1；同样，如果只有右子树没有左子树，  
        # 那么树的深度为右子树的深度加1。如果既有左子树也有右子树，  
        # 那该树的深度就是左子树和右子树的最大值加1.  
        	count = max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1  
        return count  

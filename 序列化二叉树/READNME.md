## 任务 ##
请实现两个函数，分别用来序列化和反序列化二叉树

## 关键思路 ##
**序列化**就是按照前序遍历的顺序将其输出为一个字符串，节点为空则用#代替，  
**反序列化**就是讲一个字符串恢复成为一个树。    

思路：用什么方法无所谓，关键是输入一棵树，序列化为字符串，然后将字符串反序列化还能还原为原来的那棵树。
> 设结构为   

         D
     L       R
>先根序遍历 为 DLR  ；根节点在首位  
>中根序遍历 为LDR   ；根节点左边为左叉树，右边为右叉树  
>后根序遍历 为LRD   ；根节点在最后位   


序列化：
前序递归遍历：  


    if root is None:   
   		return '#'  
 	result.append(root.val）
 	l = self.函数名（root.left）
 	result.append(l)
 	r = self.函数名（root.right）
	result.append(r)
 	return ','.join(result)

反序列化：及根据序列化result重构二叉树  


    def Deserialize(self, s):
        serialize = s.split(',')  #恢复李彪
        tree, sp = self.deserialize(serialize, 0)
        return tree
 
    def deserialize(self, s, sp):
        if sp >= len(s) or s[sp] == "#":
            return None, sp + 1
        node = TreeNode(int(s[sp]))
        sp += 1
        node.left, sp = self.deserialize(s, sp)
        node.right, sp = self.deserialize(s, sp)
        return node, sp
    

或：
>
	
	def Deserialize(self, s):
        self.flag += 1
        l = s.split(',')
        if (self.flag >= len(s)):
            return None
        root = None
        if (l[self.flag] != '#'):
            root = TreeNode(int(l[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root

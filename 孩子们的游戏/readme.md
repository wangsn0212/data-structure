## 任务 ##
每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,今年亦是如此。HF作为牛客的资深元老,自然也准备了一些小游戏。其中,有个游戏是这样的:首先,让小朋友们围成一个大圈。然后,他随机指定一个数m,让编号为0的小朋友开始报数。每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,从他的下一个小朋友开始,继续0...m-1报数....这样下去....直到剩下最后一个小朋友,可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)

##关键思路##
**1 公式归纳**   

把n个人的编号改为0~n-1，然后对删除的过程进行分析。  
第一个删除的数字是(m-1)%n，几位k，则剩余的编号为(0,1,...,k-1,k+1,...,n-1)，下次开始删除时，顺序为(k+1,...,n-1,0,1,...k-1)。
用f(n,m)表示从(0~n-1)开始删除后的最终结果。  
用q(n-1,m)表示从(k+1,...,n-1,0,1,...k-1)开始删除后的最终结果。
则f(n,m)=q(n-1,m)。  

下面把(k+1,...,n-1,0,1,...k-1)转换为(0~n-2)的形式，即  
k+1对应0  
k+2对于1  
...
k-1对应n-2  
转化函数设为p(x)=(x-k-1)%n, p(x)的你函数为p^(x)=(x+k+1)%n。
则f(n,m)=q(n-1,m)=p^(f(n-1,m))=(f(n-1,m)+k+1)%n，又因为k=(m-1)%n。  
f(n,m)=(f(n-1,m)+m)%n;  

最终的递推关系式为  
f(1,m) = 0;                        (n=1)  
f(n,m)=(f(n-1,m)+m)%n; （n>1）  

**简单讲就是：**  
由于首位从0开始，所以第一个pop的是m-1,设该位为i  
而后，一般按顺序pop,应为在i的基础上+m，然而，由于pop操作，前面少一位，所以为m+i-1  
考虑超出范围，则pop项为 （m+i-1）% len(res)


 
**2 约瑟夫环问题**    
已知n个人（以编号1，2，3...n分别表示）围坐在一张圆桌周围。从编号为k的人开始报数，数到k的那个人被杀掉；他的下一个人又从1开始报数，数到k的那个人又被杀掉；依此规律重复下去，直到圆桌周围的人只剩最后一个。

链表法：  
1. class Node()  
2. 建立循环链表：
  
    def createLink(n): 
        lihead = Node(1)      #头结点
        root = lihead         #定义指针
        for i in range(2,n):
             root.next = Node(i)
             root = root.next
        root.next = lihead    #变成环
3.主体 josephus 函数： 
 
    k = 1 时，print n  
    root=createLink(n)   #建立循环列表
	tmp=root
	while True:
		for i in range(k-2):  #在k值得前1位停止
			tmp=tmp.next
		print('kill:',tmp.next.value)   
		tmp.next=tmp.next.next       #遗弃该k结点
		tmp=tmp.next          #重定指针位置
		if tmp.next==tmp:     #当只有一个结点时，输出幸存节点
			break
	print('survive:',tmp.value)

        





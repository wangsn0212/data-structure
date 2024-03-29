## 任务 ##
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)

## 关键思路（普通） ##
1. 两个指针遍历，一个i指向子序列开始端，一个j指向结尾端  
2. 需要注意的是，由于range以及array[]特性，后一个的指针需要注意为 j in range(i+1,len(array)+1)



## 关键思路（动态规划） ##
dp[i]表示以元素array[i]结尾的最大连续子数组和.  
以[-2,-3,4,-1,-2,1,5,-3]为例  
可以发现,  
dp[0] = -2  
dp[1] = -3  
dp[2] = 4  
dp[3] = 3  
以此类推,会发现  
dp[i] = max{dp[i-1]+array[i],array[i]}.

## 关键思路（同理） ##
一个cur_sum,  一个max_sum
列表遍历  
如果 cur_sum > 0 , cur_sum等于cur_sum + 当前元素值  
> 当前元素值 + 正数，都比当前值要大, 所以最大取 cur_sum + i  

如果 cur_sum <= 0, cur_sum等于当前元素值.   
> 当前元素值 + 负数，都比当前值要小， 所以最大取 i  

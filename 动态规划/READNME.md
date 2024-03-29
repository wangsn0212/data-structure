# 动态规划算法

## 基本原理

动态规划的**三要素**：

-  **最优子结构**：指每个阶段的最优状态可以从之前某个阶段的某个或某些状态直接得到(子问题的最优解能够决定这个问题的最优解)
- **边界**：指问题最小子集的解(初始范围)
- **状态转移函数**：指从一个阶段向另一个阶段过度的具体形式,描述的是两个相邻子问题之间的关系(递推式)

**重叠子问题**，<u>对每个子问题只计算一次,然后将其计算的结果保存到一个表格中,每一次需要上一个子问题解时,进行调用</u>，**只要o(1)时间复杂度**，准确的说，**动态规划是利用空间去换取时间的算法**

判断是否可以利用动态规划求解,第一个是判断是否存在重叠子问题

## 实例分析

### 爬楼梯

```
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/23/c-programming/54/
```

**分析:**
        假定n=10,首先考虑最后一步的情况,要么从第九级台阶再走一级到第十级,要么从第八级台阶走两级到第十级,因而,要想到达第十级台阶,最后一步一定是从第八级或者第九级台阶开始.也就是说已知从地面到第八级台阶一共有X种走法,从地面到第九级台阶一共有Y种走法,那么从地面到第十级台阶一共有X+Y种走法.
**即F(10)=F(9)+F(8)**
     分析到这里,动态规划的三要素出来了：

- **边界：**F(1)=1,F(2)=2
- **最优子结构：**F(10)的最优子结构即F(9)和F(8)
- **状态转移函数：**F(n)=F(n-1)+F(n-2)

**求解:**

```python
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n<=2:
            return n
        a=1　　#边界
        b=2　　#边界
        temp=0
        for i in range(3,n+1):
            temp=a+b　　　　#状态转移
            a=b　　　　　　　　#最优子结构
            b=temp　　　　　　#最优子结构
            #简化 a,b = b,a+b ,return b
        return temp
```

### 矿工挖矿

```
    某一个地区发现了5座金矿,每个金矿的黄金储量不同,需要挖掘的工人也不同,设参加挖掘的总共10人,且每座金矿要么全挖,要么不挖,不能派出一半人挖取一半金矿，试问，想得到最多的黄金，应该选择挖取哪几个金矿。
金矿    黄金储量    工人数
           400            5
           500            5
           200            3
           300            4
           350            3
```

**分析：**

如果要使用动态规划解题，就要确定动态规划的三要素：最优子结构、边界和状态转移函数。

- **最优子结构**
  解题目标：是确定10个工人挖5个金矿能够获得最多的黄金量，该问题可以从10个工人挖4个金矿的子问题中递归求解。
  在解决10个工人挖4个金矿时，存在两种选择，一种是放弃第5个矿，将10个工人投入到挖四个矿中；另一种选择是决定对第5个矿进行挖掘，因此需要从这10个人中抽取3个人（第5个矿需要人数）加入第5个矿开采，剩余的人处理前4个矿。
  因此，最优解应该是这两种选择中获得黄金数量较多的那一种。
  为了描述方便，设**金矿数量为n**，**工人个数为w**，第n个矿的黄金数量为G(n),**挖当前第n个矿所用的工人为P(n)**，要想获得10个矿工挖掘5个金矿的最优解为 max(F(4,10),F(4,10-P[4])+G[4])。
  这就是最优子结构。

- **边界**
  对于一个金矿而言，若当前的矿工数量不能达到金矿的挖掘需要，则获得的黄金数量为0，若能满足矿工数量要求，获得的黄金数量为G[0]。
  因此，边界可以描述为
  n=1,w>=P[0]时，F(n,w)=G[0]
  n=1,w<P[0]时，F(n,w)=0

- **状态转移函数**

  F(n,w) = 0 (n<=1,w<p[0])
  F(n,w) = G[0]  (n==1, w>=P[0])
  F(n,w) = F(n-1,w)(n>1,w<P[n-1])      **(工人数少于挖第n个矿所用的人数)（P序列中的p[n-1]为第n个矿）**
  F(n,w) = max(F(n-1,w), F(n-1, w-P[n-1])+G[n-1])(n>1,w>=P[n-1])

  到这里，三要素找到了，经过这个过程也明白了求解过程，由底向上计算，一步步推导可以得到结果，换句话说，n步的解其实就是第一步的结果推来的，这就是递归过程。

  到这里，三要素找到了，经过这个过程也明白了求解过程，由底向上计算，一步步推导可以得到结果，换句话说，n步的解其实就是第一步的结果推来的，这就是递归过程。

**代码：** 

```python
def gold_mining(n ,w, G, P):
      """
      利用递归实现动态规划算法过程
      :param n:
      :param w:
      :param G:
      :param P:
      :return:
      """
      if n <= 1 and w < P[0]:
          return 0
      if n == 1 and w >= P[0]:
          return G[0]
      if n > 1 and w < P[n-1]:
          return gold_mining(n-1, w, G, P)
      if n > 1 and w >= P[n-1]:
          return max(gold_mining(n-1, w, G, P), gold_mining(n-1, w-P[n-1], G, P) + G[n-1])

  if __name__ == '__main__':
      G = [400, 500, 200, 300, 350]
      P = [5, 5, 3, 4, 3]
      n = 5
      w = 10
      print(gold_mining(n, w, G, P))
```

### 最大子序和

```
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
```

**分析：**

- 首先寻找最优子问题,[-2,1,-3,4,-1,2,1,-5,4],第一个最优子问题为-2,那么到下一个1时,其最优为当前值或者当前值加上上一个最优值,因而可以得到其递推公式
- 状态转移方程

   
$$
dp[i] = max(nums[i], nums[i] + dp[i - 1])
$$


​              i代表数组中的第i个元素的位置，dp[i]代表从0到i闭区间内，所有包含第i个元素的连续子数组中，总和最大的值

**代码：**

nums = [-2,1,-3,4,-1,2,1,-5,4]
dp = [-2, 1, -2, 4, 3, 5, 6, 1, 5]

```python
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
#        判断边界
        if len(nums)==0:
            return 0
#         定义一个表格进行存储上一个子问题的最优解
        d=[]
        d.append(nums[0])    #第一个最优解为第一个元素
        max_=nums[0]      #返回的最大值
        for i in range(1,len(nums)):
            if nums[i]>nums[i]+d[i-1]:
                d.append(nums[i])
            else:
                d.append(nums[i]+d[i-1])
            if max_<d[i]:
                max_=d[i]
        return max_
```

### 打家劫舍

```
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2:

输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
```

**分析与代码：**

- **定义向量dp**
   dp向量长度与输入数组nums相同，dp[i]表示到第下标为i的房屋位置，可以打劫到的最大金额；

- **初始条件**
   （1）当i=0时，打劫到第一家为止最大的打劫金额为这一家的金额，即dp[0]=nums[0]
   （2）当i=1时，由于相邻房屋不能同时打劫，因此打劫到第二家位置的最大打劫金额为前两家中的最大值，即dp[1]=max(nums[0], nums[1])

- **状态转移方程**
   当i>=2时，当前的总金额有两种情况：
   （1）如果打劫下标为i的房间，这样下标为i-1的房间不能打劫，则当前的最大总金额为打劫到i-2房间的金额与下标为i的房间的金额之和；
   （2）不打劫下标为i的房间，则当前的最大金额等于打劫到i-1房间的最大金额；
   取两个选择的最大值，因此有：
   dp[i] = max(dp[i-2] + nums[i], dp[i-1])

```python
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums)==0:
            return 0
        if len(nums)<=2:
            return max(nums)
        dp=[]
        dp.append(nums[0])
        dp.append(max(nums[0],nums[1]))
        for i in range(2,len(nums)):
            dp.append(max(dp[i-1],dp[i-2]+nums[i]))
        return dp[-1]
```

### 买卖股票的最佳时机

```
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
```

**思路**：动态规划，设置一个变量记录买入的最小金额

用一个变量minelement记录下左侧的最小值，

当扫描到第i个元素时，

​                          如果在这一天卖股票，盈利就是dp[i] = prices[i] - minelement

​                         如果在这一天不卖股票，盈利还是dp[i] = dp[i - 1]

**所以 dp[i] = max(dp[i-1], prices[i] - minelement)**

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        profit = 0
        dp = [0]
        minelement = prices[0]
        for i in range(1, len(prices)):
            minelement = min(minelement, prices[i])
            dp.append(max(dp[i - 1], prices[i] - minelement))
            if dp[-1] > profit:
                profit = dp[-1]
        return profit

```

在第二种思路上进一步优化，因为本题只需要返回最后i = n时的最大利润，中间结果是不需要保存的，所以可以不用dp数组记录中间答案，只需保留最大值即可。

### 使用最小花费爬楼梯

```
数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

示例 1:

输入: cost = [10, 15, 20]
输出: 15
解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
 示例 2:

输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出: 6
解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
注意：

cost 的长度将会在 [2, 1000]。
每一个 cost[i] 将会是一个Integer类型，范围为 [0, 999]
```

**思路：** 

​       从楼顶分析，比如说10为楼顶，到达楼顶只有两种方式，一种从第八层走两步到达，一种是从第九层走一步到达，因为该10为楼顶：

10为楼顶：F(10)最有子结构为:  F(9) 和  F(8)

F（10） 递推式： F(10)=min(F(9)+cost[10],F(8)+cost[10])

边界:  F(0)=1  F(1)=100

```python
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """                
        
        if len(cost)<=1:
            return min(cost)
        dp=[]
        dp.append(cost[0])
        dp.append(cost[1])
        for i in range(2,len(cost)+1):   #楼顶不在cost的范围内，因为对遍历+1
            if i==len(cost):            #该层为楼顶，没有取值
                dp.append(min(dp[i-1],dp[i-2])) 
            else:
                dp.append(min(dp[i-1]+cost[i],dp[i-2]+cost[i]))
        return dp[-1]
```

### 比特位计数

```
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:

输入: 2
输出: [0,1,1]
示例 2:

输入: 5
输出: [0,1,1,2,1,2]
进阶:

给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
要求算法的空间复杂度为O(n)。
你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。
```

**分析：**

规律就是，**对于偶数，它和它的一半的数的1是相等的。****对于奇数，它的1的个数比它的一半的1的个数多1**

```python
def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]
        for i in range(1,num+1):
            res.append(res[i>>1]+(i%2))
        return res
```

当数字i为2的指数倍时，其只有一个1，dp[i]=1 if(i==2k)

其余，**递推式 ： dp[i] = 1+dp[i-2** **k]

```python
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # 动态规划问题：当数字i未2的指数倍时，其只有一个1，dp[i]=1 if(i==2**k)
        # 递推试 ： dp[i] = 1+dp[i-2**k]
        res=[0]
        k=0
        for i in range(1,num+1):
            if(i == 2**k):
                res.append(1)
                k+=1
            else:
                res.append(1+res[i-2**k])
        return res
```

### 三角形最小路径和

```
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
```

**分析：**

利用列表进行存储，每一行每个步骤结束后的最小值，那么在最后一行，其最小值为            min（4+dp[0],4+dp[1],1+dp[0],1+dp[1]...）

所以状态转移方程为： 如果i==0 or i==len(triangle[row]) 那么其转移方程为dp[i]=dp[0]triangle[row][i]  dp[i]=dp[i-1]+triangle[row][i]
                            dp[i]=min(dp[i-1],dp[i])+trianglerow[i]
        初始值为   dp[0]=triangle[0][0]

```
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        '''
        dp问题：利用列表进行存储，每一行每个步骤结束后的最小值，那么在最后一行，其最小值为min（4+dp[0],4+dp[1],1+dp[0],1+dp[1]...）
        所以状态转移方程为： 如果i==0 or i==len(triangle[row]) 那么其转移方程为dp[i]=dp[0]triangle[row][i]  dp[i]=dp[i-1]+triangle[row][i]
                            dp[i]=min(dp[i-1],dp[i])+triangle[row][i]
        初始值为   dp[0]=triangle[0][0]
        '''
        if len(triangle)==1:
            return triangle[0][0]
        dp=[[triangle[0][0]]]
        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):
                dp.append([])
#                 边界只有一个邻边
                if j==0:
                    dp[i].append(dp[i-1][j]+triangle[i][j])
                elif j==len(triangle[i])-1:
                    dp[i].append(dp[i-1][j-1]+triangle[i][j])
                else:
#                     当前取值，在上一层的邻边最小值相加
                    dp[i].append(min(dp[i-1][j-1],dp[i-1][j])+triangle[i][j])
        return min(dp[len(triangle)-1])
```

## 递归到动规的一般转化方法

​    递归函数有n个参数，就定义一个n维的数组，数组的下标是递归函数参数的取值范围，数组元素的值是递归函数的返回值，这样就可以从边界值开始， 逐步填充数组，相当于计算递归函数值的逆过程。

​    动规解题的一般思路

​    \1. 将原问题分解为子问题

- ​    把原问题分解为若干个子问题，子问题和原问题形式相同或类似，只不过规模变小了。子问题都解决，原问题即解决(数字三角形例）。
- ​    子问题的解一旦求出就会被保存，所以每个子问题只需求 解一次。

​    2.确定状态

- ​    在用动态规划解题时，我们往往将和子问题相关的各个变量的一组取值，称之为一个“状 态”。一个“状态”对应于一个或多个子问题， 所谓某个“状态”下的“值”，就是这个“状 态”所对应的子问题的解。
- ​    所有“状态”的集合，构成问题的“状态空间”。“状态空间”的大小，与用动态规划解决问题的时间复杂度直接相关。 在数字三角形的例子里，一共有N×(N+1)/2个数字，所以这个问题的状态空间里一共就有N×(N+1)/2个状态。

​    整个问题的时间复杂度是状态数目乘以计算每个状态所需时间。在数字三角形里每个“状态”只需要经过一次，且在每个状态上作计算所花的时间都是和N无关的常数。

​    3.确定一些初始状态（边界状态）的值

​    以“数字三角形”为例，初始状态就是底边数字，值就是底边数字值。

​    \4. 确定状态转移方程

​     定义出什么是“状态”，以及在该“状态”下的“值”后，就要找出不同的状态之间如何迁移――即如何从一个或多个“值”已知的 “状态”，求出另一个“状态”的“值”(递推型)。状态的迁移可以用递推公式表示，此递推公式也可被称作“状态转移方程”。

​    数字三角形的状态转移方程:

​    ![img](https://img-blog.csdn.net/20150811160833998?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)
  

​    **能用动规解决的问题的特点**

​    1) 问题具有最优子结构性质。如果问题的最优解所包含的 子问题的解也是最优的，我们就称该问题具有最优子结 构性质。

​    2) 无后效性。当前的若干个状态值一旦确定，则此后过程的演变就只和这若干个状态的值有关，和之前是采取哪种手段或经过哪条路径演变到当前的这若干个状态，没有关系。

﻿﻿

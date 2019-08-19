# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 20:28:24 2019

@author: PPLoveXueer
"""

# =============================================================================
# 爬楼梯
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 注意：给定 n 是一个正整数。
# =============================================================================

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
    
# =============================================================================
# 矿工挖矿
# 某一个地区发现了5座金矿,每个金矿的黄金储量不同,需要挖掘的工人也不同,设参加挖掘的总共10人,且每座金矿要么全挖,要么不挖,不能派出一半人挖取一半金矿，试问，想得到最多的黄金，应该选择挖取哪几个金矿。
# 金矿    黄金储量    工人数
#            400            5
#            500            5
#            200            3
#            300            4
#            350            3
# =============================================================================
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
# =============================================================================
#       
#       
#       
# 最大子序和
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 
# 示例:
# 
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# =============================================================================
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
    
    
# =============================================================================
# 买卖股票时机
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
# 注意你不能在买入股票前卖出股票。
# 
# 示例 1:
# 
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
# 示例 2:
# 
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
# =============================================================================
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
    
# =============================================================================
# 最小化费爬楼梯
# 数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
# 每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
# 您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。
# 
# =============================================================================
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
    
# =============================================================================
# 比特位计数
# 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
# =============================================================================
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
    
    
# =============================================================================
# 三角形最小路径和
# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
# 
# 例如，给定三角形：
# 
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
# 
# 说明：
# 
# 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
# =============================================================================
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
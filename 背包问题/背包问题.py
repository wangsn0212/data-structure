# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 15:40:27 2019

@author: PPLoveXueer
"""
# =============================================================================
# 0-1背包问题
# 假设我们有n件物品，分别编号为1, 2...n。其中编号为i的物品价值为vi，它的重量为wi。为了简化问题，假定价值和重量都是整数值。现在，假设我们有一个背包，它能够承载的重量是W。现在，我们希望往包里装这些物品，使得包里装的物品价值最大化，那么我们该如何来选择装的东西呢？
# 要求恰好装满背包，那么在初始化时除了 f[0]为 0 其它 f[1..W]均设为-∞
# =============================================================================
import numpy as np

def solve(vlist,wlist,totalWeight,totalLength):
    resArr = np.zeros((totalLength+1,totalWeight+1),dtype=np.int32)
    for i in range(1,totalLength+1):   #依此考虑前i个物品时的最大价值情况
        for j in range(1,totalWeight+1):
            if wlist[i] <= j:
                resArr[i,j] = max(resArr[i-1,j-wlist[i]]+vlist[i],resArr[i-1,j])
            else:
                resArr[i,j] = resArr[i-1,j]
    return resArr[-1,-1]

if __name__ == '__main__':
    v = [0,60,100,120]
    w = [0,10,20,30]
    weight = 50
    n = 3
    result = solve(v,w,weight,n)
    print(result)
    

#完全背包
def CompletePack(N, V, weight, value):
    """
    完全背包问题(每个物品可以取无限次)
    :param N: 物品个数, 如 N=5
    :param V: 背包总容量, 如V=15
    :param weight: 每个物品的容量数组表示, 如weight=[5,4,7,2,6]
    :param value: 每个物品的价值数组表示, 如value=[12,3,10,3,6]
    :return: 返回最大的总价值
    """
    # 初始化f[N+1][V+1]为0，f[i][j]表示前i件物品恰放入一个容量为j的背包可以获得的最大价值
    f = [[0 for col in range(V + 1)] for row in range(N + 1)]

    for i in range(1, N+1):
        for j in range(1, V+1):
            # 注意由于weight、value数组下标从0开始，第i个物品的容量为weight[i-1],价值为value[i-1]
            # j/weight[i-1]表示容量为j时，物品i最多可以取多少次
            f[i][j] = f[i - 1][j]  # 初始取k=0为最大，下面的循环是把取了k个物品i能获得的最大价值赋值给f[i][j]
            for k in range(j/weight[i-1]+1):
                if f[i][j] < f[i-1][j-k*weight[i-1]]+k*value[i-1]:
                    f[i][j] = f[i-1][j-k*weight[i-1]]+k*value[i-1]  # 状态方程

            # 上面的f[i][j]也可以通过下面一行代码求得
            #  f[i][j] = max([f[i-1][j-k*weight[i-1]]+k*value[i-1] for k in range(j/weight[i-1]+1)])
    max_value = f[N][V]
    return max_value

#重复背包
def MultiplePack(N, V, weight, value, num):
    """
    多重背包问题(每个物品都有次数限制)
    :param N: 物品个数, 如 N=5
    :param V: 背包总容量, 如V=15
    :param weight: 每个物品的容量数组表示, 如weight=[5,4,7,2,6]
    :param value: 每个物品的价值数组表示, 如value=[12,3,10,3,6]
    :param num: 每个物品的个数限制，如num=[2,4,1,5,3]
    :return: 返回最大的总价值
    """

    # 初始化f[N+1][V+1]为0，f[i][j]表示前i件物品恰放入一个容量为j的背包可以获得的最大价值
    f = [[0 for col in range(V + 1)] for row in range(N + 1)]
    for i in range(1, N+1):
        for j in range(1, V+1):
            # 对于物品i最多能取的次数是j/weight[i-1]与num[i-1]中较小者
            max_num_i = min(j/weight[i-1], num[i-1])

            f[i][j] = f[i - 1][j]  # 初始取k=0为最大，下面的循环是把取了k个物品i能获得的最大价值赋值给f[i][j]
            for k in range(max_num_i+1):
                if f[i][j] < f[i-1][j-k*weight[i-1]]+k*value[i-1]:
                    f[i][j] = f[i-1][j-k*weight[i-1]]+k*value[i-1]  # 状态方程

            # 上面的f[i][j]也可以通过下面一行代码求得
            # f[i][j] = max([f[i-1][j-k*weight[i-1]]+k*value[i-1] for k in range(max_num_i+1)])
    max_value = f[N][V]
    return max_value

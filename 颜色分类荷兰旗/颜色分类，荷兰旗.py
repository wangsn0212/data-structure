# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 16:08:56 2019

@author: PPLoveXueer
"""

# =============================================================================
# ## 任务 ##
# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
# 
# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
# 
# 注意:
# 不能使用代码库中的排序函数来解决这道题。
# 
#     示例:
#     
#     输入: [2,0,2,1,1,0]
#     输出: [0,0,1,1,2,2]
# 
# 
# ##关键思路 ##
# 
# 用三个指针（p0, p2 和curr）来分别追踪0的最右边界，2的最左边界和当前考虑的元素。
# 
# 
# 
# 1. curr指向值为2时，当前值与p2指向值交换，由于交换过来的值需要再次判断，所以 curr不变， p2 -=1  
# 2. curr指向值为0时，当前值与p0指向值交换，p0 += 1,进一位；由于交换过来的值是已经判断过的值，所以 curr += 1  
# 3. 其余情况 curr += 1 继续判断
# 
# =============================================================================

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p0 = 0
        p2 = len(nums) - 1
        cur = 0
        while cur <= p2:
            if nums[cur] == 0:
                nums[cur], nums[p0] = nums[p0], nums[cur]
                p0 += 1
                cur +=1
                
            elif nums[cur] == 2:
                nums[cur], nums[p2] = nums[p2], nums[cur]
                p2 -=1  
                
            else:
                cur +=1
        return nums
    



            
## 任务 ##
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。

## 关键思路 ##


	class Solution:
    	def maxInWindows(self, num, size):
        	# write code here
        	if not num or not size or size < 1 or size > len(num):
            	return []
        	i = 0
        	result = []
        	while i <= (len(num) - size):
            	result.append(max(num[i:i+size]))
            	i += 1
        	return result

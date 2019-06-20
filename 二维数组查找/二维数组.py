class Solution:
    # array 二维列表
   
    def Find(self, target, array):
        # write code here
        flag = 'false'
        height = len(array)
        for h in range(height):
            if target in array[h]:
                flag = "true"
                break
        return flag

while True:
    try:
        S=Solution()
        # 字符串转为list
        L=list(eval(input("input:")))
        array=L[1]
        target=L[0]
        print(S.Find(target, array))
    except:
        break
    
#输入：1,[[1,2,3],[4,5,6]]
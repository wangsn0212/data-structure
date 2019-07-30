# -*- coding:utf-8 -*-

    # write code here
def exist_helper(matrix, i, j, p):
    if matrix[i][j] == p[0]:
        if not p[1:]:
            return True
        matrix[i][j] = '' #不可重叠
        if i > 0 and exist_helper(matrix, i-1, j, p[1:]):
            return True
        if i < len(matrix)-1 and exist_helper(matrix, i+1, j ,p[1:]):
            return True
        if j > 0 and exist_helper(matrix, i, j-1, p[1:]):
            return True
        if j < len(matrix[0])-1 and exist_helper(matrix, i, j+1, p[1:]):
            return True
        matrix[i][j] = p[0] ##都不符合的话说明选错了起始点要变回
        return False
    else:
        return False    
matrix = 'ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS'
rows = 5
cols = 8
path = "SGGFIECVAASABCEHJIGQEM"    
    
if not matrix:
    print False
if not path:
    print True
x = [list(matrix[cols*i:cols*i+cols]) for i in range(rows)]
for i in range(rows):
    for j in range(cols):       #路径第一个值的遍历
        if exist_helper(x, i, j, path):   
            print True
print False

m,n=(int(x) for x in input().split())
mtr=[]
for i in range(0,m):
    a=[int(x) for x in input().split()]
    if len(a)==n:
        mtr.append(a)
    else:
        break
def findMaxPath(mat):
   
    for i in range(1, n):
  
        res = -1
        for j in range(m):
            if (j > 0 and j < m - 1):
                mat[i][j] += max(mat[i - 1][j],
                                 max(mat[i - 1][j - 1],
                                     mat[i - 1][j + 1]))
            elif (j > 0):
                mat[i][j] += max(mat[i - 1][j],
                                 mat[i - 1][j - 1])
            elif (j < m - 1):
                mat[i][j] += max(mat[i - 1][j],
                                 mat[i - 1][j + 1])

            res = max(mat[i][j], res)
    return res

if __name__=='__main__':
    print(findMaxPath(mtr))

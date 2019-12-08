# mod = 10**9 + 7
#
# # 矩阵快速乘法和幂运算
# def matmul(A,B):
#     C = [[0 for _ in range(len(B[0]))]  for _ in range(len(A))]
#     for i in range(len(A)):
#         for k in range(len(B)):
#             for j in range(len(B[0])):
#                 C[i][j] = (C[i][j] + A[i][k]*B[k][j]%mod)%mod
#     return C
#
# def matpow(A,n):
#     B = [[0 for _ in range(len(A))]  for _ in range(len(A))]
#     for i in range(len(A)):
#         B[i][i] += 1
#     while n:
#         if n & 1:
#             B = matmul(B,A)
#         A = matmul(A,A)
#         n >>= 1
#     return B
#
# # n,a,b,c,f0 = 10**18, 5, 5, 5, 100
# a1,a2,a3,a4,n = map(int,input().split())
#
# A = [[1,0,1,1],[1,0,0,0],[0,1,0,0],[0,0,1,0]]
# A = matpow(A,n-4)
#
# res = (a4*A[0][0]+a3*A[0][1]+a2*A[0][2]+a1*A[0][3]) % mod
# print(res)
#
# mod = 10**9 + 7
#
# a1,a2,a3,a4,n = map(int,input().split())
#
# for i in range(5,n+1):
#     tmp = a1+a2+a4
#     a1,a2,a3,a4 = a2,a3,a4,tmp
# print(a4)

def hasPath(matrix, rows, cols, path):
    n = len(path)
    def dfs(matrix,i,j,k):
        if i < 0 or j < 0 or j >= cols or i > rows:
            return
        if k == n:
            return True
        if matrix[i][j] == path[k]:
            matrix[i][j] = '1'

            return dfs(matrix, i + 1, j, k + 1) or dfs(matrix, i - 1, j, k + 1) or dfs(matrix, i, j + 1, k + 1) or \
            dfs(matrix, i, j - 1, k + 1)

        dfs(matrix, i + 1, j, k + 1)
        dfs(matrix, i - 1, j, k + 1)
        dfs(matrix, i, j + 1, k + 1)
        dfs(matrix, i, j - 1, k + 1)
        return False

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == path[0] and dfs(matrix,i,j,1):
                return True

    return False

matrix = [['a','b','c','d'],['c','f','c','s'],['j','d','e','h']]
rows = 3
cols = 4
path = 'abfc'
print(hasPath(matrix, rows, cols, path))

class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        for i in range(rows):
            for j in range(cols):
                if matrix[i*cols+j] == path[0]:
                    if self.find(list(matrix),rows,cols,path[1:],i,j):
                        return True
        return False

    def find(self,matrix,rows,cols,path,i,j):
        if not path:
            return True

        matrix[i*cols+j]='0'

        if j+1<cols and matrix[i*cols+j+1]==path[0]:
            return self.find(matrix,rows,cols,path[1:],i,j+1)
        elif j-1>=0 and matrix[i*cols+j-1]==path[0]:
            return self.find(matrix,rows,cols,path[1:],i,j-1)
        elif i+1<rows and matrix[(i+1)*cols+j]==path[0]:
            return self.find(matrix,rows,cols,path[1:],i+1,j)
        elif i-1>=0 and matrix[(i-1)*cols+j]==path[0]:
            return self.find(matrix,rows,cols,path[1:],i-1,j)
        else:
            return False












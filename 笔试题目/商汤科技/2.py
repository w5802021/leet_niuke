# 幂运算超时
# n,a,b,c,f0 = 10**8, 0, 0, 0, 100
#
# f1 = f0
# f2 = 0
# f3 = 0
mod = 10**9 + 7
# for i in range(1,n+1):
#
#     tmp = (a * f1 + b * f2 + c * f3 + 2 * (pow(i,2)) - i + 32767)
#     f1, f2, f3 = f2, f3, tmp
#
# print(f3)

# 矩阵快速乘法和幂运算
def matmul(A,B):
    C = [[0 for _ in range(len(B[0]))]  for _ in range(len(A))]
    for i in range(len(A)):
        for k in range(len(B)):
            for j in range(len(B[0])):
                C[i][j] = (C[i][j] + A[i][k]*B[k][j]%mod)%mod
    return C

def matpow(A,n):
    B = [[0 for _ in range(len(A))]  for _ in range(len(A))]
    for i in range(len(A)):
        B[i][i] += 1
    while n:
        if n & 1:
            B = matmul(B,A)
        A = matmul(A,A)
        n >>= 1
    return B

n,a,b,c,f0 = 10**18, 5, 5, 5, 100

f1 = a*f0 + 32768
f2 = a*f1 + b*f0 + 6 + 32767

if n == 0:
    print(f0)
elif n == 1:
    print(f1)
elif n == 2:
    print(f2)
else:
    A = [[0 for _ in range(6)] for _ in range(6)]
    A[0][0] = a
    A[0][1] = b
    A[0][2] = c
    A[0][3] = 2
    A[0][4] = 3
    A[0][5] = 32768
    A[1][0] = 1
    A[2][1] = 1
    A[3][3] = 1
    A[3][4] = 2
    A[3][5] = 1
    A[4][4] = 1
    A[4][5] = 1
    A[5][5] = 1
    A = matpow(A,n-2)
    # 这里采用了（数学归纳法，即）
    # f[i] = a * f[i-1] + b * f[i-2] + c * f[i-3] + 2 * (i^2) - i + 32767
    #      = a * f[i-1] + b * f[i-2] + c * f[i-3] + [2 * (i^2) - i - 1] + 32768
    #      = a * f[i-1] + b * f[i-2] + c * f[i-3] + [2 * (i-1)^2 + 3 * (i-1)] + 32768
    # 从而 f[i] = Fun(f[i-1],f[i-2],f[i-3],i-1)
    '''
    写成矩阵递推式即为：
    [f[i]        [[a, b, c, 2, 3, 32768],    [f[i-1] 
     f[i-1]       [1, 0, 0, 0, 0, 0],         f[i-2]
     f[i-2]  ==   [0, 1, 0, 0, 0, 0],    ×    f[i-3]
     i^2          [0, 0, 0, 1, 2, 1],         (i-1)^2
     i            [0, 0, 0, 0, 1, 1],         (i-1)
     1]           [0, 0, 0, 0, 0, 1]]           1]
    '''
    res = (f2*A[0][0]+f1*A[0][1]+f0*A[0][2]+4*A[0][3]+2*A[0][4]+A[0][5]) % mod
    print('%.2f' %res)



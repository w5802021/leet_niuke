#C(m,n)的计算方法
# 递推法  下式算得c[1][1]--c[100][100]的所有组合次数
def way1():
    N=100
    c = [[0] * (N+1)  for _ in range(N+1)]
    c[0][0] = 1
    for i in range(1,N+1):
        c[i][0] = 1
        for j in range(1,N+1):
            c[i][j] = c[i-1][j-1] + c[i-1][j]

##常规阶数法：
def way2():
    N = 100
    k = 3
    summ = 1
    for i in range(k,0,-1):
        summ *= (N-(k-i))/i
    return int(summ)

way2()


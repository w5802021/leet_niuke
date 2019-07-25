def matrixchainorder(p,n):
    dp = [[None]*n for _ in range(n)]
    for i in range(1,n):
        dp[i][i] = 0

    for l in range(2,n):
        for i in range(1,n-l+1):
            j = i + l - 1
            dp[i][j] = 2**31
            for k in range(i,j):
                q = dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j]
                if q < dp[i][j]:
                    dp[i][j] = q

    return dp[1][n-1]

def matrixchainorder1(p,i,j):
    if i == j:
        return 0

    mins = 2**31
    for k in range(i,j):
        count = matrixchainorder1(p,i,k) + matrixchainorder1(p,k+1,j) + p[i-1]*p[k]*p[j]
        if count < mins:
            mins = count

    return mins

if __name__ == '__main__':
    arr = [40,20,30,10,30]
    n = len(arr)
    print(matrixchainorder(arr,n))
    print(matrixchainorder1(arr,1,n-1))

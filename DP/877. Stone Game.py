def stoneGame(piles):
    n = len(piles)
    # dp[i][j]表示在piles[i:j+1]中，先手方相对于对手能够多出的石子数
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = piles[i]
    # 计算顺序  由对角线向左，由下往上
    for j in range(1,n):
        for i in range(j-1,-1,-1):
            dp[i][j] = max(piles[i]-dp[i+1][j],piles[j]-dp[i][j-1])
    return dp[0][n-1] > 0

if __name__ == '__main__':
    piles = [1,100,3]
    print(stoneGame(piles))
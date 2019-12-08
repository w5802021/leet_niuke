def minCost(costs):
    # write your code here
    n = len(costs)
    # dp[i][j]表示粉刷第i个房子为第j中的颜色的最小费用
    dp = [[float('inf')] * 3 for _ in range(n + 1)]
    dp[0][0] = dp[0][1] = dp[0][2] = 0

    for i in range(1, n + 1):
        # show this time's the last house's color
        for j in range(3):
            # the pre house's color
            for k in range(3):
                if k == j:
                    continue
                dp[i][j] = min(dp[i][j], dp[i - 1][k] + costs[i - 1][j])
    res = min(dp[n][0], dp[n][1], dp[n][2])
    return res
################################房屋染色2#############################
# 颜色为k种

def minCostII(costs):
    # write your code here
    if not costs:
        return 0
    n = len(costs)
    k = len(costs[0])
    # dp[i][j]表示粉刷第i个房子为第j中的颜色的最小费用
    dp = [[float('inf')] * k for _ in range(n + 1)]
    for i in range(k):
        dp[0][i] = 0

    for i in range(1, n + 1):
        # 找出dp[i-1][0]....dp[i-1][k-1]中最小的费用和次小的费用  j2 j1记录颜色种类
        min1 = min2 = float('inf')
        j2 = j1 = float('inf')
        for j in range(k):
            if dp[i - 1][j] < min1:
                min2 = min1
                j2 = j1
                min1 = dp[i - 1][j]
                j1 = j
            else:
                if dp[i - 1][j] < min2:
                    min2 = dp[i - 1][j]
                    j2 = j
        # 转移矩阵
        for j in range(k):
            if j != j1:
                dp[i][j] = dp[i - 1][j1] + costs[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j2] + costs[i - 1][j]

    res = min(dp[n][j] for j in range(k))
    return res

if __name__ == '__main__':
    costs = [[14,2,11],[11,14,5],[14,3,10]]
    print(minCostII(costs))
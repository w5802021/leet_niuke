
def maxProfit(prices):
    # 滚动数组优化空间复杂度
    res = float('-inf')
    if len(prices) <= 1:
        return 0
    minpr = prices[0]
    for i in range(len(prices)):
        diff = prices[i] - minpr
        minpr = min(minpr, prices[i])
        if diff > res:
            res = diff
    return res

##############################122##############################

def maxProfit2(prices):
    '''
    只看相邻两天是否有增长，增长则加上收益
    :param prices:
    :return:
    '''
    profit = 0
    for i in range(1,len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit

#############################买卖股票3##################################
def maxProfit3(prices):
    '''
    思路：5阶段处理法
    1 第一次买前
    2 持有股票
    3 第一次卖之后 第二次卖之前
    4 持有股票
    5 第二次卖之后
    :param prices:
    :return:
    '''
    n = len(prices)
    if n == 0 :
        return 0
    # dp[i][j]表示prices[0]--prices[i-1]，在阶段j的最大获利
    dp = [[0] * (5 + 1) for _ in range(n + 1)]
    dp[0][1] = 0

    for i in range(1, n + 1):
        # 1,3,5阶段 手中无股票
        for j in range(1, 5 + 1, 2):
            # dp[i][j] = max{dp[i-1][j], dp[i-1][j-1] + P_i-1 - P_i-2 }
            dp[i][j] = dp[i - 1][j]
            if j > 1 and i > 1 :
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + prices[i - 1] - prices[i - 2])
        # 2,4阶段  手中有股票
        for j in range(2, 5 + 1, 2):
            # dp[i][j] = max{dp[i-1][j] + P_i-1 – P_i-2 , dp[i-1][j-1], dp[i-1][j-2] + P_i-1 – P_i-2 }
            dp[i][j] = dp[i - 1][j - 1]
            if i > 1 :
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + prices[i - 1] - prices[i - 2])
            if i > 1 and j == 4 :
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 2] + prices[i - 1] - prices[i - 2])
    return max(dp[n][1], dp[n][3], dp[n][5])

def maxProfit31(prices):

    h1 = h2 = - max(prices)
    s1 = s2 = 0
    for price in prices:
        s2, h2, s1, h1 = max(s2, price + h2), max(h2, -price + s1), max(s1, price + h1), max(h1, -price)
    return s2

#################################买卖股票4#####################################

def maxProfit4(K,prices):
    '''
    思路：同3
    :param prices:
    :return:
    '''
    n = len(prices)
    if n == 0 :
        return 0

    # 增加条件，如果K超过n/2次，说明购买次数没有限制，同解决方法2
    if K > n/2:
        res = maxProfit2(prices)
        return res

    dp = [[-1000000] * (2 * K + 2) for _ in range(n + 1)]
    dp[0][1] = 0

    for i in range(1, n + 1):
        # 修改5为2K+1
        for j in range(1, 2 * K + 2, 2):
            # dp[i][j] = max{dp[i-1][j], dp[i-1][j-1] + P_i-1 - P_i-2 }
            dp[i][j] = dp[i - 1][j]
            if j > 1 and i > 1 :
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + prices[i - 1] - prices[i - 2])

        for j in range(2,2 * K + 2, 2):
            # dp[i][j] = max{dp[i-1][j] + P_i-1 – P_i-2 , dp[i-1][j-1], dp[i-1][j-2] + P_i-1 – P_i-2 }
            dp[i][j] = dp[i - 1][j - 1]
            if i > 1 :
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + prices[i - 1] - prices[i - 2])
            if i > 1 and j > 2:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 2] + prices[i - 1] - prices[i - 2])

    return max(dp[n][_] for _ in range(1,2*K+2,2))


if __name__ == '__main__':
    nums = [3,2,6,5,0,3]
    K=2
    print(maxProfit4(K,nums))
def firstWillWin(n):
    '''
    两人摸石子问题
    动态规划思想
    :param n:
    :return:
    '''
    # 石子数还剩为n，是否可赢
    dp = [False]*(n+1)
    dp[1] = dp[2] = True
    for i in range(3,n+1):
        #表示本轮先手可取1或
        dp[i] = (dp[i - 1] == False | dp[i - 2] == False)
    return dp[n]
    # 数学归纳法得到：n%3 != 0

if __name__ == '__main__':
    n = 5
    print(firstWillWin(n))

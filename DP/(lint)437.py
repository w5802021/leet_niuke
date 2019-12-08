def copyBooks( pages, k):
    '''
    动态规划
    :param pages:
    :param k:
    :return:
    '''
    n = len(pages)
    if n == 0:
        return 0
    if k > n:
        k = n
    # 第k个抄写员抄写前i-1本书最少需要花多久时间
    dp = [[float('inf')] * (n + 1) for _ in range(k + 1)]
    dp[0][0] = 0

    for ki in range(1, k + 1):
        dp[ki][0] = 0
        for i in range(1, n + 1):
            dp[ki][i] = float('inf')
            for j in range(i, -1, -1):
                dp[ki][i] = min(dp[ki][i], max(dp[ki - 1][j], sum(pages[x] for x in range(j,i))))
    return dp[k][n]
def copyBooks1( pages, k):
    '''
    贪心+二分
    :param pages:
    :param k:
    :return:
    '''
    def islesstle(pages,k,tmax):
        pagesum = 0
        peonum = 1
        for i in pages:
            if pagesum + i <= tmax:
                pagesum += i
            else:
                peonum += 1
                pagesum = i
        return peonum <= k

    l = max(pages)
    r = sum(pages)
    while l < r:
        mid = l + (r - l) // 2
        if islesstle(pages,k,mid):
            r = mid
        else:
            l = mid + 1
    return l

if __name__ == '__main__':
    pages = [3, 2, 4]
    k = 2
    print(copyBooks1( pages, k))
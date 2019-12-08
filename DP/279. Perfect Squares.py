def numSquares(n):
    '''
    动态规划  时间复杂度：O(n*sqrt(n))
    :param n:
    :return:
    '''
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1,n + 1):
        for j in range(1,int(i**(1/2))+1):
            dp[i] = min(dp[i-j**2]+1,dp[i])
    return dp[n]

def numSquares1(n):
    '''
    bfs
    :param n:
    :return:
    '''
    can_use = []
    for i in range(1,n+1):
        if i**2 <= n:
            can_use.append(i**2)
        else:
            break

    seen = set()
    queue = [(0,0)]
    can_use.sort(reverse=True)

    while queue:
        cur,step = queue.pop(0)
        step += 1
        # 测试can_use内完全平方数的组合
        for num in can_use:
            num += cur
            if num == n:
                return step
            if num < n and (num,step) not in seen:
                seen.add((num,step))
                queue.append((num,step))

if __name__ == '__main__':
    n = 12
    print(numSquares1(n))

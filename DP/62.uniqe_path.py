
def uniquePaths(m,n):

    dp = [[1 for i in range(n)] for j in range(m)]

    if m == 0 and n == 0:   #增加这两行代码提高了速度
        return 0

    for i in range(m):
        for j in range(n):
            if i != 0 and j != 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]

def uniquePathsWithObstacles(grid):    #63.带障碍物

    m,n = len(grid),len(grid[0])
    dp = [[0 for i in range(n)] for j in range(m)]

    if m == 0 and n == 0:  # 增加这两行代码提高了速度
        return 0
    if grid[0][0] == 1:
        return 0
    else:
        dp[0][0] = 1

    for i in range(1,m):               #dp第一列赋值
        if grid[i][0] != 1:
            dp[i][0] = dp[i-1][0]
        else:
            dp[i][0] = 0

    for i in range(1,n):               #dp第一行赋值
        if grid[0][i] != 1:
            dp[0][i] = dp[0][i-1]
        else:
            dp[0][i] = 0

    for i in range(1,m):
        for j in range(1,n):
            if grid[i][j] != 1:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            else:
                dp[i][j] = 0
    return dp[-1][-1]

if __name__ == '__main__':
    # m,n=3,2
    # print(uniquePaths(m,n))
    nums = [[1,0,0],[0,1,0],[0,0,0]]
    print(uniquePathsWithObstacles(nums))
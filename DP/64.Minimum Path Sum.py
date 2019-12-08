######
######矩阵第一行和第一列的数要单独进行计算，其它的遵循迭代公式计算即可
######
def minPathSum(grid):
    m,n = len(grid),len(grid[0])
    #1、确定状态 dp[i][j]为i行，j列矩阵的最小路径之和
    dp = [[0 for _ in range(n)] for _ in range(m)]

    if m == 0 and n == 0:   #增加这两行代码提高了速度
        return 0
    # 第4、计算顺序 ，自左向右，自上向下
    for i in range(m):
        for j in range(n):
            # 第3、初始条件
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
            # 第2、状态转移矩阵
            elif i == 0 and j != 0:
                dp[i][j] = dp[i][j-1] + grid[i][j]
            elif j == 0 and i != 0:
                dp[i][j] = dp[i-1][j] + grid[i][j]
            else:
                dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])
    return dp[-1][-1]

###滚动数组优化空间复杂度
def minPathSum1(grid):
    m,n = len(grid),len(grid[0])

    dp = [[0 for _ in range(n)] for _ in range(2)]

    if m == 0 and n == 0:
        return 0
    old = 1
    now = 0
    # 第4、计算顺序 ，自左向右，自上向下
    for i in range(m):
        # old为i-1行 now为i行
        old = now
        now = 1- now
        for j in range(0,n):
            if i == 0 and j == 0:
                dp[now][j] = grid[i][j]
                continue
            # 第2、状态转移矩阵
            dp[now][j] = grid[i][j]
            if i > 0:
                t1 = dp[old][j]
            else:
                t1 = float('inf')
            if j > 0:
                t2 = dp[now][j-1]
            else:
                t2 = float('inf')
            if t1 < t2:
                dp[now][j] += t1
            else:
                dp[now][j] += t2

    return dp[now][n-1]


if __name__ == '__main__':
    nums = [[1,3,1], [1,5,1], [4,2,1]]
    nums1= [[1,4,3],[8,7,5],[2,1,5]]
    print(minPathSum1(nums1))
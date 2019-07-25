######
######矩阵第一行和第一列的数要单独进行计算，其它的遵循迭代公式计算即可
######
def minPathSum(grid):
    m,n = len(grid),len(grid[0])
    dp = [[0 for i in range(n)] for j in range(m)]

    if m == 0 and n == 0:   #增加这两行代码提高了速度
        return 0

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
            elif i == 0 and j != 0:
                dp[i][j] = dp[i][j-1] + grid[i][j]
            elif j == 0 and i != 0:
                dp[i][j] = dp[i-1][j] + grid[i][j]
            else:
                dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])
    return dp[-1][-1]

if __name__ == '__main__':
    nums = [[1,3,1], [1,5,1], [4,2,1]]
    nums1= [[1,4,3],[8,7,5],[2,1,5]]
    print(minPathSum(nums1))
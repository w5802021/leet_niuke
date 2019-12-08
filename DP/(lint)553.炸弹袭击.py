def maxKilledEnemies(grid):
    # write your code here
    m = len(grid)

    if not grid or m == 0 or len(grid[0]) == 0:
        return 0
    n = len(grid[0])
    dp = [[0] * n for _ in range(m)]
    res = [[0] * n for _ in range(m)]

    # up
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'W':
                dp[i][j] = 0
            else:
                dp[i][j] = 0
                if grid[i][j] == 'E':
                    dp[i][j] = 1
                if i > 0:
                    dp[i][j] += dp[i - 1][j]

            res[i][j] += dp[i][j]

    # down
    for i in range(m - 1, -1, -1):
        for j in range(n):
            if grid[i][j] == 'W':
                dp[i][j] = 0
            else:
                dp[i][j] = 0
                if grid[i][j] == 'E':
                    dp[i][j] = 1
                if i < m - 1:
                    dp[i][j] += dp[i + 1][j]

            res[i][j] += dp[i][j]

    # left
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'W':
                dp[i][j] = 0
            else:
                dp[i][j] = 0
                if grid[i][j] == 'E':
                    dp[i][j] = 1
                if j > 0:
                    dp[i][j] += dp[i][j - 1]

            res[i][j] += dp[i][j]

    # right
    for i in range(m):
        for j in range(n - 1, -1, -1):
            if grid[i][j] == 'W':
                dp[i][j] = 0
            else:
                dp[i][j] = 0
                if grid[i][j] == 'E':
                    dp[i][j] = 1
                if j < n - 1:
                    dp[i][j] += dp[i][j + 1]

            res[i][j] += dp[i][j]
    maxx = 0
    for i in range(m) :
        for j in range(n):
            if grid[i][j] == '0':
                if res[i][j] > maxx:
                    maxx = res[i][j]

    return maxx

if __name__ == '__main__':
    grid = ["E"]
    print(maxKilledEnemies(grid))
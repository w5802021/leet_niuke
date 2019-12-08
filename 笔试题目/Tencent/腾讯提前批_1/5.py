'''
动态规划，由于设定的最优子状态不能保证找到的当前层路径最优后续的路径也是最优的，状态变量设定错误
         只AC0.2
         （接下来往lintcode 515 Paint House那道题上想，每当该层出现0，要维护两种不同状态的分叉的最优）

'''

# n = int(input())
# grid = []
# for i in range(n):
#     grid.append([int(c) for c in input().split()])
n = 6
grid = [[1,2,3],[8,9,10],[5,0,5],[-9,-8,-10],[0,1,2],[5,4,6]]
class node:
    def __init__(self,val,flag):
        self.val = val
        self.flag = flag

dp = [[node(0,1)]*3 for _ in range(n+1)]
# for j in range(3):
#     dp[0][j].append([0,1])

for i in range(1,n+1):
    zuo = dp[i - 1][0].val + dp[i - 1][0].flag*grid[i-1][0]
    you = dp[i - 1][1].val + dp[i - 1][1].flag*grid[i-1][0]

    if zuo > you:
        val = zuo
        if grid[i-1][0] == 0:
            flag = -1 * dp[i - 1][0].flag
        else:
            flag = dp[i - 1][0].flag
        dp[i][0] = node(val,flag)
    else:
        val = you
        if grid[i-1][0] == 0:
            flag = -1 * dp[i - 1][1].flag
        else:
            flag = dp[i - 1][1].flag
        dp[i][0] = node(val, flag)

    zuo =  dp[i - 1][0].val + dp[i - 1][0].flag*grid[i-1][1]
    zhong = dp[i - 1][1].val + dp[i - 1][1].flag*grid[i-1][1]
    you = dp[i - 1][2].val + dp[i - 1][2].flag*grid[i-1][1]

    if zuo > zhong and zuo > you:
        val = zuo
        if grid[i-1][1] == 0:
            flag = -1 * dp[i - 1][0].flag
        else:
            flag = dp[i - 1][0].flag
        dp[i][1] = node(val,flag)
    elif zhong > zuo and zhong > you:
        val = zhong
        if grid[i-1][1] == 0:
            flag = -1 * dp[i - 1][1].flag
        else:
            flag = dp[i - 1][1].flag
        dp[i][1] = node(val, flag)
    else:
        val = you
        if grid[i-1][1] == 0:
            flag = -1 * dp[i - 1][2].flag
        else:
            flag = dp[i - 1][1].flag
        dp[i][1] = node(val, flag)

    zuo = dp[i - 1][1].val + dp[i - 1][1].flag * grid[i-1][2]
    you = dp[i - 1][2].val + dp[i - 1][2].flag * grid[i-1][2]

    if zuo > you:
        val = zuo
        if grid[i-1][2] == 0:
            flag = -1 * dp[i - 1][1].flag
        else:
            flag = dp[i - 1][1].flag
        dp[i][2] = node(val, flag)
    else:
        val = you
        if grid[i-1][2] == 0:
            flag = -1 * dp[i - 1][2].flag
        else:
            flag = dp[i - 1][2].flag
        dp[i][2] = node(val, flag)
    a = 1
maxx = max(dp[n][0].val,dp[n][1].val,dp[n][2].val)

print(maxx)

# dp[i][2][0] = max(dp[i - 1][1][0], dp[i - 1][2][0]) + grid[i][2]
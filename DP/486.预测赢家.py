def PredictTheWinner(nums):
    n = len(nums)
    # 表示从nums[i]到nums[j]先手比另一位玩家多的分数，最后返回dp[0][len(nums)-1]是否大于0即可
    dp = [[0 for _ in range(n)] for _ in range(n)]
    # 初始化 当i=j时，先手一定赢，比另一位玩家多dp[i][j]
    for i in range(n):
        dp[i][i] = nums[i]
    # 从下往上 从对角线往右
    for i in range(n-1,-1,-1):
        for j in range(i+1,n):
            # 如果先手拿nums[i], 则后手比先手所dp[i+1][j]
            # 如果先手拿nums[j], 则另一位玩家比先手多dp[i][j-1],
            dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j - 1])
    return dp[0][n-1] >= 0

if __name__ == '__main__':
    nums = [1,5,2]
    print(PredictTheWinner(nums))

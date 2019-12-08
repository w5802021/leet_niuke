
def mincostTickets(days, costs):
    # 这里+31是为了防止在第一个30天内,i-30的索引为负，做此初始化，则转移方程可节省条件判断语句
    # dp = [0] * (days[-1] + 31)
    # 1、确定状态  dp[i]表示一年内到当天为止，旅行所需的最低消费
    # 3、初始化
    dp = [0] * (days[-1] + 1)
    # 列表中存在不唯一的数尽量用集合，速度更快
    dayset = set(days)
    # 4、计算顺序  自左往右
    for i in range(1, days[-1]+1):
        # 2、转移矩阵
        if i not in dayset:
            dp[i] = dp[i - 1]
        else:
            dp[i] =  min(dp[i - 1] + costs[0], (dp[i - 30] if i >= 30 else 0) + costs[2],
                         (dp[i - 7] if i >= 7 else 0) + costs[1])

    return dp[days[-1]]

if __name__ == '__main__':
    days = [1,4,6,7,8,20]
    costs = [2,7,15]
    print(mincostTickets(days,costs))
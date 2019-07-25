
def mincostTickets(days, costs):

    dp = [0] * (days[-1] + 31)                    #dp的大小尽量压缩精确，可减少递推矩阵的搜索时间   ，这里+31是为了防止在第一个30天内,i-30的索引为负，要让其dp[i-30]取值为0
    dayset = set(days)                          #列表中存在不唯一的数尽量用集合，速度更快

    for i in range(1, days[-1]+1):   #取到1-days[-1]
        if i not in dayset:
            dp[i] = dp[i - 1]
        else:
            dp[i] =  min(dp[i - 1] + costs[0], dp[i - 30] + costs[2], dp[i - 7] + costs[1])

    return dp[days[-1]]

if __name__ == '__main__':
    days = [1,4,6,7,8,20]
    costs = [2,7,15]
    print(mincostTickets(days,costs))
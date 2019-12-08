

############DP方法#################耗时较大###
def coinChange(coins,amount):
    '''
    动态规划
    :param coins:
    :param amount:
    :return:
    '''
    # 1、确定状态 dp[i]表示总金额为i块钱的最小硬币兑换数
    # 3、初始化及边界条件
    dp = [0] + [float('inf')] * amount
    # 4、计算方向 自左往右
    for i in range(min(coins),amount+1):
        # 2、状态转移方程
        dp[i] = min(dp[i - coin] for coin in coins if coin <= i) + 1
    return dp[-1] if dp[-1] < float('inf') else -1


#####################################DFS##########################
def coinChange2(coins, amount):
    '''
    DFS
    :param coins:
    :param amount:
    :return:
    '''
    # 面值大者排前面（贪心策略）
    coins.sort(reverse=True)
    res =  float('inf')
    def dfs(pt, remain, count):
        '''
        :param pt:从大到小排序的硬币数组的某个下标
        :param remain: 剩下的还需要找零的钱
        :param count: 已经兑换的零钱数量
        :return: None
        '''
        # res：当前递归产生的最小的零钱兑换次数
        nonlocal res
        # 递归停止条件
        if not remain:
            res = min(res, count)
        # 先试大面值的硬币,如果不能到达终止条件,剪枝（退回到上一层递归在用较小的面值的硬币）
        for i in range(pt, len(coins)):
            # 增加coins[i] * (res - count)剪枝，
            # 其意义：如果当前剩余需要找零的钱remain全用coin[i]进行兑换，
            # 其所需要花费的硬币数量大于等于（res-count）,
            # 说明后续在该节点展开的子树，其最小的硬币兑换数将超过res
            if coins[i] <= remain < coins[i] * (res - count):
                dfs(i, remain - coins[i], count + 1)

    # 先用大面值递归查找
    for i in range(len(coins)):
        dfs(i, amount, 0)
    return res if res < float('inf') else -1

if __name__ == '__main__':
    coins = [2,5,7]
    amount = 27
    # print(coinChange(coins,amount))
    print(coinChange2(coins,amount))
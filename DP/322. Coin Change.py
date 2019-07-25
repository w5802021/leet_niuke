############DP方法#################耗时较大###
def coinChange(coins,amount):
    # 另为amount，以方便在遍历第一个coin时，给dp初始化值，随后没遍历一个coin与前面遍历的dp值大小进行对比，选出消耗少的
    dp = [0] + [amount + 1] * amount
    # 交换循环位置提升速度
    # for coin in coins:
    for i in range(min(coins),amount+1):
        # dp[i] = min(dp[i],dp[i - coin] + 1)
        # 用列表推导 快于 生成器  短循环用列表存储
        dp[i] = min([dp[i-coin] for coin in coins if coin <= i]) + 1
    # DP[-1]若被优化 必定少于amount + 1
    return dp[-1] if dp[-1] < amount + 1 else -1


##########################################DFS##########################
def coinChange2(coins, amount):
    # 面值大者排前面
    coins.sort(reverse=True)
    # res设为较大的值  大于amount即可
    res =  amount +1
    # 前序遍历  深度递归
    def dfs(pt, remain, count):
        # 引用外部变量
        nonlocal res
        if not remain:
            res = min(res, count)
        # 先全部试大面值的纸币，直到最后等于0
        for i in range(pt, len(coins)):
            # 增加 [(amount + 1) - count] * coins[i]  优化效果明显
            if coins[i] <= remain < coins[i] * (res - count):
                dfs(i, remain - coins[i], count + 1)
    # 先用大面值，在用小面值计算套入
    for i in range(len(coins)):
        dfs(i, amount, 0)
    return res if res <= amount else -1

if __name__ == '__main__':
    coins = [1,2,5]
    amount = 11
    # print(coinChange(coins,amount))
    print(coinChange2(coins,amount))
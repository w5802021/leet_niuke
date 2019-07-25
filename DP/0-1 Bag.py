#动态规划解题步骤：1、问题抽象化
#                 2、建立模型
#                 3、寻找约束条件
#                 4、判断是否满足最优性原理
#                 5、找大问题与小问题的递推关系式、填表、寻找解组成

#动态规划与分治法相同点：都是把大问题拆分成小问题，通过寻找大问题与小问题的递推关系，
# 解决一个个小问题，最终达到解决原问题的效果

#动态规划与分治法不同点：分治法在子问题和子子问题等上被重复计算了很多次，而动态规划则具有记忆性，
# 通过填写表把所有已经解决的子问题答案纪录下来，在新问题里需要用到的子问题可以直接提取，
# 避免了重复计算，从而节约了时间，所以在问题满足最优性原理之后，用动态规划解决问题的核心就在于填表，
# 表填写完毕，最优解也就找到。

#0-1背包问题求解

#Q:有n个物品，它们有各自的体积和价值，现有给定容量的背包，如何让背包里装入的物品具有最大的价值总和？
#n＝4，背包容量cap＝30


V = [0,12,8,9,5]
W = [0,15,10,12,8]
n = 4
cap = 30
dp = [[0] * (cap+1) for i in range(n+1)]
items = [0] * (n+1)

def findoptv(W,V,n,cap):                           #找到最优的价值总和（最优解求解）

    for i in range(1,n+1):
        for j in range(1,cap+1):
            if j < W[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-W[i]]+V[i])       ###状态转移找到最优解

    return max(max(row) for row in dp)

def finditems(i,j):                                  #找到得到最优的价值总和由哪些商品组成（最优解回溯）

    if (i >= 0):
        if(dp[i][j] == dp[i-1][j]):
            items[i] = 0
            finditems(i-1,j)

        elif (j>=W[i]) & (dp[i][j] == dp[i-1][j-W[i]] + V[i]):
            items[i] = 1
            finditems(i-1,j-W[i])

    return items



if __name__ == '__main__':

    print(findoptv(W,V,n,cap))
    print(finditems(n,cap))

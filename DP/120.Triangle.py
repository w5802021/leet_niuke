
#其实上一行到下一行就两个选择，横坐标不变或加一
def minimumTotal(triangle):  #二维DP

    n = len(triangle)
    for i in range(n-2,-1,-1):  #从倒数第二层
        for j in range(len(triangle[i])):
            triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1])   #triangle[i+1][j]是倒数第一层
    print(triangle)   #保存了每个位置计算的路径值
    return triangle[0][0]

def minimumTotal2(triangle):   #一维DP

    n = len(triangle)
    dp = triangle[-1]
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            dp[j] = triangle[i][j] + min(dp[j],dp[j+1])
    print(dp)       #保存了每一层计算的路径做小值
    return dp[0]

if __name__ == '__main__':
    nums = [[-1],[2,3],[1,-1,-3]]
    print(minimumTotal2(nums))
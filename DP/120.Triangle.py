


def minimumTotal(triangle):
    '''
    方法：二维DP
    其实上一行到下一行就两个选择，横坐标不变或加一
    :param triangle:
    :return:
    '''
    # 第3、这里无需初始化
    n = len(triangle)
    # 第3、计算顺序 自下向上 自左往右（自下向上的原因：减少最后dp列表的最优判断）
    # 从倒数第二层开始  此时triangle[i+1][j]是倒数第一层
    for i in range(n-2,-1,-1):
        for j in range(len(triangle[i])):
            # 第1、确定状态  triangle[i][j]表示当前三角形位置的最小路径之和
            # 第2、转移方程
            triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1])
    #保存了每个位置计算的路径值
    return triangle[0][0]

def minimumTotal2(triangle):
    '''
    方法：一维DP
    :param triangle:
    :return:
    '''
    n = len(triangle)
    dp = triangle[-1]
    # 第4
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            # 第1  第2
            dp[j] = triangle[i][j] + min(dp[j],dp[j+1])
    #保存了每一层计算的路径做小值
    return dp[0]

if __name__ == '__main__':
    nums =[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
    print(minimumTotal(nums))
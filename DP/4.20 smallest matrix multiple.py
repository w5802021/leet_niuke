def matrixchainorder(nums,n):
    '''
    方法：动态规划法
    :paragram nums:矩阵维度数组
    :paragram n:len(nums)
    :return:
    '''
    # 第1、确定状态dp[i][j]，nums[i]--nums[j]之间的最优矩阵链之积
    # 初始化其为最大值
    dp = [[float('inf')]*n for _ in range(n)]
    # 第3、初始条件及边界情况
    for i in range(1,n):
        # dp[i,i]之间没有分割点
        dp[i][i] = 0

    for l in range(2,n):
        # 第4、计算顺序，自顶向下
        for i in range(1,n-l+1):
            j = i + l - 1
            # dp[i][j] = 2**31
            for k in range(i,j):
                # 第2、转移方程
                # k 为dp[i,j]最优值的分割点
                q = dp[i][k] + dp[k+1][j] + nums[i-1]*nums[k]*nums[j]
                if q < dp[i][j]:
                    dp[i][j] = q

    return dp[1][n-1]

def matrixchainorder1(nums,i,j):
    '''
    方法：递归法
    思路：在大小为n的矩阵链中，有1,2,3,...,n-1中方式放置第一组括号
    :paragram nums:
    :paragram i:
    :paragram j:
    :return:
    '''
    if i == j:
        return 0
    mins = 2**31
    k = i
    while k < j:
        # nums[i]--nums[k]在i-k中继续找  nums[k+1]--nums[j]在k+1-j中继续找
        # nums[i - 1] * nums[k] * nums[j] 表示i-1至j直接的矩阵链相乘已经计算完毕，要i-1是因为递归初始是从1开始的
        count = matrixchainorder1(nums,i,k) + matrixchainorder1(nums,k+1,j) + nums[i-1]*nums[k]*nums[j]
        if count < mins:
            mins = count
        k += 1
    return mins

if __name__ == '__main__':
    arr = [40,20,30,10,30]
    # 40×20,20×30,30×10,10×30
    n = len(arr)
    print(matrixchainorder(arr,n))
    print(matrixchainorder1(arr,1,n-1))

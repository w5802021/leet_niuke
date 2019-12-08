
###################################198########################################
def rob(nums):
    '''
    动态规划 , 备忘录法 o(n^2)
    :param nums:
    :return:
    '''
    # 1、确定状态 dp[i]为到达当前位置获得的最大金币
    dp = [0 for i in range(len(nums))]
    dp[0] = nums[0]
    dp[1] = nums[1]
    for i in range(2,len(nums)):
        # 多次使用max()增加时间复杂度
        dp[i] = nums[i] + max([dp[x] for x in range(i-1)])
    return max(dp)
def rob1(nums):
    '''
    动态规划 优化时间
    时间   o(n)
    空间   o(n)
    :param nums:
    :return:
    '''
    # 1、确定状态 dp[i]为到达当前位置获得的最大金币
    dp = [0 for i in range(len(nums))]
    # 3、边界条件
    dp[0] = nums[0]
    dp[1] = max(nums[0],nums[1])
    # 4、计算顺序 自左向右
    for i in range(2,len(nums)):
        # 2、转移方程
        dp[i] = max(nums[i] + dp[i-2],dp[i-1])
    return dp[-1]

def rob2(nums):
    '''

    动态规划   优化空间
    时间      o(n)
    空间      o(1)
    :param nums:
    :return:
    '''
    # now i指向的点 last i前一个点
    last = now = 0
    for i in range(len(nums)):
        # 等号右边的dp_prev与等号左边的dp_m相差2个下标位置
        now, last = max(nums[i] + last, now), now
    return last

####################################213##########################################
def rob_circle(nums):
    if len(nums) == 1:
        return nums[1]
    pre1 = rob2(nums[1:])
    pre2 = rob2(nums[:-1])
    return max(pre1, pre2)

if __name__ == '__main__':
    nums = [2,7,9,3,1]
    print(rob1(nums))
    nums1 = [1]
    print(rob_circle(nums))
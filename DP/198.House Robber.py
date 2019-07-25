
###################################198########################################
def rob(nums):            #自己实现  beat 50%
    dp = [0 for i in range(len(nums))]
    dp[0] = nums[0]
    dp[1] = nums[1]

    for i in range(2,len(nums)):
        dp[i] = nums[i] + max([dp[x] for x in range(i-1)])
    return max(dp)

def rob2(nums):
    dp_n = dp_prev = 0   #dp_n i指向的点 dp_prev i前一个点
    for i in range(len(nums)):
        dp_n, dp_prev = max(nums[i] + dp_prev, dp_n), dp_n  #等号右边的dp_prev与等号左边的dp_m相差2个下标位置
    return dp_n

####################################213##########################################
def rob_circle(nums):

    return max(rob2(nums[len(nums) != 1:]), rob2(nums[:-1]))    #nums[len(nums) != 1:] 表示 len(nums) != 1 成立，则索引取1:...,
                                                                                       # 否则索引取 0:...

if __name__ == '__main__':
    nums = [2,7,9,3,1]
    print(rob2(nums))
    nums1 = [1]
    print(rob_circle(nums1))
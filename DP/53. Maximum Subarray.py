
def maxSubArray(nums):    ######DP方法#####    nums中存的是在当前下标及其之前的最优子序列的值
    for i in range(1, len(nums)):                #基本思想就是保证dp[i]前面计算的最优子序列的和要大于等于0  否则舍去前面的子序列
        nums[i] = nums[i] + max(nums[i - 1], 0)
    return max(nums)

def maxSubArray2(nums):       ###耗时少###

    ans = nums[0]
    current_sum = 0

    for i in range(len(nums)):
        if current_sum > 0:
            current_sum += nums[i]
        else:
            current_sum = nums[i]
        ans = max(ans,current_sum)
    return ans

###################################分治法解决问题#########################

def maxSubArrayHelper( nums, l, r):     ########待看
    if l > r:
        return -2147483647
    m = (l + r) // 2

    leftMax = sumNum = 0
    for i in range(m - 1, l - 1, -1):
        sumNum += nums[i]
        leftMax = max(leftMax, sumNum)

    rightMax = sumNum = 0
    for i in range(m + 1, r + 1):
        sumNum += nums[i]
        rightMax = max(rightMax, sumNum)

    leftAns = maxSubArrayHelper(nums, l, m - 1)
    rightAns = maxSubArrayHelper(nums, m + 1, r)

    return max(leftMax + nums[m] + rightMax, max(leftAns, rightAns))

def maxSubArray3(nums):
    return maxSubArrayHelper(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]

    print(maxSubArray3(nums))
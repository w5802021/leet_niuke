def findLengthOfLCIS( nums):
    '''
    最长连续递增子序列
    不需要动态规划
    :param nums:
    :return:
    '''
    if len(nums) < 1:
        return 0
    res = 1
    index = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            res = max(res, i - index + 1)
        else:
            index = i
    return res


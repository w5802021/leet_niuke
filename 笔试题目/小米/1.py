def fun(nums):
    # 令初始为最大的数

    maxsum = nums[0]
    for i in range(len(nums)):
        maxtmp = 0
        for j in range(i,len(nums)):
            maxtmp += nums[j]
            if maxtmp > maxsum:
                maxsum = maxtmp
    return maxsum

nums = [int(c) for c in input().split()]
print(fun(nums))
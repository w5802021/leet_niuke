def maxcover(nums,L):
    i = 0
    j = 1
    n = len(nums)
    count = 2
    maxcount = 1
    start = i
    res = []
    while i < n and j < n:
        while (j < n) and (nums[j] - nums[i] <= L):
            j += 1
            count += 1

        j -= 1
        count -= 1

        if count > maxcount:
            start = i  #记录覆盖点的起点
            maxcount = count
        i += 1
        j += 1
    res = [nums[x] for x in range(start,start + maxcount)]

    return maxcount,res

if __name__ == '__main__':
    nums = [1,3,7,8,10,11,12,13,15,16,17,19,25]
    L = 8
    print(maxcover(nums,L))


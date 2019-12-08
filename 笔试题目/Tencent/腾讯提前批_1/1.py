n,k = map(int,input().split())
nums = [int(c) for c in input().split()]

if len(set(nums)):
    print(1)

else:
    queue = nums[:k]
    tmp = res = sum(queue)
    minidx = 0

    for i in range(k,n):
        tmp = tmp - nums[i - k] + nums[i]
        if tmp < res:
            res = tmp
            minidx = i - k + 2
    print(minidx)









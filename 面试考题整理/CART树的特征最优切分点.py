
def summ(nums,flag):
    res = []
    cur = 0
    square = 0
    if flag:
        for i in range(len(nums)):
            cur += nums[i]
            square += nums[i] * nums[i]
            # E[x^2] - E[x]^2
            res.append(square/(i+1) - (cur/(i+1))**2)
    else:
        for i in range(len(nums)-1,-1,-1):
            cur += nums[i]
            square += nums[i] * nums[i]
            # E[x^2] - E[x]^2
            res.append(square/(i+1) - (cur/(i+1))**2)
    return res

nums = [int(c) for c in input().split()]
# 从左到右做一遍方差，再从右到左求一遍方差，然后就可以求了。
left  = summ(nums,True)
right = summ(nums,False)

n = len(nums)
k = 0
minn = float('inf')

for i in range(1,n):
    if left[i-1] + right[n - i - 1] < minn:
        minn = left[i-1] + right[n - i - 1]
        k = i - 1
print(k)
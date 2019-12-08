n,m = map(int,input().split())

nums = [int(c) for c in input().split()]

# n,m = 7,2
# nums = [ 4, 3, 3, 3, 1, 5, 5 ]
from collections import Counter
dic = Counter(nums)
res = []
i = 0
while i < len(nums):
    times = nums[i]
    if dic[nums[i]] > m:
        i += dic[nums[i]]
    else:
        res += [nums[i]]*dic[nums[i]]
        i += dic[nums[i]]
print(' '.join(str(c) for c in res))
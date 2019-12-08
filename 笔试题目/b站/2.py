n,s = map(int,input().split())
nums = [int(c) for c in input().split()]
l,r = 0,0
total = 0
minl = float('inf')
count = 0
while l < len(nums) and r < len(nums):
    while total < s and r < len(nums):
        total += nums[r]
        count += 1
        r += 1
    if count < minl:
        minl = count

    total -= nums[l]
    l += 1
    count -= 1
print(minl)
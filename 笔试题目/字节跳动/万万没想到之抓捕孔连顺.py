# 固定左端left（即确定该位置放入特工C(1, 1)）），记忆当前左端所能到达最大的右端坐标right，从后续可用数中选两个
# 即组合数为C(right - left, 2)


n,d = 4,3
nums = [1,2,3,4]

mod = 99997867
i = 0
res = 0
pos = 2
while i < len(nums)-2:

    if nums[pos] - nums[i] > d:
        i += 1
        continue
    while pos+1 <= len(nums)-1 and nums[pos+1] - nums[i] <= d:
        pos += 1
    res += (pos - i)*(pos - i -1)//2
    i += 1

print(res%mod)


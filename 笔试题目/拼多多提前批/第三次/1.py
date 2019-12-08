n,m = map(int,input().split())
nums = [int(x) for x in input().split()]
nums.sort()
arr = nums[:2*m]
res = 0
for i in range(m):
    res += arr[i]*arr[2*m-1-i]
print(res)
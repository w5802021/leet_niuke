N = int(input())
nums = [int(c) for c in input().split()]
if N < 3:
    print(-1)
res = -1
for i in range(3,N):
    shape = nums[:i]
    max_len = max(shape)
    shape.remove(max_len)
    if sum(shape) > max_len:
        res = i
        break
    if i == N-1:
        print(-1)


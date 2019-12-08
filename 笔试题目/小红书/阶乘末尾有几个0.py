n = int(input())

res = 0
for i in range(1,n+1):
    count = 0
    while i >= 5:
        i = i // 5
        count += i
    res += count

print(res)
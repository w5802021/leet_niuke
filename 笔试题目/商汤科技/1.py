
n,m = map(int,input().split())
xiguas = []

for _ in range(n):
    ti,wi = map(int,input().split())
    xiguas.append([ti,wi])
xiguas.sort(key = lambda x:x[1],reverse=True)


for _ in range(m):
    d = int(input())
    res = 0
    # 应该二分搜索进行优化
    for xigua in xiguas:
        if xigua[0] >= d:
            res += xigua[1]
            break
    if res:
        print(res)
    else:
        print(-1)








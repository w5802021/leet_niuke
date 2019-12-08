n,m = map(int,input().split())
from collections import defaultdict
guys = []
guysdic = defaultdict(int)
for i in range(m):
    key = tuple(map(int, input().split()))
    guys.append(key)
    guysdic[key] = i
guys.sort(key = lambda x:x[0])

res = 0
ans = [0] * m
for i in range(m):
    if i == 0:
       res += guys[i][1] - guys[i][0] + 1
       ans[guysdic[guys[i]]] = res
    else:
        if guys[i][1] <= guys[i-1][1]:
            ans[guysdic[guys[i]]] = res
            continue
        else:
            if guys[i][0] > guys[i-1][1]:
                res += guys[i][1] - guys[i][0] + 1
                ans[guysdic[guys[i]]] = res
            else:
                chongdie = guys[i-1][1] - guys[i][0] + 1
                res += guys[i][1] - guys[i][0] + 1
                res -= chongdie
                ans[guysdic[guys[i]]] = res
for r in ans:
    print(r)



n = int(input())
nochan = []
for _ in range(n):
    a,b,c = map(str,input().split(','))
    nochan.append([a,b,c])

m = int(input())
from collections import defaultdict

dic = defaultdict(list)
for _ in range(m):
    a,b,c,d = map(str,input().split(','))
    dic[(a, b)].append(c)
    dic[(a, b)].append(d)
res = []
for passen in nochan:
    if (passen[0],passen[1]) in dic:
        tmp = dic[(passen[0], passen[1])]
        tmp.append(passen[2])
        res.append(tmp)
    else:
        res.append(passen)

seen1 = set()
seen2 = set()
res2 = []

for idxx,i in enumerate(res):
    if (i[0],i[1]) not in seen1 and (i[0],i[2]) not in seen2:
        seen1.add((i[0],i[1]))
        seen2.add((i[0],i[2]))
        res2.append(i)

res2.sort(key = lambda x:(x[0],x[1]))

for k in res2:
    print(','.join(k))

# 3
# CZ7132,A1,ZHANGSAN
# CZ7132,A2,ZHAOSI
# CZ7156,A2,WANGWU
# 2
# CZ7132,A1,CZ7156,A2
# CZ7156,A2,CZ7156,A3






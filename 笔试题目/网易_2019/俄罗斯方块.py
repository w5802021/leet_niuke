n,m = map(int, input().split())
cols = [int(c) for c in input().split()]

from collections import Counter

dic_col = Counter(cols)
if len(dic_col.keys()) == n:
    res = min(dic_col.values())
else:
    res = 0
print(res)





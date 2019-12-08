

# n = int(input())
# Qs = input()
# dic = {}
# duiying = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M'}
# for i,c in enumerate(input().split()):
#     dic[duiying[i]] = int(c)
#
# res = float('-inf')
# for k in dic.keys():
#     if k in Qs:
#         continue
#     if dic[k] > res:
#         res = dic[k]
#         flag = k
#
# print(flag)

n,m,k = map(int,input().split())

dic = {}
seen = set()
butong_lau = 0
for i in range(k):
    u,v = map(int,input().split())
    dic[u] = v
    if v not in seen:
        seen.add(v)
        butong_lau += 1

no_lau = 0
for i in range(1,n+1):
    if i not in dic.keys():
        no_lau += 1

# 所有人都会语言
if no_lau == 0:
    print(butong_lau - 1)
# 有一些人会，有一些人不会
else:
    res = (no_lau - 1) + butong_lau-1
    print(res)






























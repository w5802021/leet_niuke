# n = int(input())
# ask = int(input())
#
# from collections import defaultdict
#
# look = defaultdict(list)
#
# for _ in range(ask):
#     a,b = map(int,input().split())
#     look[a].append(b)
# queue = []
#
# def dfs(look,k,x):
#     if x not in look and x not in look[k]:
#         return True
#     if x in look[k]:
#         return False
#     for i in look[x]:
#         a = dfs(look,k,i)
#         if a == False:
#             return a
#
# for k in look:
#     zhi = dfs(look,k,k)
#     if zhi == False:
#         print(0)
#         exit()
#
#
# for k in look:
#     queue.append(look[k])
#     for j in look[k]:
#         for i in queue:
#             if k in i and j in i:
#                 print(0)
#                 exit()
#
# print(1)

num_kids = int(input())
num_requests = int(input())

matrix_requests = [[0 for _ in range(num_kids)] for _ in range(num_kids)]

for i in range(num_requests):

    a,b = map(int,input().split(' '))
    matrix_requests[a - 1][b - 1] = 1
    matrix_requests[b - 1][a - 1] = 1
# 记录最大冲突的小孩数
max_sum = 0
# 记录没有任何冲突的小孩数量
count_zero = 0
for i in range(num_kids):
    _sum = sum(matrix_requests[i][0: i + 1])
    if _sum == 0:
        count_zero = count_zero + 1
    if _sum > max_sum:
        max_sum = _sum
if count_zero >= max_sum:
    print(1)
else:
    print(0)


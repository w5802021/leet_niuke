# n,m,d = map(int,input().split())
# spec = [int(c) for c in input().split()]
# parent = {}
# child = {}
# tmp = [int(c) for c in input().split()]
# for i,tm in enumerate(tmp):
#     parent[i+2] = tm
#     child[tm] = i+2

#第三行有n-1个整数，第i个数表示第i+1号结点的父亲结点的编号，同样在1-n之间。

# n,m,d = 6, 2, 3
# spec = [2, 1]
# parent = {2:3, 3:4, 4:5, 5:6, 6:1}
# child = {3:2, 4:3, 5:4, 6:5, 1:6}

# def get_dist(j,s):
#     def dfs_l(j,s,count):
#         if j == s:
#             return True,count
#         if j in parent.keys():
#             flag,a = dfs_l(parent[j], s, count+1)
#         else:
#             return False,0
#         return flag,a
#     def dfs_r(j,s,count):
#         if j == s:
#             return True,count
#         if j in child.keys():
#             flag,a = dfs_r(child[j], s, count+1)
#         else:
#             return False,0
#         return flag,a
#     if j == s:
#         return 0
#     else:
#         flag,dist =dfs_l(j,s,0)
#         if flag == True:
#             return dist
#         else:
#             flag, dist = dfs_r(j, s, 0)
#             return dist
#
# res = []
# # 包含特殊点本身
# for j in range(1,n+1):
#     count = 0
#     for s in spec:
#         if get_dist(j,s) <= d:
#             count += 1
#             continue
#         else:
#             break
#     if count == len(spec):
#         res.append(j)
# print(len(res))


# n,m,d = 6, 2, 3
# spec = [2, 1]
# parent = {2:3, 3:4, 4:5, 5:6, 6:1}
# child = {3:2, 4:3, 5:4, 6:5, 1:6}


n,m,d = map(int,input().split())
spec = [int(c) for c in input().split()]
lis = [int(c) for c in input().split()]
# nei为节点邻接表
nei = [[] for _ in range(n+1)]
for i in range(n-1):
    nei[i+2].append(lis[i])
    nei[lis[i]].append(i+2)

for i in range(1,n+1):
    nei[i].append(i)

flag = [0] * (n+1)
for i in range(m):
    dis = 1
    queue = [spec[i]]
    # 存储已经被遍历的节点
    see = set()
    while queue:
        size = len(queue)
        while size != 0 :
            tmp = queue.pop(0)

            for j in range(len(nei[tmp])):
                if nei[tmp][j] not in see:
                    see.add(nei[tmp][j])
                    flag[nei[tmp][j]] += 1

            for i in nei[tmp]:
                if i != tmp:
                    queue.append(i)
            size -= 1
        dis += 1
        if dis > d:
            break
#共有多少合适的点
count = 0
for i in range(len(flag)):
    if flag[i] == m:
        count += 1
print(count)
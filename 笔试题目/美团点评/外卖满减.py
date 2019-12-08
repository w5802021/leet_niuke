# n,x = map(int, input().split())
# pris = [int(c) for c in input().split()]
#
# # dp[i]满减为i元的情况下，最少的凑单价
# dp = [float('inf')] * (x + 1)
#
# for i in range(n):
#     for j in range(x,-1,-1):
#         if j > pris[i]:
#             dp[j] = min(dp[j],dp[j-pris[i]]+pris[i])
#         else:
#             dp[j] = min(dp[j],pris[i])
# print(dp[x])


#############贪心##################
#不能全过
N, X = [int(c) for c in input().split()]
costs = [int(c) for c in input().split()]

costs.sort()
# 列表是全局变量
ans = [float('inf')]
maked = set()
index = set()

# 贪心 +DFS + 剪枝
def dfs(cur):
    if cur >= X:
        ans[0] = min(ans[0], cur)
        return
    maked.add(cur)
    for i in range(N):
        if i not in index and costs[i] + cur not in maked:
            index.add(i)
            dfs(cur + costs[i])
            index.remove(i)

dfs(0)
print(ans[0])


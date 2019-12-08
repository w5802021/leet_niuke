n = int(input())
graph = []
for i in range(n):
    graph.append([int(c) for c in input().split()])
n = 4
graph =[[0 ,2 ,6 ,5],[2 ,0 ,4 ,4],[6 ,4 ,0 ,2],[5 ,4 ,2 ,0]]

V = 1 << (n - 1)  # 从左至右每一位二进制代表第i个城市是否被访问 如这里1左移3位——>1000代表，第一个城市被访问，而其他城市没有
dp = [[float("inf")] * V for i in range(n)]  # dp[i][j]:从节点i只经过集合j所有点再回到0点所需要的最小开销

# 初始化，代表从起始点i出发，其它各城市访问状态为‘0’
for i in range(n):
    dp[i][0] = graph[i][0]

# j为二进制数，判断位上对应的节点是否被访问
for j in range(1, V):
    # i表示起始点城市的节点编号
    for i in range(n):
        for k in range(1, n):  # 能不能先到k城市
            # 可以途径k
            if (j >> (k - 1) & 1) == 1:
                dp[i][j] = min(dp[i][j], graph[i][k] + dp[k][j ^ (1 << (k - 1))])

# 从0出发，经过所有点，再回到0的费用
print(dp[0][(1 << (n - 1)) - 1])


#################################################################################################

# n = int(input())
# # graph = []
# # for i in range(n):
# #     graph.append([int(c) for c in input().split()])

n = 4
graph =[[0 ,2 ,6 ,5],[2 ,0 ,4 ,4],[6 ,4 ,0 ,2],[5 ,4 ,2 ,0]]
# ‘10000’
stateNum = 1 << n
# dp[i][j]表示 以经过的城市状态为二进制数i开始，并且以j结尾的最短路径
dp = [[float('inf')] * n for _ in range(stateNum)]
dp[1][0] = 0

for i in range(1,stateNum):
    for j in range(n):
        # 如果该状态已经访问过
        if dp[i][j] != float('inf'):
            for k in range(1,n):
                # 如果没有访问过k，且从这里到k的距离小于原来的距离，则更新
                if (1 << k) & i == 0:
                    # i | (1 << k) 表示同时经过城市i和城市k（在后续遍历中若找到值比dp[i | (1 << k)][k]更小，则更新）
                    dp[i | (1 << k)][k] = min(dp[i | (1 << k)][k],dp[i][j] + graph[j][k])

res = float('inf')
# 因为确定是从北京出发，故而还需要加上graph[j][0]，并找出最短的路径
for i in range(1,n):
    res = min(res,dp[stateNum-1][i] + graph[i][0])
print(res)
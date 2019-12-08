from collections import defaultdict, deque
N = int(input())
graph = defaultdict(list)
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

queue = deque()
# 队列存储当前遍历到的节点，及走过的路径长度
queue.append((1, 0))
visit = set([1])
max_depth = 0
while queue:
    node, depth = queue.popleft()
    # 从该节点出发找到一条路径可以使得只经过结点一次，并且使得该路径最长
    max_depth = max(depth, max_depth)
    for child in graph[node]:
        if child not in visit:
            visit.add(child)
            queue.append((child, depth+1))
print(2*(N-1)-max_depth)



def gardenNoAdj(N, paths):
    res = [0] * N
    graph = [[] for _ in range(N)]
    for x, y in paths:
        graph[x - 1].append(y - 1)
        graph[y - 1].append(x - 1)
    for i in range(N):
        # seen将节点i的邻接节点的颜色存下
        seen = set(res[x] for x in graph[i])
        # 将邻接节点的花的种类剔除，随意选择剩下的一种花类型
        res[i] = ({1, 2, 3, 4} - seen).pop()
    return res

if __name__ == '__main__':
    N = 3
    paths = [[1, 2], [2, 3], [3, 1]]
    print(gardenNoAdj(N,paths))

def findMinHeightTrees(n, edges):
    '''
    方法：BFS
    思想：每次遍历树的所有叶节点，将本轮记录的所有叶节点从graph中删除，同时找到满足下一轮遍历的叶节点，循环反复直至遍历完至少n-1各节点
    输出此时记录的叶节点，即为最小高度树的叶节点
    :param n:
    :param edges:
    :return:
    '''
    if n == 1:return [0]
    graph = [[] for _ in range(n)]
    for x,y in edges:
        graph[x].append(y)
        graph[y].append(x)
    # 从叶节点往根节点遍历
    leaves = [i for i in range(n) if len(graph[i]) == 1]

    while n > 2:
        n -= len(leaves)
        next_leaves = []
        # 每次遍历所有的叶节点
        for i in leaves:
            j = graph[i].pop()
            # 将上一层的叶节点从graph中删除
            graph[j].remove(i)
            if len(graph[j]) == 1:next_leaves.append(j)
        leaves = next_leaves
    return leaves

if __name__ == '__main__':
    n = 4
    edges = [[1, 0], [1, 2], [1, 3]]
    print(findMinHeightTrees(n, edges))


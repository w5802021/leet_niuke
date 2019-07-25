import heapq as hp
import math

#####################################BFS########################################
#层序遍历
def BFS(graph,s):
    '''
    :param graph:
    :param s:表示第一个开始的节点
    :return:
    '''
    res = []
    queue = []
    queue.append(s)
    # 存储访问过哪些节点
    seen = set()
    seen.add(s)
    while queue:
        # 弹出队列第一个元素
        vertex = queue.pop(0)
        # vertex的邻接节点
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
        res.append(vertex)
    return res

########################################DFS#######################################
#前序遍历
def DFS(graph,s): #s表示第一个开始的节点
    res = []
    stack = []
    stack.append(s)

    seen = set()  # 存储访问过哪些节点
    seen.add(s)

    while stack:
        vertex = stack.pop()   #弹出队列最后一个元素
        nodes = graph[vertex]   #vertex的临接节点

        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)

        res.append(vertex)
    return res

######################################KFS###########################################

def KFS(graph,s): #s表示第一个开始的节点
    res = []
    queue = []
    queue.append(s)

    seen = set()  # 存储访问过哪些节点
    seen.add(s)

    parent = {s:None}

    while (len(queue) > 0):
        vertex = queue.pop(0)   #弹出队列第一个元素
        nodes = graph[vertex]   #vertex的邻接节点

        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
                parent[w] = vertex

        res.append(vertex)
    return res,parent

#####################################Dijkstra######################################################
def Dijkstra (graph,start):
    '''
    方法一：堆排实现
    :param graph:网络结构
    :param start:路径起点
    :return:
    '''
    res = []
    pqueue = []
    hp.heappush(pqueue,(0,start))
    # 存储访问过哪些节点
    seen = set()
    parent = {start:None}
    # 防止distance字典无初始化 导致后面distance[w]出现索引超界
    distance = {x: math.inf for x in graph if x != start}
    distance[start] = 0
    while pqueue:
        # 弹出队列第一个元素  小顶堆
        dist,vertex = hp.heappop(pqueue)
        # 当点在堆内弹出来的时候才能说是被看到
        seen.add(vertex)
        # vertex的邻接节点
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                if dist + graph[vertex][w] < distance[w]:
                    hp.heappush(pqueue,(dist+graph[vertex][w],w))
                    parent[w] = vertex
                    distance[w] = dist + graph[vertex][w]
        res.append(vertex)
    return parent,distance

if __name__ == '__main__':
    # graph = {'A': ['B', 'C'], 'B': ['A', 'C', 'D'], 'C': ['A', 'B', 'D', 'E'], 'D': ['B', 'C', 'E', 'F'],
    #          'E': ['C', 'D'], 'F': ['D']}
    # # print(BFS(graph,'E'))
    # print(DFS(graph, 'E'))
################################KFS###########################################  不带权重的最短路径
    # res,parent = KFS(graph, 'E')

    #######给定起始点‘E’，给定终点‘B’，求得最少走的节点数####
    # v = 'B'
    # Minpath = []
    # while v != None:
    #     Minpath.append(v)
    #     v = parent[v]
    # print(Minpath[::-1])

############################Dijistra########################################   带权重的最短路径
    graph_w = {'A': {'B':5, 'C':1}, 'B': {'A':5, 'C':2, 'D':1}, 'C': {'A':1, 'B':2, 'D':4, 'E':8},
               'D': {'B':1, 'C':4, 'E':3, 'F':6},
               'E': {'C':8, 'D':3}, 'F': {'D':6}}
    parent, distance = Dijkstra(graph_w,'A')
    v = 'D'
    Minpath = []
    while v != None:
        Minpath.append(v)
        v = parent[v]
    print(Minpath[::-1])      #输出从A--D的最短路径


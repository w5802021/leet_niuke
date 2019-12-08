import collections
import heapq as hq

def networkDelayTime(times, N, K):
    '''
    方法：堆排 + Dijkstra算法
    思路：求出源点K到其它每个节点的最短距离，当其中相距最远的节点距离已经接收到信号，则所有节点都收到了信号
    :param times:
    :param N:
    :param K:
    :return:
    '''
    pqueue = [(0, K)]
    dist = {}
    adj = collections.defaultdict(list)
    for u, v, w in times:
        adj[u].append((v, w))
    while pqueue:
        # 将下一节点距离上一节点最短距离的节点先弹出来
        time, node = hq.heappop(pqueue)
        if node not in dist:
            dist[node] = time
            for v, w in adj[node]:
                if v not in dist:
                    # 堆排（根据time + w 的值优先进行排序） 将最小值放在堆顶
                    hq.heappush(pqueue, (time + w, v))
    return max(dist.values()) if len(dist) == N else -1

def networkDelayTime1(times, N, K):
    '''
    方法：Dijkstra算法
    思路：求出源点K到其它每个节点的最短距离，当其中相距最远的节点距离已经接收到信号，则所有节点都收到了信号
    :param times:
    :param N:
    :param K:
    :return:
    '''
    graph = collections.defaultdict(list)
    for u,v,w in times:
        graph[u].append((v,w))
    dist = {x: float('inf') for x in range(1,N+1)}
    dist[K] = 0
    seen = [False] * (N+1)
    while True:
        can_node = -1
        can_dist = float('inf')
        for i in range(1,N+1):
            if not seen[i] and dist[i] < can_dist:
                can_dist = dist[i]
                can_node = i
        if can_node < 0:break
        seen[can_node] = True
        for v,w in graph[can_node]:
            dist[v] = min(dist[v],dist[can_node] + w)
    return max(dist.values()) if max(dist.values()) < float('inf') else -1


if __name__ == '__main__':
    times = [[2,3,1],[2,1,1],[3,4,1]]
    N = 4
    K = 2
    print(networkDelayTime1(times, N, K))
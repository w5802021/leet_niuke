def canFinish(numCourses, prerequisites):
    '''
    方法一：DFS
    :param numCourses:
    :param prerequisites:
    :return:
    '''
    ###初始化逆邻接表
    graph = [[] for _ in range(numCourses)]
    for x,y in prerequisites:
        graph[x].append(y)
    ###visit记录节点的访问状态
    ### 0表示节点未访问，1表示节点已经访问，-1表示节点正在被访问
    visit = [0 for _ in range(numCourses)]
    ###DFS遍历
    def dfs(i):
        if visit[i] == -1:
            return False
        if visit[i] == 1:
            return True
        ###如果节点i正在被访问，则节点i赋值为-1
        ###DFS遍历邻接点，如果邻接点已经被遍历，则为有环图
        visit[i] = -1
        for j in graph[i]:
            if not dfs(j):
                return False
        ###如果节点i被访问期间其邻接节点且为无环图，则节点i赋值为1
        visit[i] = 1
        return True
    ###以图的每个节点为起始点做dfs遍历
    for i in range(numCourses):
        if not dfs(i):
            return False
    return True

def canFinish1(numCourses, prerequisites):
    '''
    方法二：（BFS的拓扑排序） Kahn算法 AVO网   ---这里采用队列进行bfs的拓扑排序  采用栈可进行dfs的拓扑排序
    用途：拓扑排序的结果不唯一。拓扑排序还可以用于检测一个有向图是否有环
    关键辅助结构：
        1、邻接表：通过结点的索引，我们能够得到这个结点的后继结点；
        2、入度数组：通过结点的索引，我们能够得到指向这个结点的结点个数。
    :param numCourses:
    :param prerequisites:
    :return:
    '''
    #课程的长度
    clen = len(prerequisites)
    if clen == 0:
        # 没有课程，当然可以完成课程的学习
        return True
    # 入度数组，一开始全部为 0
    in_degrees = [0 for _ in range(numCourses)]
    # 邻接表
    adj = [set() for _ in range(numCourses)]
    # 想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
    # [0,1] 表示1在先，0在后
    # 注意：邻接表存放的是后继successor结点的集合
    for second, first in prerequisites:
        in_degrees[second] += 1
        adj[first].add(second)
    queue = []
    # 首先遍历一遍，把所有入度为 0 的结点加入queue
    for i in range(numCourses):
        if in_degrees[i] == 0:
            queue.append(i)
    #counter记录能完成的课程数
    counter = 0
    while queue:
        top = queue.pop(0)
        counter += 1
        for successor in adj[top]:
            in_degrees[successor] -= 1
            if in_degrees[successor] == 0:
                queue.append(successor)
    return counter == numCourses

#############################################210###############################################两种方法同上
def findOrder(numCourses, prerequisites):
    '''
    方法一：bfs拓扑排序
    :param numCourses:
    :param prerequisites:
    :return:
    '''
    clen = len(prerequisites)
    if clen == 0:
        ###不同
        return [i for i in range(numCourses)]

    in_degrees = [0 for _ in range(numCourses)]
    adj = [set() for _ in range(numCourses)]


    for second, first in prerequisites:
        in_degrees[second] += 1
        adj[first].add(second)
    #增加res
    res = []
    queue = []
    for i in range(numCourses):
        if in_degrees[i] == 0:
            queue.append(i)
    while queue:
        top = queue.pop(0)
        res.append(top)
        for successor in adj[top]:
            in_degrees[successor] -= 1
            if in_degrees[successor] == 0:
                queue.append(successor)
    #不同
    if len(res) != numCourses:
        return []
    return res

def findOrder1(numCourses, prerequisites):
    '''
    方法一：dfs
    :param numCourses:
    :param prerequisites:
    :return:
    '''
    if len(prerequisites) == 0:
        ###不同
        return [i for i in range(numCourses)]
    graph = [set() for _ in range(numCourses)]
    for x, y in prerequisites:
        graph[x].add(y)
    visit = [0 for _ in range(numCourses)]
    #保存结果
    res = []
    def dfs(i):
        if visit[i] == -1:
            return False
        if visit[i] == 1:
            return True
        visit[i] = -1
        for j in graph[i]:
            if not dfs(j):
                return False
        visit[i] = 1
        #此处将节点添加入结果列表
        res.append(i)
        return True

    for i in range(numCourses):
        if not dfs(i):
            return []
    return res

if __name__ == '__main__':
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    print(findOrder1(numCourses,prerequisites))


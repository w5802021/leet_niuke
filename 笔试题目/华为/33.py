
grid = input()
ee = []
tmp = []
count = 0
hang = 0
for i in grid:
    if i == '0' or i == '1':
        count+= 1
        tmp.append(int(i))
    if i == ']' and len(tmp) != 0:
        ee.append(tmp)
        tmp = []
        lie = count
        count = 0
print(ee)
# ee = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
graph = []
for i in range(len(ee)):
    for j in range(len(ee[0])):
        if ee[i][j] == 1:
            graph.append([i,j])
n = lie
def canFinish(numCourses, prerequisites):

    # 课程的长度
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
    # counter记录能完成的课程数
    counter = 0
    while queue:
        top = queue.pop(0)
        counter += 1
        for successor in adj[top]:
            in_degrees[successor] -= 1
            if in_degrees[successor] == 0:
                queue.append(successor)
    return counter == numCourses
if canFinish(n, graph):
    print('0')
else:
    print('1')



# ee = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
# vv = [[0, 0, 0, 1, 0], [1, 0, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0]]


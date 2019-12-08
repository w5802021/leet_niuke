# from collections import defaultdict
# def main(n,m,task_t,depend):
#     '''
#     BFS方法
#     :param n:
#     :param m:
#     :param task_t:
#     :param depend:
#     :return:
#     '''
#
#     task_dict = { i:x for i,x in enumerate(task_t)}
#     dic = defaultdict(list)
#     for i in range(m):
#         dic[depend[i][1]-1].append(depend[i][0]-1)
#     res = []
#     # 初始化任务完成状态
#     remain = list(task_dict.keys())
#     while remain:
#         level = []
#         # 找到所有能够执行的任务
#         for i in remain:
#             if i not in task_dict or i not in dic:
#                 level.append(i)
#         # 将level中的任务按执行时间降序排列
#         level.sort(key = lambda x:task_dict[x])
#         for i in level:
#             res.append(i)
#             remain.remove(i)
#             # 删除已完成任务的依赖
#             for k in dic.copy():
#                 if i in dic[k]:
#                     dic[k].remove(i)
#                     if len(dic[k]) == 0:
#                         del dic[k]
#
#     for i in res:
#         print(i+1,end = ' ')
#
# if __name__ == '__main__':
#     n, m = 5,6
#     task_t = [1,2,1,1,1]
#     depend = [[1,2],[1,3],[1,4],[2,5],[3,5],[4,5]]
#     main(n,m,task_t,depend)

# 优先队列法
from collections import defaultdict
import heapq

class Node(object):
    def __init__(self, time, l, index):
        self.time = time
        self.l = l
        self.index = index

    def __lt__(self, other):
        if self.time < other.time:
            return True
        elif self.time == other.time:
            return self.index < other.index
        else:
            return False

N, M = map(int, input().split())
times = list(map(int, input().split()))
d = defaultdict(set)
l = []
# heapq.heapify(l)
for i in range(M):
    tmp = list(map(int, input().split()))
    for e in tmp[:-1]:
        d[tmp[-1]].add(e)

for i in range(N):
    # print(times[i], d[i+1],i+1)
    heapq.heappush(l, Node(times[i], d[i + 1], i + 1))

res = []
while len(l) > 0:
    tmp = []
    node = None
    # 找出一个入度为0的结点开始
    while len(l) > 0:
        node = heapq.heappop(l)
        if len(node.l) > 0:
            tmp.append(node)
        else:
            res.append(node.index)
            break
    for e in tmp:
        heapq.heappush(l, e)

    # 做完node这个任务，更新后续任务的依赖关系，即更新后续任务node.l的值
    if node != None:
        for i in range(len(l)):
            if node.index in l[i].l:
                l[i].l.remove(node.index)
for e in res:
    print(e, end=" ")




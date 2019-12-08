from queue import PriorityQueue as pque
## 优先队列接口

'''
#向队列中添加元素
PriorityQueue.put(item[, block[, timeout]])
#从队列中获取元素
PriorityQueue.get([block[, timeout]])
#队列判空
PriorityQueue.empty()
#队列大小
PriorityQueue.qsize()
'''


def PriorityQueue_int():
    que = pque()
    que.put(10)
    que.put(1)
    que.put(5)
    while not que.empty():
        print (que.get())

def PriorityQueue_tuple():
    que = pque()
    que.put((10,'ten'))
    que.put((1,'one'))
    que.put((10/2,'five'))
    while not que.empty():
        print (que.get())

class tup(object):
    def __init__(self,priority,description):
        self.priority = priority
        self.description = description
    #下面两个方法重写一个就可以了
    def __lt__(self,other):#operator <
        return self.priority > other.priority


    # def __cmp__(self,other):
    #     #call global(builtin) function cmp for int
    #     return cmp(self.priority,other.priority)
    # def __str__(self):
    #     return '(' + str(self.priority)+',\'' + self.description + '\')'

def PriorityQueue_class():
    que = pque()
    skill5 = tup(5,'proficient')
    skill6 = tup(6,'proficient6')
    que.put(skill6)
    que.put(tup(5,'proficient'))
    que.put(tup(10,'expert'))
    que.put(tup(1,'novice'))
    while not que.empty():
        print (que.get())

if __name__ == '__main__':
    PriorityQueue_class()


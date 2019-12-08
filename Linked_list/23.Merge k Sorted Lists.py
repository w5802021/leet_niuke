from Linked_list import linkedlist_operate
import heapq

class LNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

class tup:
    def __init__(self,v,n):
        self.v = v
        self.n = n
    #下面两个方法重写一个就可以了
    def __lt__(self,other):#operator <
        return self.v < other.v

def mergeKLists(nums):
    '''
    方法：优先队列法
    :param nums:
    :return:
    '''
    dummy = cur = LNode(0)
    queue = []

    for l in nums:
        if l:
            # 刚开始初始化一个堆为列表中每个链表的头结点
            heapq.heappush(queue,tup(l.val,l))
    while queue:
        node = heapq.heappop(queue)
        cur.next = node.n
        cur = cur.next
        newnode = node.n.next
        if newnode:
            heapq.heappush(queue, tup(newnode.val, newnode))
    return dummy.next

def mergeKLists1(lists):
    '''
    方法：分治
    这题的出题目的与分治的思想最为接近
    :param lists:
    :return:
    '''
    if not lists:
        return
    n = len(lists)
    return merge(lists,0,n-1)

def merge(lists,left,right):
    # 递归划分k个链表
    if left == right:
        return lists[left]
    mid = left + (right - left)//2
    l1 = merge(lists,left,mid)
    l2 = merge(lists,mid + 1,right)
    return mergetwolists(l1,l2)

def mergetwolists(l1,l2):
    # 两两合并排序后的链表值
    if not l1: return l2
    if not l2: return l1

    if l1.val < l2.val:
        # l1的当前值后接（l1.next与l2比较大小之后得到的值）
        l1.next = mergetwolists(l1.next,l2)
        return l1
    else:
        l2.next = mergetwolists(l1,l2.next)
        return l2


if __name__ == '__main__':
    l1 = [1,4,5]
    l2 = [1,3,4]
    l3 = [2,6]
    llist = linkedlist_operate.LinkList()
    cur1 = llist.initList(l1)
    cur2 = llist.initList(l2)
    cur3 = llist.initList(l3)
    res = mergeKLists1([cur1.next, cur2.next, cur3.next])
    llist.outll(res)
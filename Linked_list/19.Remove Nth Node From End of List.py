from Linked_list import linkedlist_operate

class LNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

def removeNthFromEnd(head, n):
    dum = LNode(None)
    # dum初始化技巧
    dum.next = head
    count = 0
    while head:
        count += 1
        head = head.next
    # 这里：新head定位在原head之前，因为一般在(删除点的pre）做操作
    first = dum
    # 处理删除倒数数，定位尾端边界  不要在循环中处理，易忽略边界问题
    m = count - n
    while m > 0:
        first = first.next
        m -= 1
    first.next = first.next.next

    return dum.next

def removeNthFromEnd1(head, n):
    '''
    思路：定义两个相同的链表slow、fast，先让快指针先走n步，
         随后，slow、fast指针同时向后遍历直到fast指针到达链表尾部
         此时slow指向的是倒数第n+1个节点，将其next接到倒数第n-1个节点即可
    :param head:
    :param n:
    :return:
    '''
    slow,fast = head,head
    for i in range(n):
        # 若n超出链表的长度，则删除第一个节点
        if fast.next == None:
            return head.next
        fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head

if __name__ == '__main__':
    l1 = [2,4,3,4,5,6]
    n = 3
    llist = linkedlist_operate.LinkList()
    cur1 = llist.initList(l1)
    res = removeNthFromEnd1(cur1.next, n)
    print('输出')
    llist.outll(res)
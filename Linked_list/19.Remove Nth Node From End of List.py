from Linked_list import linkedlist_operate

class LNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

def removeNthFromEnd(head, n):
    dum = LNode(None)
    dum.next = head          #dum初始化技巧
    count = 0
    while head:
        count += 1
        head = head.next
    first = dum                #这里：新head定位在原head之前，因为一般在(删除点的pre）做操作

    m = count - n             #处理删除倒数数，定位尾端边界  不要在循环中处理，易忽略边界问题
    while m > 0:
        first = first.next
        m -= 1
    first.next = first.next.next

    return dum.next

def removeNthFromEnd1(head, n):
    dum = LNode(0)
    dum.next = head
    first,second = dum,dum
    for i in range(n+1):
        first = first.next

    while first:
        first = first.next
        second = second.next
    second.next = second.next.next

    return dum.next

if __name__ == '__main__':
    l1 = [2,4,3,4,5,6]
    n = 3
    llist = linkedlist_operate.LinkList()
    cur1 = llist.initList(l1)
    res = removeNthFromEnd1(cur1.next, n)
    print('输出')
    llist.outll(res)
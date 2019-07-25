from Linked_list import linkedlist_operate

class LNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

def removeElements(head, val):   #思路类似链表移除重复的数
    dum = LNode(0)
    dum.next = head
    cur = dum

    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return dum.next

if __name__ == '__main__':
    l = [1,2,3,4,5,4]

    llist = linkedlist_operate.LinkList()
    cur = llist.initList(l)
    val = 4
    res = removeElements(cur.next,val)

    print('输出')
    llist.outll(res)

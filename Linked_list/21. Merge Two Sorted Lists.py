from Linked_list import linkedlist_operate

class LNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    dum = cur = LNode(None)

    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dum.next

if __name__ == '__main__':
    l1 = [1,2,4]
    l2 = [1,3,4]
    llist = linkedlist_operate.LinkList()
    cur1 = llist.initList(l1)
    cur2 = llist.initList(l2)
    res = mergeTwoLists(cur1.next, cur2.next)
    print('输出')
    llist.outll(res)
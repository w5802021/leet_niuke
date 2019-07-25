from Linked_list import linkedlist_operate

class LNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

def swapPairs(head):
    if not head or not head.next:
        return head
    nex = head.next
    head.next = swapPairs(nex.next)
    nex.next = head
    return nex

def swapPairs1(head):
    if not head or not head.next:
        return head
    res = LNode(0)
    res.next = head
    pre = res
    cur = res.next

    while cur and cur.next:
        pre.next = cur.next
        cur.next = cur.next.next  #这一步把cur.next移到pre.next的节点清除
        pre.next.next = cur

        pre = cur
        cur = cur.next

    return res.next





if __name__ == '__main__':
    l = [1,2,3,4,5]

    llist = linkedlist_operate.LinkList()
    cur = llist.initList(l)

    res = swapPairs1(cur.next)

    print('输出')
    llist.outll(res)
from Linked_list import linkedlist_operate

class LNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

def swapPairs(head):
    '''
    思路：处理链表中的三个节点三个节点：head、head.next、未处理完的链表部分
         交换两节点head、head.next
    :param head:
    :return:
    '''
    if not head or not head.next:
        return head
    nex = head.next
    # 由于是从左往右递归
    # swapPairs(nex.next)处理右边节点后面的未完成的链表部分
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
    llist.outll(res)
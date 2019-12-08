from Linked_list import linkedlist_operate

class LNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

def oddEvenList(head):
    if head == None or head.next == None:
        return head
    # 节点编号为奇数
    odd = head
    # 节点编号为偶数
    even = head.next
    evenhead = even

    while even and even.next:
        odd.next = even.next
        # 跳到下一个奇数编号节点
        odd = odd.next
        even.next = odd.next
        # 跳到下一个偶数编号节点
        even = even.next
    # 奇数编号子串与偶数编号子串连接
    odd.next = evenhead
    return head

if __name__ == '__main__':
    l = [1,2,3,4,5]
    llist = linkedlist_operate.LinkList()
    cur = llist.initList(l)
    res = oddEvenList(cur.next)
    llist.outll(res)
from Linked_list import linkedlist_operate    #链表题规范化输入输出


class LNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

def sortList(head):
    l = []
    while head:
        l.append(head.val)
        head = head.next
    l.sort()
    return l

##############################################################    链表的归并排序
# 效率不高 ，不知道什么原因
def merge(l,r):
    dum = cur = LNode(0)
    while l and r:
        if l.val < r.val:
            cur.next,l = l,l.next
        else:
            cur.next,r = r,r.next

        cur = cur.next

    cur.next = l or r
    return dum.next


def sortList1(head):
    if not head or not head.next:
        return head

    slow,fast = head,head

    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next                         #找到中点
    slow.next = None
    return merge(*map(sortList1,(head,mid)))   #递归分裂 再合并



if __name__ == '__main__':
    l = [1, 8, 3, 4, 5]

    llist = linkedlist_operate.LinkList()
    cur = llist.initList(l)
    print('输入')
    llist.outll(cur)

    res = sortList1(cur.next)

    print('输出')
    llist.outll(res)
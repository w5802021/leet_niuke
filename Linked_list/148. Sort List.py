from Linked_list import linkedlist_operate    #链表题规范化输入输出

class LNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

# def sortList(head):
#     l = []
#     while head:
#         l.append(head.val)
#         head = head.next
#     l.sort()
#     return l

##############################################################
# 链表的归并排序

def sortleft(head):
    def merge(left, right):
        dum = cur = LNode(0)
        while left and right:
            #较小的数接在cur后面
            if left.val < right.val:
                cur.next= left
                left = left.next
            else:
                cur.next= right
                right = right.next
            cur = cur.next
        # 剩下的数接在cur后面
        cur.next = left or right
        return dum.next

    if not head or not head.next:
        return head
    fast,slow = head,head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    mid = slow.next
    slow.next = None

    left = sortleft(head)
    right = sortleft(mid)
    sorted = merge(left, right)

    return sorted

if __name__ == '__main__':
    l = [1, 8, 3, 4, 5]

    llist = linkedlist_operate.LinkList()
    cur = llist.initList(l)
    print('输入')
    llist.outll(cur)

    res = sortleft(cur.next)

    print('输出')
    llist.outll(res)
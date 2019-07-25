from Linked_list import linkedlist_operate    #链表题规范化输入输出


class LNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

def reverseList(head):
    l = []
    while head:
        l.append(head.val)
        head = head.next
    lt = l[::-1]                                      #列表
    llist = linkedlist_operate.LinkList()
    cur = llist.initList(lt)                          #将列表转化为链表输出
    return cur.next

def reverseList1(head):

    p, rev = head, None
    while p:
        rev, rev.next, p = p, rev, p.next
    return rev


def reverseList2(head):
    if head == None or head.next == None:
        return
    pre,cur,next = None,None,None

    cur = head.next
    next = cur.next
    cur.next = None
    pre = cur
    cur = next

    while cur.next != None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = cur.next
        cur = next

    cur.next = pre
    head.next = cur

if __name__ == '__main__':
    l = [1, 8, 3, 4, 5]

    llist = linkedlist_operate.LinkList()
    cur = llist.initList(l)
    print('输入')
    llist.outll(cur)

    res = reverseList1(cur)

    print('输出')
    llist.outll(res)





    # head = LNode()
    # head.next = None
    # tmp = None
    # cur = head
    #
    # for i in l:
    #     tmp = LNode()
    #     tmp.val = i
    #     tmp.next = None
    #     cur.next = tmp
    #     cur = tmp
    # print('输入')
    # cur = head
    # outll(cur)
    #
    # print('输出：')
    # res = reverseList1(head)
    # outll(res)





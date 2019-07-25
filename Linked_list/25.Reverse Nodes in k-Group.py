from Linked_list import linkedlist_operate

class LNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None


def reverse( head):
    p, rev = head, None
    while p:
        rev, rev.next, p = p, rev, p.next
    return rev

def reverseKGroup(head, k):

    if head == None or k < 2:
        return
    count = k
    pre = None
    cur = head
    while count:
        if cur:
            cur.next,pre,cur = pre,cur,cur.next    #进入一个节点，即将它放到最前面
            count -= 1
            if count == 0:
                head.next = reverseKGroup(cur,k)  #将k一组反转后的数列接到‘head’后面，这个head是每次迭代
        else:
            head = reverse(pre)
            return head
    return pre


if __name__ == '__main__':
    l = [1,2,3,4,5]

    llist = linkedlist_operate.LinkList()
    cur = llist.initList(l)
    k = 2
    res = reverseKGroup(cur.next,k)

    print('输出')
    llist.outll(res)

from Linked_list import linkedlist_operate

class LNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

def deleteDuplicates(head):
    cur = head
    while cur and cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head

def deleteDuplicates1(head):
    dum = cur = head
    while cur and cur.next:
        if cur.val == cur.next.val:
            cur = cur.next.next
            head = cur
            head = head.next

        else:
            cur = cur.next
    return dum

###########################82       II#####
def deleteDuplicates2(head):
    dum = pre = LNode(0)

    dum.next = head

    while head and head.next:       #这里将head看成当前值
        if head.val == head.next.val:
            # 若存在多个重复值，则都跳过
            while head and head.next and head.val == head.next.val:
                head = head.next
            head = head.next
            pre.next = head
        else:
            pre = pre.next          #没有重复节点时，pre的位置对应右移一步
            head = head.next
    return dum.next

#############################如何对无序的链表删除重复项######################   拓展
def deleteDuplicates3(head):
    '''
    哈希表最小的时间复杂度
    :param head:
    :return:
    '''
    has = set()
    dum = head
    while head and head.next:
        if head.val not in has:
            has.add(head.val)
            head = head.next
        else:                              #删除单前节点操作
            head.val = head.next.val
            head.next = head.next.next

    if head.val in has:
        head.val = None
    else:
        head = head.next
    return dum

if __name__ == '__main__':
    l1 = [8,9,7,4,3,2,1,8,4,6,5,4,3,1,10]
    l2 = [1,1,2,3,3]

    llist = linkedlist_operate.LinkList()
    cur1 = llist.initList(l1)
    cur2 = llist.initList(l2)

    res = deleteDuplicates2(cur2.next)

    print('输出')
    llist.outll(res)
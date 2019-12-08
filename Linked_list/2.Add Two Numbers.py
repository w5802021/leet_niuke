from Linked_list import linkedlist_operate

class LNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2, carry=0):
    '''

    :param l1:
    :param l2:
    :param carry: carry判断两数之和是否有进位
    :return:
    '''
    # l1,l2输入都为空
    # 有进位要返回进位
    if not l1 and not l2:
        return LNode(1) if carry else None
    # l1,l2取完，则后续其值赋为0
    l1 = l1 or LNode(0)
    l2 = l2 or LNode(0)

    val = l1.val + l2.val + carry
    # 链表l1存储两数之和
    l1.val = val % 10
    l1.next = addTwoNumbers(l1.next,l2.next,val > 9)
    return l1    #

def addTwoNumbers1(l1, l2):
    res = LNode(0)

    tmp = res

    carry = 0
    while l1 or l2:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        summ = x + y + carry
        tmp.next = LNode(summ % 10)
        carry = summ // 10
        tmp = tmp.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    if carry > 0:
        tmp.next = LNode(1)
    return res.next

if __name__ == '__main__':
    l1 = [2,4,3]
    l2 = [5,6,4]
    llist = linkedlist_operate.LinkList()
    cur1 = llist.initList(l1)
    cur2 = llist.initList(l2)
    res = addTwoNumbers(cur1.next, cur2.next)
    llist.outll(res)
from Linked_list import linkedlist_operate

class LNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2, carry=0):              # carry判断两数之和是否有进位
    if not(l1 or l2):                            #l1,l2输入都为空
        return LNode(1) if carry else None       #有进位要返回进位

    l1 ,l2 = l1 or LNode(0),l2 or LNode(0)       # l1,l2取完，则后续其值赋为0

    val = l1.val + l2.val + carry

    l1.val, l1.next = val % 10, addTwoNumbers(l1.next,l2.next,val > 9)  #链表l1存储两数之和

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
    res = addTwoNumbers1(cur1.next, cur2.next)
    print('输出')
    llist.outll(res)
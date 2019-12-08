from Linked_list import linkedlist_operate

class LNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

def reverseList1(head):
    p, rev = head, None
    while p:
        rev, rev.next, p = p, rev, p.next
    return rev

def reverseList(head):
    pre = reverse_head = None
    while head:
        nextNode = head.next
        if not nextNode:reverse_head = head
        head.next = pre
        pre = head
        head = nextNode
    return reverse_head

def reorderList(head):
    '''
    思路：1.找到中点
          2.逆转后半部分
          3.拼接前半部分和逆转过的后半部分
    :param head:
    :return:
    '''
    if not head or not head.next:
        return None

    fast,slow = head,head

    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

    rev = slow.next       # 数组长度为奇数 中间的数一般放最后
    slow.next = None      # 为了使前半部分 被切分出来
    rev = reverseList1(rev) #将数组后半部分反转

    first = head #前半部分
    second = rev #后半部分                    #链表长为奇数，first比second长度大1，偶数则相等

    # 里面的节点交换顺序要理清
    while first and second:
        tmp1 = first.next
        tmp2 = second.next
        first.next = second
        second.next = tmp1
        first,second = tmp1,tmp2

    return head

if __name__ == '__main__':
    l = [1,2,3,4,5]

    llist = linkedlist_operate.LinkList()
    cur = llist.initList(l)


    res = reorderList(cur.next)

    print('输出')
    llist.outll(res)



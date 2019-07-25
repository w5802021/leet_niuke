from Linked_list import linkedlist_operate    #链表题规范化输入输出


class LNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

def reverseBetween(head,m,n):

    l1 = []
    l2 = []
    l3 = []
    count = 0
    while head:
        count += 1
        if m <= count <= n:
            l2.append(head.val)
        elif count < m:
            l1.append(head.val)
        else:
            l3.append(head.val)
        head = head.next
    l1.extend(l2[::-1]).extend(l3)
    return l1

def reverseBetween1(head,m,n):          #迭代版本

    dummy = pre = LNode(0)
    dummy.next = head

    for i in range(m - 1):
        pre = pre.next
    cur = pre.next

    for i in range(n - m):   #cur:当前节点  pre：上一个节点  tmp:下一个节点
        tmp = cur.next                 #保存cur.next为后面做交换
        cur.next = tmp.next            #tmp.next后的数接到cur后，使得pre.next中去除tmp位置元素
        tmp.next = pre.next
        pre.next = tmp                 #将cur.next调换到最前面

    return dummy.next                   #核心思路：每次循环将cur.next和（pre.next--cur这个整体作交换）

def reverseBetween2(head,m,n):        #迭代版本   。。。。待理解
    if not head:
        return None

    left, right = head, head
    stop = False

    def recurseAndReverse(right, m, n):
        nonlocal left, stop

        # base case. Don't proceed any further
        if n == 1:
            return

        # Keep moving the right pointer one step forward until (n == 1)
        right = right.next

        # Keep moving left pointer to the right until we reach the proper node
        # from where the reversal is to start.
        if m > 1:
            left = left.next

        # Recurse with m and n reduced.
        recurseAndReverse(right, m - 1, n - 1)

        # In case both the pointers cross each other or become equal, we
        # stop i.e. don't swap data any further. We are done reversing at this
        # point.
        if left == right or right.next == left:
            stop = True
            # Until the boolean stop is false, swap data between the two pointers
        if not stop:
            left.val, right.val = right.val, left.val

            # Move left one step to the right.
            # The right pointer moves one step back via backtracking.
            left = left.next

    recurseAndReverse(right, m, n)
    return head

if __name__ == '__main__':
    l = [1, 8, 3, 4, 5]

    llist = linkedlist_operate.LinkList()
    cur = llist.initList(l)
    print('输入')
    llist.outll(cur)
    m=2
    n=5

    res = reverseBetween1(cur.next,m,n)

    print('输出')
    llist.outll(res)
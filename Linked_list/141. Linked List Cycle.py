#
#如果列表中不存在环，最终快指针将会最先到达尾部，此时我们可以返回 false。

#现在考虑一个环形链表，把慢指针和快指针想象成两个在环形赛道上跑步的运动员（分别称之为慢跑者与快跑者）。而快跑者最终一定会追上慢跑者。这是为什么呢？
#考虑下面这种情况（记作情况 A）- 假如快跑者只落后慢跑者一步，在下一次迭代中，它们就会分别跑了一步或两步并相遇。
#其他情况又会怎样呢？例如，我们没有考虑快跑者在慢跑者之后两步或三步的情况。但其实不难想到，因为在下一次或者下下次迭代后，又会变成上面提到的情况 A。
#

from Linked_list import linkedlist_operate

class LNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

def hasCycle(head):               #快慢指针法  （有环则两指针必定相遇）

    if head is None or head.next is None:
        return None

    slow ,fast = head ,head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        while slow == fast:
            return True
    return False

def hasCycle1(head):              #哈希表  存放链表节点的地址    （相同思路：将访问过的节点都赋上同一元素值，空间复杂度缩小）
    has = set()

    while head:
        if id(head) in has:
            return True
        has.add(id(head))
        head = head.next
    return False

if __name__ == '__main__':
    l1 = [4,1,8,4,5]

    llist = linkedlist_operate.LinkList()
    cur = llist.initList(l1)

    res = hasCycle(cur.next)

    print('输出')
    print(res)
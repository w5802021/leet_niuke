from Linked_list import linkedlist_operate

class LNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

def detectCycle(head):
    if not head or not head.next:
        return None

    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # 找到链表中入环的第一个结点
            # 这里注意，slow与fast指针第一次相遇的结点不一定是入口节点
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None

def detectCycle1(head):   ###哈希##

    l = set()
    while head:
        if head in l:
            return head
        l.add(head)
        head = head.next

    return head

if __name__ == '__main__':
    l1 = [4,1,8,4,5]

    llist = linkedlist_operate.LinkList()
    cur = llist.initList(l1)

    res = detectCycle(cur.next)

    print('输出')
    print(res)
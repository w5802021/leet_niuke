from Linked_list import linkedlist_operate

class LNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

def detectCycle(head):
    if head is None or head.next is None:
        return None

    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            slow = head
            while slow is not fast:
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
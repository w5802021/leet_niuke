from Linked_list import linkedlist_operate
from Tree import operate_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class LNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

def middleNode(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def sortedListToBST(head):
    if not head:
        return None
    if not head.next:
        return TreeNode(head.val)
    prevPtr = None
    slow, fast = head, head
    while fast and fast.next:
        prevPtr = slow
        fast = fast.next.next
        slow = slow.next
    tmp = slow
    #
    if prevPtr:
        prevPtr.next = None
    root = TreeNode(tmp.val)
    root.left = sortedListToBST(head)
    root.right = sortedListToBST(tmp.next)
    return root

if __name__ == '__main__':
    l = [1,2,3,4,5]

    llist = linkedlist_operate.LinkList()
    cur = llist.initList(l)


    res = sortedListToBST(cur.next)

    print('输出')
    llist.outll(res)
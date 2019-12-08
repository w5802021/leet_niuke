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

def sortedListToBST(head):
    if not head:
        return None
    if not head.next:
        return TreeNode(head.val)
    # 这里取得中点要靠前，所以让fast先走一步
    slow, fast = head, head.next.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    mid = slow.next
    slow.next = None

    root = TreeNode(mid.val)
    root.left = sortedListToBST(head)
    root.right = sortedListToBST(mid.next)
    return root

if __name__ == '__main__':
    l = [1,2,3,4,5]

    llist = linkedlist_operate.LinkList()
    cur = llist.initList(l)
    res = sortedListToBST(cur.next)
    tree = operate_tree.Tree()
    print(tree.levelOrder(res))

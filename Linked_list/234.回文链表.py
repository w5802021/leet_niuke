from Linked_list import linkedlist_operate

class LNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

def reverseList1(head):
    # 初始化res=None代表反转链表的尾结点
    p, res = head, None
    while p:
        p,res,res.next=p.next,p,res
    return res

def isPalindrome(head):

    if not head or not head.next:
        return True
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # 链表长度为奇数时
    if fast:
        slow = slow.next
    p2 = reverseList1(slow)
    p1 = head
    while p1 and p2:
        if p1.val != p2.val:
            return False
        p1 = p1.next
        p2 = p2.next
    return True

if __name__ == '__main__':
    l = [1,2,2,1]
    llist = linkedlist_operate.LinkList()
    cur = llist.initList(l)
    print(isPalindrome(cur.next))

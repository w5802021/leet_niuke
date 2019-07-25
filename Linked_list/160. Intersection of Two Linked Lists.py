# -*- coding: utf-8 -*-
from Linked_list import linkedlist_operate

class LNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

def getIntersectionNode(headA, headB):     ###本题是要求交集，理解题意，不是求一个公共交点
    if headA is None or headB is None:
        return None

    pa = headA
    pb = headB

    while pa is not pb:    #?本地通不过出不来结果

        pa = headB if pa is None else pa.next
        pb = headA if pb is None else pb.next

    return pa

def getIntersectionNode1(headA, headB):     ###？？？
    if (headA is None) | (headB is None):
        return None
    last = headB

    while last.next:
        last = last.next
    last.next = headB

    slow, fast = headA, headA

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = headA
            while slow != fast:
                slow = slow.next
                fast = fast.next
            last.next = None
            return slow
    last.next = None
    return None

def getIntersectionNode2( headA, headB):    #哈希表法

    has = set()

    while headA:
        has.add(headA)
        headA = headA.next
    while headB:
        if headB in has:
            return headB
        headB = headB.next
    return None

if __name__ == '__main__':
    l1 = [4,1,8,4,5]
    l2 = [5,0,1,8,4,5]

    llist = linkedlist_operate.LinkList()
    cur1 = llist.initList(l1)
    cur2 = llist.initList(l2)

    res = getIntersectionNode2(cur1.next,cur2.next)

    print('输出')
    llist.outll(res)
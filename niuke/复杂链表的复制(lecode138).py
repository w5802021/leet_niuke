class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    '''
    dfs bfs 迭代
    '''
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here

        if not pHead:
            return None

        dummy = pHead
        # 在链表每个结点后复制结点
        while dummy:
            dummynext = dummy.next
            copynode = RandomListNode(dummy.label)
            copynode.next = dummynext
            dummy.next = copynode
            dummy = dummynext

        dummy = pHead
        # 将复制链表的random指针指向原链表节点random指针指向的下一个节点
        # second step, random' to random'
        while dummy:
            dummyrandom = dummy.random
            copynode = dummy.next
            if dummyrandom:
                copynode.random = dummyrandom.next
            dummy = copynode.next
        # 分离复制的链表与原链表
        # third step, split linked list
        dummy = pHead
        copyHead = pHead.next
        while dummy:
            copyNode = dummy.next
            dummy.next = copyNode.next
            if copyNode.next:
                copyNode.next = copyNode.next.next
            else:
                copyNode.next = None
            dummy = dummy.next

        return copyHead
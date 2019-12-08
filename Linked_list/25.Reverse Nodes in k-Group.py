from Linked_list import linkedlist_operate

class LNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

def reverse( head):
    p, rev = head, None
    while p:
        rev, rev.next, p = p, rev, p.next
    return rev

def reverseKGroup(head, k):

    # cur = head
    # count = 0
    # # cur指针遍历到下一个k个数组的原始头结点
    # while cur and count != k:
    #     cur = cur.next
    #     count += 1
    #
    # if count == k:
    #     # 获取下一组反转后的头结点
    #     cur = reverseKGroup(cur,k)
    #     # 对k个链表组内的节点进行反转
    #     while count:
    #         tmp = head.next
    #         # 将下一组反转后的头结点接到该组head结点后
    #         head.next = cur
    #         cur = head
    #         head = tmp
    #         count -= 1
    #     head = cur
    # return head

    if not head or k < 2:
        return
    count = k
    pre = None
    cur = head

    while count:
        if cur:
            # 进入一个节点cur
            # 即将它放到pre位置（即数组最前面）,pre存储的是逆序后的已读入的链表结点
            cur.next,pre,cur = pre,cur,cur.next
            count -= 1
            if count == 0:
                # 将下一组k个链表结点 反转 接到‘head’后面，这个head是每次迭代
                head.next = reverseKGroup(cur,k)
        else:
            # 如果结点总数不是 k 的整数倍，最后剩余的节点保持原有顺序
            head = reverse(pre)
            return head
    # pre存储本轮k个结点逆序后的链表输出
    return pre

if __name__ == '__main__':
    l = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    llist = linkedlist_operate.LinkList()
    cur = llist.initList(l)
    k = 5
    res = reverseKGroup(cur.next,k)
    print('输出')
    llist.outll(res)

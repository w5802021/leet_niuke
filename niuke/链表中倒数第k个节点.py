class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        slow,fast = head,head
        for i in range(k):
            if fast == None:
                return None
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow
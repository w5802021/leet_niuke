from Tree import operate_tree

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def GetNext(self, pNode):
        '''
        分三种情况来写代码
        :param pNode:
        :return:
        '''
        node = pNode
        if not node:
            return
        # 若当前节点有右子树，下一个结点即为右子树最左下角的节点
        if node.right:
            res = node.right
            while res.left:
                res = res.left
            return res
        # 若没有右子树，且节点是父结点的左节点，那么下一个结点就是当前节点的父结点
        #              若节点不是父结点的左节点，那么一直往上找父结点直到找到一个节点是父结点的左节点，返回该父结点
        else:
            while node.next:
                #
                if  node.next.left == node:
                    return node.next
                node = node.next
            return




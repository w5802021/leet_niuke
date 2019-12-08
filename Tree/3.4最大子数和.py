from Tree import operate_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxsubtree(root,maxsum=float('-inf')):
    '''
    方法：后序遍历
    :param root:
    :param maxsum:
    :return:
    '''
    if not root:
        return 0

    l = maxsubtree(root.left,maxsum)
    r = maxsubtree(root.right,maxsum)
    sums = root.val + l + r
    # 判断左、右子树及以root为节点的数的节点数之和与maxsum的大小
    maxsum = max(maxsum,sums,l,r)
    return maxsum

class solution:
    maximum = float('-inf')
    result = None
    def findSubtree(self, root):
        self.helper(root)
        return self.result,self.maximum

    def helper(self, root):
        if root is None:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        sums = left + right + root.val

        if sums > self.maximum:
            self.maximum = sums
            self.result = root
        return sums

if __name__ == '__main__':
    nums = [-10, 9, 20, None, None, 15, 7]
    # nums = [15,16,17,8,67,7,41,55,None,44,None,None,11,None,None]
    tree = operate_tree.Tree()
    sol = solution()
    print(maxsubtree(tree.creatTree(nums)))

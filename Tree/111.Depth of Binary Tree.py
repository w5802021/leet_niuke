from Tree import operate_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def minDepth(root):
    if not root:
        return 0
    if not root.left:
        return minDepth(root.right) + 1
    if not root.right:
        return minDepth(root.left) + 1
    return min(minDepth(root.left),minDepth(root.right)) + 1

def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left),maxDepth(root.right))

if __name__ == '__main__':
    l = [3,9,20,1,2]
    tree = operate_tree.Tree()
    print(maxDepth(tree.creatTree(l)))

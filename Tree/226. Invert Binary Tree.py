from Tree import operate_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def invertTree(root):

    if not root:
        return None
    root.left, root.right = root.right, root.left      #反转左右节点
    invertTree(root.left)
    invertTree(root.right)
    return root


if __name__ == '__main__':
    l = [4,2,7,1,3,6,9]
    tree = operate_tree.Tree()
    print(tree.levelOrder(invertTree(tree.creatTree(l))))
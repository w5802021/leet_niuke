from Tree import operate_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def insertIntoBST(root, val):
    if val > root.val:
        if root.right:
            insertIntoBST(root.right, val)
        else:
            root.right = TreeNode(val)

    elif val < root.val:
        if root.left:
            insertIntoBST(root.left, val)
        else:
            root.left = TreeNode(val)
    return root

if __name__ == '__main__':
    l = [18, 2, 22, None, None, None, 63, None, 84, None, None]
    val = 79
    tree = operate_tree.Tree()
    print(tree.preorderTraversal(tree.creatTree(l)))
    print(tree.preorderTraversal(insertIntoBST(tree.creatTree(l), val)))
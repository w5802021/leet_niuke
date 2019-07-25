from Tree import operate_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def flatten(root):
    def dfs(root):
        if not root:
            return
        dfs(root.left)
        dfs(root.right)
        # 用后续遍历来调整整个二叉树的结构
        # 先将左、右子树调整为链式结构，最后到根节点
        tmp = root.right
        root.right = root.left
        root.left = None
        # 将原来的root.right赋给root.right.right
        # 相当于root.left-root-root.right------>root-root.left-root.right
        while root.right:
            root = root.right
        root.right = tmp
        return root
    dfs(root)
    return root


if __name__ == '__main__':
    l = [1,2,5,3,4,None,6]

    tree = operate_tree.Tree()
    flatten(tree.creatTree(l))

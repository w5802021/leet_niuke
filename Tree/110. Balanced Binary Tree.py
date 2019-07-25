from Tree import operate_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isBalanced(root):
    # 本题可与111 树的最大深度结合看
    # （a1,a2）a1代表子树的高度，a2代表当前子树是否是平衡二叉树
    def check(root):
        if not root:
            return (0, True)
        # 递归遍历root节点的左、右子树
        l = check(root.left)
        r = check(root.right)
        # 判断左子树 右子树是否为平衡状态
        if (not l[1]) | (not r[1]):
            return (0, False)
        # 判断左右子树的高度差
        if abs(l[0] - r[0]) > 1:
            return (0, False)
        else:
            # (获取树的最大深度，平衡状态)
            return (max(l[0], r[0]) + 1, True)
    return check(root)[1]

if __name__ == '__main__':
    l = [3,9,20,None,None,15,7]
    tree = operate_tree.Tree()
    print(isBalanced(tree.creatTree(l)))
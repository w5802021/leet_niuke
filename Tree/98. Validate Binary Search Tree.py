from Tree import operate_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isValidBST(root):  # 不能简单地认为递归每个节点，左节点小于当前节点，右节点大于当前节点就可以了，还要注意边界问题，
                       # 即左子树上的节点值（包括左子树上的右子节点）都少于根节点（即上限动态调整） ，
                       # 右子树上的节点值（包右子树上的左子节点）都大于根节点（即下限动态调整）
    def dfs(root, lower, upper):
        if not root:
            return True

        if root.val > lower and root.val < upper:
            # 每次递归需要改变边界的上下限  要保证所有递归子树都满足二叉搜索树的条件才成立
            return dfs(root.left, lower, root.val) and dfs(root.right, root.val, upper)
        else:
            return False

    return dfs(root, float('-inf'), float('inf'))

if __name__ == '__main__':
    l = [9,7,11,5,8,10,12]
    tree = operate_tree.Tree()
    print(isValidBST(tree.creatTree(l)))
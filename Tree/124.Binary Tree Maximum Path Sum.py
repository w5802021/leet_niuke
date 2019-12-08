from Tree import operate_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxPathSum(root: TreeNode):
    '''
    思路：后序遍历到最右节点，从下往上递归
    :param root:
    :return:
    '''
    def max_path(root):
        nonlocal max_num
        if not root:
            return 0
        # 后序遍历到树的最右子节点
        left = max_path(root.left)
        right = max_path(root.right)
        # 记录当前节点最大值 = 左子树节点之和+右子树节点之和+根节点  即后面的后序往上递归的寻路过程都是为了找到有路径的增益大于该节点
        # 的左或右子树的节点之和
        max_num = max(left + right + root.val, max_num)
        # 此节点与左右子树较大值之和，较差的解直接被舍弃，不会再被用到
        tmp = max(left, right) + root.val
        # 若root的较大分支增益仍为负
        # 不会在任何情况选这条路（父节点root中止），因此返回0
        return max(0,tmp)

    max_num = float('-inf')
    max_path(root)
    return max_num

if __name__ == '__main__':
    nums = [-10, 9, 20, None, None, 15, 7]
    tree = operate_tree.Tree()
    print(maxPathSum(tree.creatTree(nums)))




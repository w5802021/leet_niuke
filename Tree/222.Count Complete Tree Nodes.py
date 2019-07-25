from Tree import operate_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def countNodes(root):
    def get_height(root):
        if not root:
            return 0
        # 这里因为给定完全二叉树，故求树的高度可简化
        return 1 + get_height(root.left)

    if not root: return 0
    h = get_height(root)

    if get_height(root.right) == h - 1:
        # 说明根节点的左子树是满二叉树 故而 （左子树的节点数+根节点）== 2**(h-1) -1 + 1
        return 2 ** (h - 1) + countNodes(root.right)
    else:
        # 根节点的右子树最后一层没有节点，故右子树的节点数+根节点 == 2**（h-2）-1 + 1
        return 2 ** (h - 2) + countNodes(root.left)

if __name__ == '__main__':
    l = [1,2,3,4,5,6]
    tree = operate_tree.Tree()
    print(countNodes(tree.creatTree(l)))

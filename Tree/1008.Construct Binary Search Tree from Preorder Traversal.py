from Tree import operate_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#将先序遍历输出后的列表转化为二叉搜索树
def bstFromPreorder(preorder):
    if not preorder:
        return None

    root = TreeNode(preorder[0])
    if len(preorder) == 1:
        return root
    r = 0
    for i in range(1,len(preorder)):
        if preorder[i] > preorder[0]:
            r = i
            break
    # 表示数组的值都在root节点的左子树中
    if r == 0:
        root.left = bstFromPreorder(preorder[1:])
    # r表示root节点右子树的最小节点编号
    else:
        root.left = bstFromPreorder(preorder[1:r])
        root.right = bstFromPreorder(preorder[r:])

    return root

def bstFromPreorder2(preorder):
    if preorder:
        root = TreeNode(preorder[0])

        l,r = [],[]
        for i in range(1, len(preorder)):
            if preorder[i] <= preorder[0]:
                l.append(preorder[i])
            else:
                r.append(preorder[i])

        root.left = bstFromPreorder2(l)
        root.right = bstFromPreorder2(r)

        return root






if __name__ == '__main__':
    l = [3,9,20,1,2]
    tree = operate_tree.Tree()
    print(tree.levelOrder(bstFromPreorder([8,5,1,7,10,12])))
from Tree import operate_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildtree(preorder,inorder):
    '''
    中序列表中每个节点具有划分左右子树的作用
    :param preorder:
    :param inorder:
    :return:
    '''
    # 由中序遍历判断子节点，由先序遍历构建子树
    def build(pre,prestart,preend,instart,inpos):
        if prestart > preend:
            return
        # 先序遍历建子树
        root = TreeNode(pre[prestart])
        # root节点在中序列表中的位置  为后面划分左右子树做准备
        rootidx = inpos[root.val]
        # 左子树在preorder所占长度
        leftLen = rootidx - instart
        ###  通过不断迭代缩小prestart-preend的范围缩小了递归的时间
        # 递归构建左子树   root占据了prestart的位置 ， 故prestart+1
        root.left = build(pre, prestart + 1, prestart + leftLen, instart, inpos)
        # 递归构建右子树    rootidx + 1是右子树在inoder中第一个输出的节点
        root.right = build(pre, prestart + leftLen + 1, preend, rootidx + 1, inpos)
        return root

    inPos = {val: idx for idx, val in enumerate(inorder)}
    return build(preorder, 0, len(preorder)-1, 0, inPos)

if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    tree = operate_tree.Tree()
    result = buildtree(preorder, inorder)
    print(tree.levelOrder(result))


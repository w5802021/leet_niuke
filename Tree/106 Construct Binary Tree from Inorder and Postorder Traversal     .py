from Tree import operate_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildtree(postorder,inorder):
    '''
    给与注释的三行代码与105题不同
    :param preorder:
    :param inorder:
    :return:
    '''

    def build(post, poststart, postend, instart, inPos):
        if poststart > postend: return None
        #
        root = TreeNode(post[postend])

        rootIdx = inPos[root.val]
        leftLen = rootIdx - instart
        #后序遍历   0 - poststart + leftLen - 1
        root.left = build(post, poststart, poststart + leftLen - 1, instart, inPos)
        # root占据了postend的位置 ， 故postend-1
        root.right = build(post, poststart + leftLen, postend - 1, rootIdx + 1, inPos)
        return root

    inPos = {val: idx for idx, val in enumerate(inorder)}
    return build(postorder, 0, len(postorder)-1, 0, inPos)

def buildTree1(postorder,inorder) :
    if not inorder or not postorder:
        return None
    root = TreeNode(postorder[-1])
    for i in range(len(inorder)):
        if postorder[-1] == inorder[i]:
            root.left = buildTree1(postorder[:i],inorder[:i])
            root.right = buildTree1(postorder[i:-1],inorder[i + 1:])

    return root
if __name__ == '__main__':
    inorder = [9,3,15,20,7]
    preorder = [9,15,7,20,3]
    tree = operate_tree.Tree()
    result = buildTree1(preorder, inorder)
    print(tree.levelOrder(result))

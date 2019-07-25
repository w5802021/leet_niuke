from Tree import operate_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#################################二叉搜索树的最近公共祖先######################  235
def lowestCommonAncestor(root, p, q):  #递归方法     利用二叉搜索树的性质快速求解
    if not root or not p or not q:
        return

    if p.val < root.val and q.val < root.val:
        return lowestCommonAncestor(root.left,p,q)

    elif p.val > root.val and q.val > root.val:
        return lowestCommonAncestor(root.right,p,q)

    return root

def lowestCommonAncestor1(root, p, q):   #非递归方法
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left

        elif p.val > root.val and q.val > root.val:
            root = root.right

        else:
            return root

########################################二叉树的最近公共祖先###############################  236
def lowestCommonAncestor2(root,p,q):
    if root == None or root.val == p.val or root.val == q.val:
        return root
    # 递归查找左子树是否存在p或q
    left = lowestCommonAncestor2(root.left,p,q)
    # 递归查找左子树是否存在p或q
    right = lowestCommonAncestor2(root.right,p,q)
    # 父节点的左子树或右子树查找到匹配节点，则将匹配到的节点值往上回送到父节点位置
    if left and right:
        return root
    elif left:
        return left
    else:
        return right

if __name__ == '__main__':
    l = [3,5,1,6,2,0,8,None,None,7,4]
    p = 0
    q = 8
    tree = operate_tree.Tree()
    print(lowestCommonAncestor2(tree.creatTree(l),TreeNode(p),TreeNode(q)).val)  #输出该节点的值


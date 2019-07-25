from Tree import operate_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def mergeTrees(t1, t2):
    if not t1 and not t2:
        return

    if not t1 and t2:
        return t2

    if not t2 and t1:
        return t1

    t1.val += t2.val    #递归循环里只考虑本层循环需要做的
    t1.left = mergeTrees(t1.left, t2.left)
    t1.right = mergeTrees(t1.right, t2.right)
    return t1

if __name__ == '__main__':
    l = [1,3,2,5,None,None,None]
    r = [2,1,3,None,4,7,None]
    tree = operate_tree.Tree()
    print(tree.levelOrder(mergeTrees(tree.creatTree(l),tree.creatTree(r))))
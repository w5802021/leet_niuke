from Tree import operate_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSameTree(p, q):
    if not p and not q:
        return True
    if p and q == None:
        return False
    if q and p == None:
        return False

    if p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    else:
        return False

if __name__ == '__main__':
    l = [1,2,3]
    r = [1,2,3]

    tree = operate_tree.Tree()
    print(isSameTree(tree.creatTree(l), tree.creatTree(r)))

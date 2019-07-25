from Tree import operate_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def searchBST(root, val):

    while root:
        if val < root.val:
            root = root.left
        elif val > root.val:
            root = root.right
        else:
            return root
    return root

def searchBST1(root, val):
    if not root:
        return None

    if val < root.val:
        return searchBST(root.left, val)
    elif val > root.val:
        return searchBST(root.right, val)
    else:
        return root



if __name__ == '__main__':
    l = [18,2,22,None,None,None,63,None,84,None,None]

    tree = operate_tree.Tree()
    print(searchBST(tree.creatTree(l),63))
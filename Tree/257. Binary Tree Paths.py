from Tree import operate_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def binaryTreePaths(root):              #思路同112的路径之和2

    def dfs(root, tmp, res):
        if not root:
            return []

        tmp += str(root.val) + '->'
        if not root.left and not root.right:
            res.append(tmp[:-2])
        dfs(root.left, tmp, res)
        dfs(root.right, tmp, res)

    res = []
    tmp = ''
    dfs(root, tmp, res)
    return res

if __name__ == '__main__':
    l = [1,2,3,None,5,None,None]
    tree = operate_tree.Tree()
    print(binaryTreePaths(tree.creatTree(l)))
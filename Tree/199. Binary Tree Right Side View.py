from Tree import operate_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def rightSideView(root):
    '''
    方法一：dfs递归
    :param root:
    :return:
    '''
    res = []
    def dfs(root,res,deep):
        if root:
            if len(res) < deep:
                res.append(root.val)
            dfs(root.right, res, deep + 1)
            dfs(root.left,res,deep+1)
    dfs(root,res,1)
    return res

def rightSideView1(root):
    '''
    方法二：层序遍历（bfs）非递归
    :param root:
    :return:
    '''
    res, lev = [], [root]
    while root and lev:
        res.append(lev[-1].val)
        #(n.left, n.right)
        lev = [k for n in lev for k in (n.left, n.right) if k]
    return res

if __name__ == '__main__':
    l = [1,2,3,8,5,9,4]
    tree = operate_tree.Tree()
    print(rightSideView(tree.creatTree(l)))
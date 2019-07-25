from Tree import operate_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class solution:
    def __init__(self):
        self.maxnode = TreeNode(0)
        self.minnode = TreeNode(2**32)

    def getmaxmin(self,root):
        if not root:
            return
        if not root.left and not root.right:
            if root.val > self.maxnode.val:
                self.maxnode = root
            elif root.val < self.minnode.val:
                self.minnode = root
        self.getmaxmin(root.left)
        self.getmaxmin(root.right)

    def getlca(self,root):
        if root == None or root.val == self.maxnode.val or root.val == self.minnode.val:
            return root
        # 递归查找左子树是否存在p或q
        left = self.getlca(root.left)
        # 递归查找左子树是否存在p或q
        right = self.getlca(root.right)
        # 父节点的左子树或右子树查找到匹配节点，则将匹配到的节点值往上回送到父节点位置
        if left and right:
            return root
        elif left:
            return left
        else:
            return right

    def getdist(self,lca,node):
        if not lca:
            return None
        if lca.val == node.val:
            return 0
        dist = self.getdist(lca.left,node)
        if dist == None:
            dist = self.getdist(lca.right,node)
        if dist != None:
            return dist + 1
        return None

    def main(self,root):
        '''
        思路：1、首先在二叉树中找到最大、最小的权值节点
             2、求得最大、最小节点的最近公共祖先
             3、求得最大、最小的权值节点与最近公共祖先的距离和即为所求
        :param root:
        :return:
        '''
        self.getmaxmin(root)
        lca = self.getlca(root)
        dist1 = self.getdist(lca,self.maxnode)
        dist2 = self.getdist(lca, self.minnode)
        return dist1 + dist2

if __name__ == '__main__':
    l = [5, 4, 8, 11, None, 13, 4, 14, 2, None, None, 5, 1]
    tree = operate_tree.Tree()
    root = tree.creatTree(l)
    sol = solution()
    print(sol.main(root))
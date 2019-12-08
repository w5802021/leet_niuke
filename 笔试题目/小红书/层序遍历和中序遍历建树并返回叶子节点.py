class TreeNode(object):
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x

class Solution(object):
    def __init__(self):
        self.leaf = []

    def creatTree(self, bfsorder, inorder):
        """
        从中序遍历找出左右子树，然后再从序列层次遍历中找出左右子树序列，重建二叉树
        :param bfsorder:
        :param inorder:
        :return:
        """
        if not bfsorder:
            return
        if len(bfsorder) == 1 and bfsorder[0] not in self.leaf:
            self.leaf.append(bfsorder[0])

        root = TreeNode(bfsorder[0])
        # 根节点在中序遍历的索引
        root_index = inorder.index(root.val)
        # 中序遍历的左子树
        left_in = inorder[:root_index]
        # 中序遍历的右子树
        right_in = inorder[root_index + 1:]
        # 层次遍历的左子树
        left_bsf = [x for x in bfsorder if x in left_in]
        right_bfs = [x for x in bfsorder if x in right_in]

        # 对左子树依层序遍历与中序遍历建树
        root.left = self.creatTree(left_bsf, left_in)
        # 对右子树依层序遍历与中序遍历建树
        root.right = self.creatTree(right_bfs, right_in)
        return root

    def preorder(self, root):
        if not root:
            return []
        return [root.val] + self.preorder(root.left) + self.preorder(root.right)

    def postorder(self, root):
        if not root:
            return []
        return self.postorder(root.left) + self.postorder(root.right) + [root.val]

s = Solution()
bfsorder = [int(x) for x in input().split()]
inorder = [int(x) for x in input().split()]
root = s.creatTree(bfsorder, inorder)

pre = s.preorder(root)
post = s.postorder(root)
print(' '.join(list(map(str, s.leaf))))
print(' '.join(list(map(str, pre))))
print(' '.join(list(map(str, post))))
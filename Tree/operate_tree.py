class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree:

    def preorderTraversal(self,root):   #前序遍历
        def dfs(root, res):
            if root:
                res.append(root.val)
                dfs(root.left, res)
                dfs(root.right, res)

        res = []
        dfs(root, res)
        return res

    def inorderTraversal(self,root):    #中序遍历
        def dfs(root,res):
            if root:
                if root.left:
                    dfs(root.left,res)

                res.append(root.val)

                if root.right:
                    dfs(root.right,res)

        res = []
        dfs(root, res)
        return res

    def postorderTraversal(self,root):   #后序遍历
        def dfs(root,res):
            if root:
                if root.left:
                    dfs(root.left,res)

                if root.right:
                    dfs(root.right,res)

                res.append(root.val)

        res = []
        dfs(root, res)
        return res

    def levelOrder(self, root):
        res, level = [], [root]

        while root and level:
            res.append([node.val for node in level])

            lrpair = [(node.left, node.right) for node in level]

            level = [leaf for lr in lrpair for leaf in lr if leaf]
        return res

    def creatTree(self,nodeList):           #数组层序构建二叉树
        if nodeList[0] == None:
            return None
        head = TreeNode(nodeList[0])
        Nodes = [head]            #在后续存储所有节点
        j = 1
        for node in Nodes:        #Nodes在每轮迭代都会变化，node遍历过的数就不会再遍历了
            if node:
                node.left = (TreeNode(nodeList[j]) if nodeList[j] != None else None)
                Nodes.append(node.left)
                j += 1
                if j == len(nodeList):
                    return head
                node.right = (TreeNode(nodeList[j]) if nodeList[j] != None else None)
                j += 1
                Nodes.append(node.right)
                if j == len(nodeList):
                    return head



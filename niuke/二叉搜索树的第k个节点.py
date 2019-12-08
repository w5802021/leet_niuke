class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        res = []
        def dfs(root,k,res):
            if not root:
                return
            dfs(root.left,k,res)
            # res数组长度小于k说明还没有找满前k个数
            if len(res) < k:
                res.append(root)
            else:
                return
            dfs(root.right,k,res)

        if k == 0:
            return None
        else:
            dfs(pRoot,k,res)
            if len(res) < k:
                return None
            return res[-1]


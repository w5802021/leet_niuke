from Tree import operate_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sortedArrayToBST( nums):
    if not nums:
        return None
    mid = len(nums) // 2
    T = TreeNode(nums[mid])
    T.left = sortedArrayToBST(nums[:mid])
    T.right = sortedArrayToBST(nums[mid + 1:])
    return T

def printtreemidorder(root):

    def dfs(root,res):
        if not root:
            return

        if root.left:
            dfs(root.left,res)

        res.append(root.val)

        if root.right:
            dfs(root.right,res)

    res = []
    dfs(root, res)
    return res

if __name__ == '__main__':
    l = [1,2,3,4,5]
    root = sortedArrayToBST(l)
    tree = operate_tree.Tree()
    print(tree.levelOrder(root))
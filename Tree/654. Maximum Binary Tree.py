from Tree import operate_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def constructMaximumBinaryTree(nums):         #常规递归思路

    if len(nums) == 0:
        return None

    maxi = max(nums)
    root = TreeNode(maxi)
    l = nums[:nums.index(maxi)]
    r = nums[nums.index(maxi) + 1:]
    root.left = constructMaximumBinaryTree(l)
    root.right = constructMaximumBinaryTree(r)
    return root

def constructMaximumBinaryTree1(nums):       #用栈实现，速度更快
    stack = []                               #用列表存根节点
    for n in nums:
        node = TreeNode(n)
        while stack and stack[-1].val < n:
            node.left = stack.pop()
        if stack:
            stack[-1].right = node
        stack.append(node)
    return stack[0]

if __name__ == '__main__':
    l = [3,2,1,6,0,5]

    tree = operate_tree.Tree()
    print(tree.levelOrder(constructMaximumBinaryTree1(l)))
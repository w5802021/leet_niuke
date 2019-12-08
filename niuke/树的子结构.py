class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # 判断a的子结构是否与b相同
        def isequal(root1,root2):
            if (not root1 and not root2) or (not root2 and root1):
                return True
            if not root1 and root2:
                return False
            if root1.val == root2.val:
                return isequal(root1.left,root2.left) and isequal(root1.right,root2.right)
            else:
                return False

        result = False
        if pRoot1 and pRoot2:
            # 如果树a中出现于树b的根节点值相同的结点，则进行子结构的匹配
            if pRoot1.val == pRoot2.val:
                result = isequal(pRoot1, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result
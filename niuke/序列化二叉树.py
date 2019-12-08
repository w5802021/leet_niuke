from Tree import operate_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.flag = -1

    def Serialize(self, root):
        # write code here
        if not root:
            return '#,'
        return str(root.val) + ',' + self.Serialize(root.left) + self.Serialize(root.right)

    def Deserialize(self, s):
        # write code here
        self.flag += 1
        l = s.split(',')

        if self.flag >= len(s):
            return None
        root = None

        if l[self.flag] != '#':
            root = TreeNode(int(l[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root

if __name__ == '__main__':
    l = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
    tree = operate_tree.Tree()
    root = tree.creatTree(l)
    test = Solution()
    s = test.Serialize(root)
    res = test.Deserialize(s)
    a = 1
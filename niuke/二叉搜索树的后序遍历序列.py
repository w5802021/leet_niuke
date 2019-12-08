class Solution:
    def VerifySquenceOfBST(self, sequence):

        length = len(sequence)
        # 对于递归来说，当sequence为空为终止条件
        if length == 0:
            return False
        # 对于判断BST来说，sequence为空为终止条件
        if length == 1:
            return True

        root = sequence[-1]
        left = 0
        # 找到squence中root左子树的部分
        while sequence[left] < root:
            left += 1
        # 判断root的右子树是否有小于root的节点
        for i in range(left, length - 1):
            if sequence[i] < root:
                return False

        return self.VerifySquenceOfBST(sequence[:left]) or self.VerifySquenceOfBST(sequence[left:-1])
class Solution:
    def VerifySquenceOfBST(self, sequence):
        '''
        二叉搜索树的后序遍历序列
        :param sequence:
        :return:
        '''
        length = len(sequence)
        if length == 0:
            return False
        if length == 1:
            return True
        # 后序遍历根节点
        root = sequence[-1]
        # left为右子树的最小结点号
        r = 0
        while sequence[r] < root:
            r += 1
        for j in range(r, length-1):
            if sequence[j] < root:
                return False
        return self.VerifySquenceOfBST(sequence[:r]) or self.VerifySquenceOfBST(sequence[r:length-1])
class Solution:
    def __init__(self):
        self.head = None
        self.end = None

    def Convert(self, root):
        '''
        二叉搜索树转化为双向链表
        思路：
        :param root:
        :return:
        '''
        # write code here
        if not root:
            return
        self.Convert(root.left)
        root.left = self.end
        # self.end == None表示双向链表为空时 将root分别赋予给 self.head self.end
        if self.end == None:
            self.head = root

        else:
            self.end.right = root
        self.end = root

        self.Convert(root.right)
        return self.head
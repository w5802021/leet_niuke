from Tree import operate_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.head = None
        self.end = None

    def Convert(self, root):
        # write code here
        if not root:
            return
        self.Convert(root.left)

        root.left = self.end
        if not self.end:
            self.head = root
        else:
            self.end.right = root
        # 最后的end指针指向最右边的结点
        self.end = root

        self.Convert(root.right)
        return self.head

class Solution1:
     def Convert(self, root):
          if not root:
                return None
          if not root.left and not root.right:
                return root
        # 1.将左子树构造成双链表，并返回链表头节点
          left = self.Convert(root.left)
          p = left
        # 2.定位至左子树双链表最后一个节点
          while p and p.right:
                p = p.right
          # 3.如果左子树链表不为空的话，将当前root追加到左子树链表
          if left:
                p.right = root
                root.left = p
          # 4.将右子树构造成双链表，并返回链表头节点
          right = self.Convert(root.right)
          # 5.如果右子树链表不为空的话，将该链表追加到root节点之后
          if right:
               right.left = root
               root.right = right
          return left if left else root 

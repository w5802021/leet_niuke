from Tree import operate_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSymmetric(root):
    '''
    满足镜像的条件：1、它们的两个根结点具有相同的值
                  2、每个树的右子树都与另一个树的左子树镜像对称
    方法：递归
    :param root:
    :return:
    '''
    def isqeual(node1, node2):
        if not node1 and not node2:
            return True

        if not node1 or not node2:
            return False

        if node1.val != node2.val:
            return False
        # 递归遍历每一层的相邻的两个结点，判断是否对称
        return isqeual(node1.left, node2.right) and isqeual(node1.right, node2.left)

    return isqeual(root, root)

def isSymmetric1(root):
    '''
    方法：迭代
    :param root:
    :return:
    '''
    queue = [root, root]
    while queue:
        node1 = queue.pop()
        node2 = queue.pop()

        if not node1 and not node2: continue
        if not node1 or not node2: return False
        if node1.val != node2.val: return False

        queue.append(node1.left)
        queue.append(node2.right)
        queue.append(node1.right)
        queue.append(node2.left)
    return True


if __name__ == '__main__':
    l = [1,2,2,None,3,None,3]
    tree = operate_tree.Tree()
    print(isSymmetric1(tree.creatTree(l)))
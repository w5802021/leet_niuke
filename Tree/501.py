from Tree import operate_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def findMode(root):
    if not root:
        return []
    else:
        res = []                      #中序遍历递归整颗树的节点 并存在列表，用数组的思想来解决
        middle_digui(root, res)
    from collections import Counter
    dic = Counter(res)
    max = 0
    for k in dic:
        if dic[k] > max:
            max = dic[k]  #找到众数的个数
    temp = []
    for k in dic:
        if dic[k] == max:
            temp.append(k)  #找到所有众数的值
    return temp


def middle_digui(root, res):
    if not root:
        return
    middle_digui(root.left, res)
    res.append(root.val)
    middle_digui(root.right, res)

if __name__ == '__main__':
    l = [1,None,2,2]
    tree = operate_tree.Tree()
    print(findMode(tree.creatTree(l)))
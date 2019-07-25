from Tree import operate_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

##############################################################################################   112
def hasPathSum(root, sum):    #路径之和1   问题：是否存在根节点到叶子节点路径总和等于给定目标和的路径
    if not root:
        return False

    while not root.left and not root.right:
        return sum == root.val
    sum = sum - root.val

    return hasPathSum(root.left, sum) or hasPathSum(root.right, sum)

##################################################################################################   113
def hasPathSum1(root, sum):    #路径之和2    问题：从根节点到叶子节点路径总和等于给定目标和的  具体的路径

    def dfs(root, sum, res, tmp):
        if not root:
            return []

        tmp.append(root.val)
        if not root.left and not root.right and root.val == sum:
            # 这个地方一定要使用tmp的拷贝, 因为后面tmp.pop()会弹出元素，导致错误
            res.append(tmp.copy())
        sum = sum - root.val
        dfs(root.left, sum, res, tmp)
        dfs(root.right, sum, res, tmp)
        tmp.pop()

    res = []
    tmp = []
    dfs(root, sum, res, tmp)
    return res

#########################################################################################  437
def hasPathSum2(root, sum) :   # 路径之和3    问题：从任意位置到出发经过（路径方向必须是向下）若干连续的二叉树结构满足  路径之和为目标数
    def mypathsum(root, sum, tar):
        if not root:
            return 0
        res = 0
        for t in tar:
            if root.val == t:
                res += 1
        tar = [x - root.val for x in tar] + [sum]
        return res + mypathsum(root.left, sum, tar) + mypathsum(root.right, sum, tar)
    return mypathsum(root, sum, [sum])

if __name__ == '__main__':
    l = [5,4,8,11,None,13,4,7,2,None,None,5,1]
    sum = 22
    tree = operate_tree.Tree()
    print(hasPathSum2(tree.creatTree(l),sum)) #输出该节点的值
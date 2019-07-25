class treeNode():
    def __init__(self,data=-1,left=None,right=None):
        self.val=data
        self.left=left
        self.right=right
    def __str__(self):
        return str(self.val)

#####################################112####################################
def PathSum1(root, sum):

    if not root:
        return []

    sum = sum - root.val
    if not root.left and not root.right and sum == 0:   #遍历到叶子节点
        return True

    return PathSum1(root.left, sum) or PathSum1(root.right, sum)

###########################################113#######################################
def pathSum2(root, sum):
    if not root:
        return []

    def dfs(root, sum, res, temp):
        if not root:
            return []

        temp.append(root.val)

        sum = sum - root.val
        if not root.left and not root.right and sum == 0 :
            res.append(temp.copy())

        dfs(root.left, sum, res, temp)
        dfs(root.right, sum, res, temp)
        temp.pop()

    res = []    #列表存在此，防止每次递归将列表清空
    temp = []
    dfs(root, sum, res, temp)
    return res

###################################################437##################################################
class sol1:           #双重递归的方法
    result = 0
    def mypathsum(self, root, sum):      #第二层递归
        if not root:
            return 0

        sum -= root.val
        if sum == 0:
            self.result += 1

        self.mypathsum(root.left, sum)
        self.mypathsum(root.right, sum)

    def pathSum3(self, root, sum):        #第一层递归
        if not root:
            return 0

        self.mypathsum(root, sum)
        self.pathSum3(root.left, sum)
        self.pathSum3(root.right, sum)
        return self.result

class sol2:
    def pathSum3(self, root, sum):         #一维数组 + 一层递归
        return self.mypathsum(root, sum, [sum])

    def mypathsum(self, node, origin, targets):
        if not node:
            return 0

        result = 0
        for t in targets:
            if t == node.val:     #targets中存在0的元素即表示找到了该数
                result += 1

        targets = [t-node.val for t in targets]+[origin]         #记录下经过一个节点后的 ，加origin = sum是要看后面有没有直接 等于sum的数字

        return result + self.mypathsum(node.left, origin, targets)+self.mypathsum(node.right, origin, targets)

if __name__ == '__main__':
    # root = treeNode(5,treeNode(4,treeNode(11,treeNode(7),treeNode(2))),treeNode(8,treeNode(13),treeNode(4,treeNode(5),treeNode(1))))
    # sum = 22
    # print(PathSum1(root,sum))
    # print(pathSum2(root,sum))

    root1 = treeNode(10, treeNode(5, treeNode(3, treeNode(3), treeNode(-2)),treeNode(2, None, treeNode(1))),
                    treeNode(-3, None, treeNode(11)))
    sum1 = 8
    S = sol2()
    print(S.pathSum3(root1,sum1))
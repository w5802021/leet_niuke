def findKthNumber(n, k):
    '''
    思路：对于10叉树，需要知道n的大小方能确定树的深度，依此来求得k排序

    :param n:字典中最大的节点
    :param k:
    :return:
    '''
    res = 1
    k -= 1
    while k > 0:
        gap = 0
        interval = [res,res+1]
        # 计算res与res+1之间的数字个数gap
        # 注意：1和2之间隔了多少个数需要根据n的大小确定树的深度来确定，如果n = 99, 那么1与2之间隔了11个数 n=999,1和2之间隔了111
        # 个数，
        while interval[0] <= n:
            gap += (min(n+1,interval[1]) - interval[0])
            interval = [10*interval[0],10*interval[1]]
        # 如果相隔的距离小于k，那么我们可以将搜索范围【0——k】缩小到【gap——k】，下一轮迭代则是【gap_old+gap_new——k】
        if gap <= k:
            res += 1
            k -= gap
        # 如果相隔的距离大于k，那么说明超出了搜索范围，因此仅将范围缩小1，res*=10,相当于在当前res节点上跳到10叉树下一个同位置
        # 子节点，排序位置仅变动1，之后，其得到的gap则会小一个数量级，例如之前gap=111，超过了k的范围，往子节点跳了一格后，
        # 下一次得到的gap=11
        else:
            res *= 10
            k -= 1
    return res

if __name__ == '__main__':
    n = 999
    k = 100
    print(findKthNumber(n, k))

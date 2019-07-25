
def getallcomb(nsum,pdata,ndepth):
    '''
    题意：给定一个正整数n，求解出所有和为n的整数组合，要求组合按照递增方式展示，而且唯一
    :param nsum: 给定的整整n
    :param pdata: 存储递归时组合的数
    :param ndepth: 记录组合总数字的个数
    :return:
    '''
    if nsum < 0:
        return
    # 已达到要求，输出该整数组合
    if nsum == 0:
        print([pdata[j] for j in range(ndepth)])
        return
    # 记录本层节点父节点的取值
    start = (1 if ndepth == 0 else pdata[ndepth-1])
    # 该子树下，下一个递归节点的可取值（要保证本层节点的取值大于上层节点的取值）
    # 如果不要求组合按照递增方式，则上述start取值为1
    for i in range(start,nsum+1):
        pdata[ndepth] = i
        ndepth += 1
        getallcomb(nsum-i,pdata,ndepth)
        ndepth -= 1

if __name__ == '__main__':
    n = 10
    result = [None] * n
    getallcomb(n,result,0)

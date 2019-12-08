n,m,k=map(int,input().split())

def findKthNumber(n, m, k):
    '''
    方法：二分搜索
    思路：在m，n的乘法表中寻找不超过mid的个数，如果个数超过k则需减少右边的最大边界，反之则增大左边的边界
    :param n:
    :param m:
    :param k:
    :return:
    '''
    l = 1
    r = n*m+1
    while l < r:
        mid = l + (r-l)//2

        count = 0
        # 把每一行不大于mid的数累加
        for i in range(1,m+1):
            count += min(mid//i, n)
        # 二分搜索
        if count >= k:
            r = mid
        else:
            l = mid + 1
    return l

print(findKthNumber(n, m, n*m-k+1))








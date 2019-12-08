import math

def summ(s, n, m):
    # 计算以s为第一天的量，吃n天最少需要多少巧克力
    summ = 0
    for i in range(n):
        summ += s
        # s为下一天需要吃的数量
        s = math.ceil(s / 2)
    return summ

def bin_seach(n, m):
    '''
    题目要求第一天多吃多少巧克力？
    思路：第一天可以吃的巧克力数量为1---m块，因此可以尝试第一天取1到m中的数，并判断是否满足父母回来前还有巧克力即可
    贪心+二分搜索
    :param n: 父母出差n天
    :param m: 总的巧克力数量
    :return: 第一天最大的可吃的巧克力数量
    '''
    if n == 1:
        return m
    # 1--m中二分搜索
    low = 1
    high = m
    while low < high:
        # 偶数的话中位数往上取
        mid = math.ceil((low + high) / 2)
        if summ(mid, n, m) == m:
            return mid
        elif summ(mid, n, m) < m:
            low = mid
        else:
            high = mid - 1
    return high

if __name__ == '__main__':
    n, m = map(int,input().split())
    res = bin_seach(n, m)
    print(res)

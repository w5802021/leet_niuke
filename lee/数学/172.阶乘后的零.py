def trailingZeroes(n):
    '''
    统计数字1...n中，是5的倍数，25的倍数。。。的数量
    :param n:
    :return:
    '''
    res = 0
    while n >= 5:
        n = n // 5
        res += n
    return res
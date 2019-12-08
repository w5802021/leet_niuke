def myPow(x, n):
    '''
    思路：迭代 时间复杂度：O（logn） 空间复杂度O（1）
    :param x:
    :param n:
    :return:
    '''
    if n < 0:
        x = 1 / x
        n = -n
    pow = 1
    # x为当前乘子系数
    # pow为最后输出的值
    while n:
        # 若n为奇数，先将n-1乘上
        if n % 2 != 0:
            pow *= x
        # 此时n-1为偶数，将乘子系数连乘，
        x *= x
        # 将n//2
        n >>= 1
    return pow

def myPow1( x,  n):
    '''
    思路：递归 时间复杂度：O（logn） 空间复杂度O（logn）
    :param x:
    :param n:
    :return:
    '''
    def fastPow(x, n):
        if (n == 0):
            return 1
        half = fastPow(x, n // 2)
        if (n % 2 == 0):
            return half * half
        else:
            return half * half * x
    if (n < 0):
        x = 1 / x
        n = -n
    return fastPow(x, n)

print(myPow(2,16))


